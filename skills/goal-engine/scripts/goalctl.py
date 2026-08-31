#!/usr/bin/env python3
"""Deterministic lifecycle and evidence controls for Loop Engineering goals."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import secrets
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple

SCHEMA_VERSION = 1
FINGERPRINT_ALGORITHM = "goalctl-v1-sha256"
GOAL_ID = re.compile(r"^[a-z0-9][a-z0-9-]{2,63}$")
GOAL_STATUSES = {"candidate", "ready", "active", "paused", "blocked", "closed"}
MUTATION_MODES = {"read_only", "propose_patch", "apply_verified_fixes"}
ASSURANCE_LEVELS = {"lite", "standard", "high"}
ACCEPTANCE_STATUSES = {"not_run", "pass", "fail", "blocked"}
RUN_TERMINATIONS = {
    "achieved",
    "approval_required",
    "budget_exhausted",
    "stalled",
    "external_blocked",
    "safety_stop",
    "cancelled_by_user",
    "host_failure",
}
GOAL_OUTCOMES = {"achieved", "cancelled", "superseded", "abandoned"}
TRANSITIONS = {
    "candidate": {"ready"},
    "ready": {"active", "closed"},
    "active": {"paused", "blocked", "closed"},
    "paused": {"active", "blocked", "closed"},
    "blocked": {"active", "paused", "closed"},
    "closed": set(),
}


class GoalctlError(RuntimeError):
    pass


def now() -> datetime:
    return datetime.now(timezone.utc)


def iso(value: Optional[datetime] = None) -> str:
    return (value or now()).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def atomic_write(path: Path, content: bytes, mode: int = 0o600) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, mode)
        os.replace(str(temporary), str(path))
    finally:
        if temporary.exists():
            temporary.unlink()


def write_json(path: Path, value: Dict[str, Any]) -> None:
    atomic_write(path, json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False).encode("utf-8") + b"\n")


def read_json(path: Path) -> Dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise GoalctlError(f"Missing required state file: {path}") from error
    except json.JSONDecodeError as error:
        raise GoalctlError(f"Invalid JSON in {path}: {error}") from error
    if not isinstance(value, dict):
        raise GoalctlError(f"Expected a JSON object in {path}")
    return value


def state_paths(root: Path, goal_id: str) -> Tuple[Path, Path, Path, Path]:
    base = root / ".loop"
    goal = base / "goals" / goal_id
    return goal / "contract.json", goal / "progress.json", base / "active-goal.json", base / "leases" / f"{goal_id}.json"


def approval_payload(contract: Dict[str, Any]) -> Dict[str, Any]:
    keys = (
        "schema_version",
        "goal_id",
        "revision",
        "title",
        "mutation_mode",
        "assurance_level",
        "scope",
        "acceptance",
        "source",
        "protected_paths",
        "authority_boundaries",
    )
    payload = {key: copy.deepcopy(contract.get(key)) for key in keys}
    for item in payload.get("acceptance") or []:
        if isinstance(item, dict):
            item["status"] = "not_run"
            item["evidence"] = []
    return payload


def fingerprint(contract: Dict[str, Any]) -> str:
    return hashlib.sha256(canonical_json(approval_payload(contract))).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GoalctlError(message)


def validate_contract(contract: Dict[str, Any]) -> None:
    require(contract.get("schema_version") == SCHEMA_VERSION, "Unsupported contract schema_version")
    goal_id = contract.get("goal_id")
    require(isinstance(goal_id, str) and bool(GOAL_ID.fullmatch(goal_id)), "Invalid goal_id")
    require(isinstance(contract.get("revision"), int) and contract["revision"] >= 1, "Invalid revision")
    require(isinstance(contract.get("title"), str) and bool(contract["title"].strip()), "Missing title")
    status = contract.get("goal_status")
    require(status in GOAL_STATUSES, f"Invalid goal_status: {status!r}")
    mutation = contract.get("mutation_mode")
    require(mutation in MUTATION_MODES, f"Invalid mutation_mode: {mutation!r}")
    assurance = contract.get("assurance_level")
    require(assurance in ASSURANCE_LEVELS, f"Invalid assurance_level: {assurance!r}")
    outcome = contract.get("goal_outcome")
    require(outcome is None or outcome in GOAL_OUTCOMES, f"Invalid goal_outcome: {outcome!r}")
    acceptance = contract.get("acceptance")
    require(isinstance(acceptance, list) and bool(acceptance), "Acceptance list must not be empty")
    seen: Set[str] = set()
    for item in acceptance:
        require(isinstance(item, dict), "Acceptance items must be objects")
        item_id = item.get("id")
        require(isinstance(item_id, str) and bool(item_id), "Acceptance item missing id")
        require(item_id not in seen, f"Duplicate acceptance id: {item_id}")
        seen.add(item_id)
        require(isinstance(item.get("description"), str) and bool(item["description"].strip()), f"{item_id}: missing description")
        require(item.get("status") in ACCEPTANCE_STATUSES, f"{item_id}: invalid status")
        require(isinstance(item.get("evidence"), list), f"{item_id}: evidence must be a list")
    approval = contract.get("approval")
    require(isinstance(approval, dict), "Missing approval object")
    require(approval.get("algorithm") == FINGERPRINT_ALGORITHM, "Unsupported approval fingerprint algorithm")
    approved = approval.get("approved") is True
    if approved:
        require(approval.get("fingerprint") == fingerprint(contract), "Approval fingerprint does not match the canonical contract")
        require(bool(approval.get("question_id")), "Approved contract missing approval question id")
        require(bool(approval.get("answer")), "Approved contract missing approval answer")
    if status in {"ready", "active", "paused", "blocked", "closed"}:
        require(approved, f"Goal status {status!r} requires approval")
    if status == "closed":
        require(outcome in GOAL_OUTCOMES, "Closed goal requires a final goal_outcome")
    else:
        require(outcome is None, "Open goal must not have a final goal_outcome")
    if outcome == "achieved":
        require(all(item["status"] == "pass" for item in acceptance), "Achieved outcome requires every acceptance item to pass")


def validate_progress(progress: Dict[str, Any], contract: Dict[str, Any]) -> None:
    require(progress.get("schema_version") == SCHEMA_VERSION, "Unsupported progress schema_version")
    require(progress.get("goal_id") == contract.get("goal_id"), "Progress goal_id does not match contract")
    require(progress.get("revision") == contract.get("revision"), "Progress revision does not match contract")
    termination = progress.get("run_termination")
    require(termination is None or termination in RUN_TERMINATIONS, f"Invalid run_termination: {termination!r}")
    verifier = progress.get("verifier")
    require(isinstance(verifier, dict), "Missing verifier object")
    require(isinstance(verifier.get("evidence"), list), "Verifier evidence must be a list")
    require(isinstance(progress.get("changed_paths"), list), "changed_paths must be a list")
    if termination == "achieved":
        require(verifier.get("succeeded") is True and verifier.get("exit_code") == 0, "Achieved run requires a successful verifier")
        require(all(item["status"] == "pass" for item in contract["acceptance"]), "Achieved run requires every acceptance item to pass")


def transition(contract: Dict[str, Any], target: str) -> None:
    current = contract["goal_status"]
    require(target in TRANSITIONS[current], f"Invalid goal transition: {current} -> {target}")
    contract["goal_status"] = target
    contract["updated_at"] = iso()


def initialize(root: Path, goal_id: str, title: str, mutation_mode: str, assurance_level: str, acceptance_texts: Sequence[str]) -> None:
    require(bool(GOAL_ID.fullmatch(goal_id)), "goal_id must match ^[a-z0-9][a-z0-9-]{2,63}$")
    require(mutation_mode in MUTATION_MODES, "Invalid mutation mode")
    require(assurance_level in ASSURANCE_LEVELS, "Invalid assurance level")
    require(bool(acceptance_texts), "At least one acceptance criterion is required")
    contract_path, progress_path, active_path, _ = state_paths(root, goal_id)
    require(not contract_path.exists(), f"Goal already exists: {goal_id}")
    timestamp = iso()
    contract: Dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "goal_id": goal_id,
        "revision": 1,
        "title": title,
        "goal_status": "candidate",
        "goal_outcome": None,
        "mutation_mode": mutation_mode,
        "assurance_level": assurance_level,
        "scope": {"included": [], "excluded": []},
        "acceptance": [
            {"id": f"A{index}", "description": text, "status": "not_run", "evidence": []}
            for index, text in enumerate(acceptance_texts, 1)
        ],
        "approval": {
            "approved": False,
            "question_id": None,
            "answer": None,
            "approved_at": None,
            "fingerprint": None,
            "algorithm": FINGERPRINT_ALGORITHM,
        },
        "source": {"branch": None, "commit": None},
        "protected_paths": [],
        "authority_boundaries": [],
        "created_at": timestamp,
        "updated_at": timestamp,
    }
    progress: Dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "goal_id": goal_id,
        "revision": 1,
        "run_termination": None,
        "verifier": {"command": None, "exit_code": None, "succeeded": None, "evidence": []},
        "changed_paths": [],
        "next_action": "Complete shaping and obtain explicit approval.",
        "updated_at": timestamp,
    }
    validate_contract(contract)
    validate_progress(progress, contract)
    write_json(contract_path, contract)
    write_json(progress_path, progress)
    write_json(
        active_path,
        {
            "schema_version": SCHEMA_VERSION,
            "goal_id": goal_id,
            "revision": 1,
            "contract_path": str(contract_path.relative_to(root)).replace(os.sep, "/"),
            "progress_path": str(progress_path.relative_to(root)).replace(os.sep, "/"),
            "updated_at": timestamp,
        },
    )
    render(root, goal_id)


def approve(root: Path, goal_id: str, question_id: str, answer: str) -> str:
    contract_path, _, _, _ = state_paths(root, goal_id)
    contract = read_json(contract_path)
    validate_contract(contract)
    require(contract["goal_status"] == "candidate", "Only a candidate contract can be approved")
    contract["approval"] = {
        "approved": True,
        "question_id": question_id,
        "answer": answer,
        "approved_at": iso(),
        "fingerprint": None,
        "algorithm": FINGERPRINT_ALGORITHM,
    }
    contract["approval"]["fingerprint"] = fingerprint(contract)
    transition(contract, "ready")
    validate_contract(contract)
    write_json(contract_path, contract)
    render(root, goal_id)
    return contract["approval"]["fingerprint"]


def read_lease(path: Path) -> Optional[Dict[str, Any]]:
    if not path.exists():
        return None
    lease = read_json(path)
    required = {"schema_version", "goal_id", "owner", "acquired_at", "expires_at", "token"}
    require(required.issubset(lease), f"Malformed lease: {path}")
    return lease


def acquire_lease(root: Path, goal_id: str, owner: str, ttl_seconds: int) -> Dict[str, Any]:
    require(bool(owner.strip()), "Lease owner is required")
    require(30 <= ttl_seconds <= 86400, "Lease TTL must be between 30 and 86400 seconds")
    _, _, _, path = state_paths(root, goal_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = read_lease(path)
    current = now()
    if existing is not None:
        if existing["owner"] == owner:
            existing["expires_at"] = iso(current + timedelta(seconds=ttl_seconds))
            write_json(path, existing)
            return existing
        if parse_time(existing["expires_at"]) > current:
            raise GoalctlError(f"Goal lease is held by {existing['owner']} until {existing['expires_at']}")
        stale = path.with_name(f"{path.name}.stale-{secrets.token_hex(4)}")
        try:
            os.replace(str(path), str(stale))
        except FileNotFoundError:
            pass
    lease = {
        "schema_version": SCHEMA_VERSION,
        "goal_id": goal_id,
        "owner": owner,
        "acquired_at": iso(current),
        "expires_at": iso(current + timedelta(seconds=ttl_seconds)),
        "token": secrets.token_hex(16),
    }
    payload = json.dumps(lease, indent=2, sort_keys=True).encode("utf-8") + b"\n"
    try:
        descriptor = os.open(str(path), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError as error:
        raise GoalctlError("Lease acquisition lost a concurrent race; retry after inspecting the current owner") from error
    with os.fdopen(descriptor, "wb") as handle:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())
    return lease


def release_lease(root: Path, goal_id: str, owner: str, token: Optional[str] = None) -> None:
    _, _, _, path = state_paths(root, goal_id)
    lease = read_lease(path)
    if lease is None:
        return
    require(lease["owner"] == owner, f"Lease is owned by {lease['owner']}, not {owner}")
    if token is not None:
        require(lease["token"] == token, "Lease token does not match")
    path.unlink()


def activate(root: Path, goal_id: str, owner: str, ttl_seconds: int) -> Dict[str, Any]:
    contract_path, _, _, _ = state_paths(root, goal_id)
    contract = read_json(contract_path)
    validate_contract(contract)
    require(contract["goal_status"] in {"ready", "paused", "blocked"}, "Only ready, paused, or blocked goals can be activated")
    lease = acquire_lease(root, goal_id, owner, ttl_seconds)
    transition(contract, "active")
    validate_contract(contract)
    write_json(contract_path, contract)
    render(root, goal_id)
    return lease


def checkpoint(
    root: Path,
    goal_id: str,
    acceptance_updates: Sequence[str],
    evidence_updates: Sequence[str],
    verifier_command: Optional[str],
    verifier_exit: Optional[int],
    next_action: Optional[str],
) -> None:
    contract_path, progress_path, _, _ = state_paths(root, goal_id)
    contract = read_json(contract_path)
    progress = read_json(progress_path)
    validate_contract(contract)
    validate_progress(progress, contract)
    require(contract["goal_status"] == "active", "Checkpoint requires an active goal")
    by_id = {item["id"]: item for item in contract["acceptance"]}
    for update in acceptance_updates:
        item_id, separator, status = update.partition("=")
        require(bool(separator) and item_id in by_id and status in ACCEPTANCE_STATUSES, f"Invalid acceptance update: {update}")
        by_id[item_id]["status"] = status
    for update in evidence_updates:
        item_id, separator, evidence = update.partition("=")
        require(bool(separator) and item_id in by_id and bool(evidence), f"Invalid evidence update: {update}")
        by_id[item_id]["evidence"].append(evidence)
    if verifier_command is not None:
        require(verifier_exit is not None, "Verifier exit code is required with a verifier command")
        progress["verifier"] = {
            "command": verifier_command,
            "exit_code": verifier_exit,
            "succeeded": verifier_exit == 0,
            "evidence": progress["verifier"].get("evidence", []),
        }
    if next_action is not None:
        progress["next_action"] = next_action
    timestamp = iso()
    contract["updated_at"] = timestamp
    progress["updated_at"] = timestamp
    progress["run_termination"] = None
    validate_contract(contract)
    validate_progress(progress, contract)
    write_json(contract_path, contract)
    write_json(progress_path, progress)
    render(root, goal_id)


def terminate(root: Path, goal_id: str, reason: str, next_action: Optional[str]) -> None:
    contract_path, progress_path, _, _ = state_paths(root, goal_id)
    contract = read_json(contract_path)
    progress = read_json(progress_path)
    validate_contract(contract)
    validate_progress(progress, contract)
    require(reason in RUN_TERMINATIONS - {"achieved"}, "Use close --outcome achieved for achieved runs")
    progress["run_termination"] = reason
    if next_action is not None:
        progress["next_action"] = next_action
    target = "blocked" if reason in {"external_blocked", "safety_stop"} else "paused"
    if contract["goal_status"] == "active":
        transition(contract, target)
    progress["updated_at"] = iso()
    validate_contract(contract)
    validate_progress(progress, contract)
    write_json(contract_path, contract)
    write_json(progress_path, progress)
    render(root, goal_id)


def close(root: Path, goal_id: str, outcome: str) -> None:
    contract_path, progress_path, active_path, _ = state_paths(root, goal_id)
    contract = read_json(contract_path)
    progress = read_json(progress_path)
    validate_contract(contract)
    validate_progress(progress, contract)
    require(outcome in GOAL_OUTCOMES, "Invalid goal outcome")
    require(contract["goal_status"] != "closed", "Goal is already closed")
    if outcome == "achieved":
        require(all(item["status"] == "pass" for item in contract["acceptance"]), "False-completion guard: every acceptance item must pass")
        require(progress["verifier"].get("succeeded") is True, "False-completion guard: verifier must succeed")
        require(progress["verifier"].get("exit_code") == 0, "False-completion guard: verifier exit code must be zero")
        progress["run_termination"] = "achieved"
    elif outcome == "cancelled":
        progress["run_termination"] = "cancelled_by_user"
    contract["goal_outcome"] = outcome
    transition(contract, "closed")
    timestamp = iso()
    progress["updated_at"] = timestamp
    progress["next_action"] = None
    validate_contract(contract)
    validate_progress(progress, contract)
    write_json(contract_path, contract)
    write_json(progress_path, progress)
    if active_path.exists():
        active = read_json(active_path)
        if active.get("goal_id") == goal_id:
            active_path.unlink()
    render(root, goal_id)


def source_hash(value: Dict[str, Any]) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


def render(root: Path, goal_id: str) -> None:
    contract_path, progress_path, _, _ = state_paths(root, goal_id)
    contract = read_json(contract_path)
    progress = read_json(progress_path)
    validate_contract(contract)
    validate_progress(progress, contract)
    contract_lines = [
        "# Generated Goal Contract",
        "",
        f"> Generated from `{contract_path.relative_to(root).as_posix()}`.",
        f"> Source hash: `{source_hash(contract)}`. Do not edit this view directly.",
        "",
        f"- Goal ID: `{contract['goal_id']}`",
        f"- Revision: `{contract['revision']}`",
        f"- Title: {contract['title']}",
        f"- Goal status: `{contract['goal_status']}`",
        f"- Final outcome: `{contract['goal_outcome']}`",
        f"- Mutation mode: `{contract['mutation_mode']}`",
        f"- Assurance level: `{contract['assurance_level']}`",
        f"- Approval fingerprint: `{contract['approval'].get('fingerprint')}`",
        "",
        "## Acceptance",
        "",
    ]
    for item in contract["acceptance"]:
        contract_lines.append(f"- **{item['id']}** [{item['status']}]: {item['description']}")
        for evidence in item["evidence"]:
            contract_lines.append(f"  - Evidence: {evidence}")
    progress_lines = [
        "# Generated Goal Progress",
        "",
        f"> Generated from `{progress_path.relative_to(root).as_posix()}`.",
        f"> Source hash: `{source_hash(progress)}`. Do not edit this view directly.",
        "",
        f"- Goal ID: `{progress['goal_id']}`",
        f"- Revision: `{progress['revision']}`",
        f"- Run termination: `{progress['run_termination']}`",
        f"- Verifier command: `{progress['verifier'].get('command')}`",
        f"- Verifier exit code: `{progress['verifier'].get('exit_code')}`",
        f"- Verifier succeeded: `{progress['verifier'].get('succeeded')}`",
        f"- Next action: {progress.get('next_action')}",
        "",
        "## Changed paths",
        "",
    ]
    progress_lines.extend(f"- `{path}`" for path in progress.get("changed_paths", []))
    atomic_write(root / "GOAL.md", ("\n".join(contract_lines).rstrip() + "\n").encode("utf-8"), 0o644)
    atomic_write(root / "GOAL_PROGRESS.md", ("\n".join(progress_lines).rstrip() + "\n").encode("utf-8"), 0o644)


def changed_paths(root: Path) -> Set[str]:
    try:
        tracked = subprocess.run(
            ["git", "diff", "--name-only", "--no-ext-diff", "HEAD"],
            cwd=str(root),
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).stdout.splitlines()
        untracked = subprocess.run(
            ["git", "ls-files", "--others", "--exclude-standard"],
            cwd=str(root),
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).stdout.splitlines()
    except (OSError, subprocess.CalledProcessError) as error:
        raise GoalctlError(f"Unable to inspect Git worktree: {error}") from error
    return {path.replace(os.sep, "/") for path in tracked + untracked if path}


def mutation_violations(root: Path, goal_id: str) -> List[str]:
    contract_path, _, _, _ = state_paths(root, goal_id)
    contract = read_json(contract_path)
    validate_contract(contract)
    if contract["mutation_mode"] == "apply_verified_fixes":
        return []
    allowed_exact = {"GOAL.md", "GOAL_PROGRESS.md"}
    allowed_prefixes = {".loop/", f"docs/goals/{goal_id}/"}
    violations = []
    for path in sorted(changed_paths(root)):
        if path in allowed_exact or any(path.startswith(prefix) for prefix in allowed_prefixes):
            continue
        violations.append(path)
    return violations


def verify_mutation(root: Path, goal_id: str) -> None:
    violations = mutation_violations(root, goal_id)
    require(not violations, "Mutation mode violation outside goal state paths: " + ", ".join(violations))


def sanitize_text(text: str) -> str:
    patterns = (
        (re.compile(r"(?i)(api[_-]?key\s*[:=]\s*)[^\s,;]+"), r"\1[REDACTED]"),
        (re.compile(r"(?i)(token\s*[:=]\s*)[^\s,;]+"), r"\1[REDACTED]"),
        (re.compile(r"(?i)(password\s*[:=]\s*)[^\s,;]+"), r"\1[REDACTED]"),
        (re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"), "[REDACTED_GITHUB_TOKEN]"),
        (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "[REDACTED_AWS_KEY]"),
    )
    result = text
    for pattern, replacement in patterns:
        result = pattern.sub(replacement, result)
    return result


def doctor(root: Path) -> List[Tuple[str, str]]:
    checks: List[Tuple[str, str]] = []
    checks.append(("python", sys.version.split()[0]))
    git = subprocess.run(["git", "--version"], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    checks.append(("git", git.stdout.strip() if git.returncode == 0 else "unavailable"))
    checks.append(("repository", "yes" if (root / ".git").exists() else "no"))
    active_path = root / ".loop" / "active-goal.json"
    if active_path.exists():
        active = read_json(active_path)
        goal_id = str(active.get("goal_id"))
        contract_path, progress_path, _, lease_path = state_paths(root, goal_id)
        contract = read_json(contract_path)
        progress = read_json(progress_path)
        validate_contract(contract)
        validate_progress(progress, contract)
        checks.append(("active_goal", goal_id))
        checks.append(("goal_status", str(contract["goal_status"])))
        checks.append(("lease", "present" if lease_path.exists() else "missing"))
    else:
        checks.append(("active_goal", "none"))
    return checks


def self_test() -> None:
    with tempfile.TemporaryDirectory(prefix="goalctl-self-test-") as temporary:
        root = Path(temporary)
        subprocess.run(["git", "init", "-q"], cwd=str(root), check=True)
        subprocess.run(["git", "config", "user.email", "goalctl@example.invalid"], cwd=str(root), check=True)
        subprocess.run(["git", "config", "user.name", "goalctl self-test"], cwd=str(root), check=True)
        (root / "README.md").write_text("baseline\n", encoding="utf-8")
        subprocess.run(["git", "add", "README.md"], cwd=str(root), check=True)
        subprocess.run(["git", "commit", "-q", "-m", "baseline"], cwd=str(root), check=True)

        initialize(root, "self-test-goal", "Self-test", "read_only", "high", ["Verifier succeeds"])
        approval_fingerprint = approve(root, "self-test-goal", "R1-Q1", "Approved")
        require(len(approval_fingerprint) == 64, "Fingerprint length is invalid")
        lease = activate(root, "self-test-goal", "self-test", 60)
        require(lease["owner"] == "self-test", "Lease owner mismatch")

        (root / "README.md").write_text("unauthorized mutation\n", encoding="utf-8")
        require("README.md" in mutation_violations(root, "self-test-goal"), "Read-only mutation was not detected")
        subprocess.run(["git", "checkout", "--", "README.md"], cwd=str(root), check=True)

        checkpoint(root, "self-test-goal", ["A1=fail"], ["A1=expected negative proof"], "false", 1, "Repair verifier")
        try:
            close(root, "self-test-goal", "achieved")
        except GoalctlError:
            pass
        else:
            raise GoalctlError("False-completion guard accepted a failed verifier")

        checkpoint(root, "self-test-goal", ["A1=pass"], ["A1=self-test verifier exit 0"], "true", 0, "Close goal")
        verify_mutation(root, "self-test-goal")
        close(root, "self-test-goal", "achieved")
        contract_path, progress_path, _, _ = state_paths(root, "self-test-goal")
        contract = read_json(contract_path)
        progress = read_json(progress_path)
        validate_contract(contract)
        validate_progress(progress, contract)
        require(contract["goal_outcome"] == "achieved", "Final outcome mismatch")
        require(progress["run_termination"] == "achieved", "Run termination mismatch")
        release_lease(root, "self-test-goal", "self-test", lease["token"])
        require("[REDACTED]" in sanitize_text("api_key=secret-value"), "Sanitizer failed")
    print("goalctl self-test passed")


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(prog="goalctl")
    result.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root")
    sub = result.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init")
    init.add_argument("goal_id")
    init.add_argument("--title", required=True)
    init.add_argument("--mutation-mode", choices=sorted(MUTATION_MODES), default="read_only")
    init.add_argument("--assurance-level", choices=sorted(ASSURANCE_LEVELS), default="standard")
    init.add_argument("--acceptance", action="append", required=True)

    approval = sub.add_parser("approve")
    approval.add_argument("goal_id")
    approval.add_argument("--question-id", required=True)
    approval.add_argument("--answer", required=True)

    activation = sub.add_parser("activate")
    activation.add_argument("goal_id")
    activation.add_argument("--owner", required=True)
    activation.add_argument("--ttl", type=int, default=1800)

    checkpoint_parser = sub.add_parser("checkpoint")
    checkpoint_parser.add_argument("goal_id")
    checkpoint_parser.add_argument("--acceptance", action="append", default=[])
    checkpoint_parser.add_argument("--evidence", action="append", default=[])
    checkpoint_parser.add_argument("--verifier-command")
    checkpoint_parser.add_argument("--verifier-exit", type=int)
    checkpoint_parser.add_argument("--next-action")

    termination = sub.add_parser("terminate")
    termination.add_argument("goal_id")
    termination.add_argument("--reason", choices=sorted(RUN_TERMINATIONS - {"achieved"}), required=True)
    termination.add_argument("--next-action")

    closing = sub.add_parser("close")
    closing.add_argument("goal_id")
    closing.add_argument("--outcome", choices=sorted(GOAL_OUTCOMES), required=True)

    validation = sub.add_parser("validate")
    validation.add_argument("goal_id")

    rendering = sub.add_parser("render")
    rendering.add_argument("goal_id")

    mutation = sub.add_parser("verify-mutation")
    mutation.add_argument("goal_id")

    acquire = sub.add_parser("acquire-lease")
    acquire.add_argument("goal_id")
    acquire.add_argument("--owner", required=True)
    acquire.add_argument("--ttl", type=int, default=1800)

    release = sub.add_parser("release-lease")
    release.add_argument("goal_id")
    release.add_argument("--owner", required=True)
    release.add_argument("--token")

    sanitization = sub.add_parser("sanitize")
    sanitization.add_argument("source", type=Path)
    sanitization.add_argument("--output", type=Path)

    sub.add_parser("doctor")
    sub.add_parser("self-test")
    return result


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parser().parse_args(argv)
    root = args.root.expanduser().resolve()
    try:
        if args.command == "init":
            initialize(root, args.goal_id, args.title, args.mutation_mode, args.assurance_level, args.acceptance)
        elif args.command == "approve":
            print(approve(root, args.goal_id, args.question_id, args.answer))
        elif args.command == "activate":
            print(json.dumps(activate(root, args.goal_id, args.owner, args.ttl), indent=2, sort_keys=True))
        elif args.command == "checkpoint":
            checkpoint(root, args.goal_id, args.acceptance, args.evidence, args.verifier_command, args.verifier_exit, args.next_action)
        elif args.command == "terminate":
            terminate(root, args.goal_id, args.reason, args.next_action)
        elif args.command == "close":
            close(root, args.goal_id, args.outcome)
        elif args.command == "validate":
            contract_path, progress_path, _, _ = state_paths(root, args.goal_id)
            contract = read_json(contract_path)
            progress = read_json(progress_path)
            validate_contract(contract)
            validate_progress(progress, contract)
            print("valid")
        elif args.command == "render":
            render(root, args.goal_id)
        elif args.command == "verify-mutation":
            verify_mutation(root, args.goal_id)
            print("mutation mode satisfied")
        elif args.command == "acquire-lease":
            print(json.dumps(acquire_lease(root, args.goal_id, args.owner, args.ttl), indent=2, sort_keys=True))
        elif args.command == "release-lease":
            release_lease(root, args.goal_id, args.owner, args.token)
        elif args.command == "sanitize":
            sanitized = sanitize_text(args.source.read_text(encoding="utf-8"))
            if args.output:
                atomic_write(args.output, sanitized.encode("utf-8"), 0o600)
            else:
                sys.stdout.write(sanitized)
        elif args.command == "doctor":
            for name, value in doctor(root):
                print(f"{name}: {value}")
        elif args.command == "self-test":
            self_test()
        else:
            raise GoalctlError(f"Unsupported command: {args.command}")
    except GoalctlError as error:
        print(f"goalctl: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
