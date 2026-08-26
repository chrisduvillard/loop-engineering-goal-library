# Goal Shaping History: Portfolio Import v1.4

**Goal ID:** 2026-08-25-portfolio-import-v1-4  
**Contract:** `CONTRACT.md`  
**Lifecycle state:** Closed  
**Created:** 2026-08-25  
**Last updated:** 2026-08-25  
**Completed rounds:** 2 — R1, R2  
**Latest round:** R2  
**Approval round:** R2

## Current decision index

| Decision | Current answer | Source | Contract impact | Status |
|---|---|---|---|---|
| Supported spreadsheet formats | CSV and XLSX only | R1-Q1 | In scope / out of scope | Current |
| Export compatibility | Existing export formats and public error codes must not change | R1-Q2 | Protected behavior | Current |
| Spreadsheet date semantics | Normalize Excel serial dates only at the XLSX parser boundary | R2-Q1 | Target / acceptance evidence | Current |
| Performance work | Separate follow-on goal after correctness is proven | R2-Q2 | Out of scope / portfolio | Current |

## Round R1 — Initial shaping

**Purpose:** Resolve the minimum product and compatibility decisions for the import milestone.  
**Started / completed:** 2026-08-25  
**Lenses covered:** outcome, scope, compatibility, evidence

### Questions and answers

#### R1-Q1 — Supported formats

- **Status:** Answered
- **Why this was asked:** The PRD mentioned spreadsheets broadly, while the existing product supported CSV and the branch contained partial XLSX code.
- **Evidence considered:** `docs/product/portfolio-import-v1.4.md`, import routes, parser registry, and current tests.
- **Recommendation:** Limit this goal to CSV and XLSX; broker-specific formats belong in later goals.
- **Options or trade-off:** CSV+XLSX now; all spreadsheet formats; broker-specific adapters.
- **Exact question:**

> Should this milestone finish the documented CSV and XLSX workflow only, or expand to additional spreadsheet and broker-specific formats?

- **User answer:**

> Keep it to CSV and XLSX. Broker-specific adapters can be separate later.

- **Normalized decision:** CSV and XLSX are in scope; new broker formats are out of scope.
- **Contract impact:** In scope, out of scope, acceptance matrix.
- **Supersedes:** None.

#### R1-Q2 — Compatibility boundary

- **Status:** Answered
- **Why this was asked:** A global normalization approach could alter existing CSV values and frontend error handling.
- **Evidence considered:** Export tests, frontend error-code consumers, and current CSV fixtures.
- **Recommendation:** Protect existing exports, CSV behavior, and public error codes.
- **Options or trade-off:** Preserve all existing contracts; permit an approved breaking change; redesign the wider import/export domain.
- **Exact question:**

> Should this goal preserve the existing CSV import, export formats, and public error codes exactly?

- **User answer:**

> Yes. This goal should only complete XLSX support and must not break existing imports or exports.

- **Normalized decision:** Existing CSV, exports, and public error codes are protected behavior.
- **Contract impact:** Protected behavior and regression gates.
- **Supersedes:** None.

### Round summary

- **New decisions:** Limited scope to CSV/XLSX; protected existing import/export contracts.
- **Contract revisions:** Added format exclusions and export regression gate.
- **Remaining uncertainty:** Exact XLSX date semantics and whether performance belongs in this goal.
- **Readiness:** Deeper shaping recommended.
- **Next step:** Run R2.

## Round R2 — Deepening

**Purpose:** Challenge the data semantics and prevent hidden performance scope.  
**Started / completed:** 2026-08-25  
**Lenses covered:** data semantics, failure cases, scope, follow-on work

### Questions and answers

#### R2-Q1 — Date normalization boundary

- **Status:** Answered
- **Why this was asked:** Tests showed failing Excel serial-date cases, but a shared post-parse coercion could change valid CSV strings.
- **Evidence considered:** Four failing XLSX tests, CSV parser behavior, and the proposed global-coercion diff.
- **Recommendation:** Normalize only at the XLSX parser boundary and add format-specific fixtures.
- **Options or trade-off:** XLSX-boundary normalization; global post-parse coercion; leave serial values unchanged.
- **Exact question:**

> Should Excel serial dates be normalized only inside the XLSX adapter, so shared CSV and domain behavior remain unchanged?

- **User answer:**

> Yes. Keep it specific to XLSX and protect it with a real workbook fixture.

- **Normalized decision:** XLSX-only parser-boundary normalization with fixture-based regression coverage.
- **Contract impact:** Target, implementation constraint, acceptance evidence.
- **Supersedes:** None.

#### R2-Q2 — Performance scope

- **Status:** Answered
- **Why this was asked:** Large-file latency was mentioned in a backlog note but had no approved target or benchmark.
- **Evidence considered:** Roadmap, absence of a stable benchmark, and the correctness milestone dependency.
- **Recommendation:** Finish correctness first; create a separate measured optimization goal afterward.
- **Options or trade-off:** Include unbounded performance work now; defer it; define a separate benchmark goal.
- **Exact question:**

> Should large-file performance remain outside this contract and become a separate benchmarked goal after correctness is proven?

- **User answer:**

> Yes. Correctness first, then a separate performance goal with a real budget.

- **Normalized decision:** Performance optimization is out of scope and added as a ready follow-on portfolio goal.
- **Contract impact:** Out of scope, portfolio, follow-on relationship.
- **Supersedes:** None.

### Round summary

- **New decisions:** XLSX-only normalization; performance separated into a follow-on goal.
- **Contract revisions:** Added parser-boundary constraint, fixture evidence, and follow-on goal relationship.
- **Remaining uncertainty:** None material.
- **Readiness:** Ready for approval.
- **Next step:** Contract approved from R2.

## Corrections and supersessions

_None._

## Open and deferred decisions

| Decision | Status | Why unresolved | Owner / trigger | Contract treatment |
|---|---|---|---|---|
| Large-file performance budget | Deferred | Requires a stable correctness baseline and benchmark protocol | Follow-on goal | Out of scope; tracked in portfolio |
