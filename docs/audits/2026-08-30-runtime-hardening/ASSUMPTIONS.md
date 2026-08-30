# Assumptions

- Version 0.11.1 remains a beta release.
- Existing profile semantics and generated launchers remain compatible.
- Read-only state artifacts may be written only in the approved goal-state paths.
- Standalone packages remain supported, so their transitive assets are vendored
  and checked for drift rather than silently removed.
- The integrated Claude plugin metadata complements, rather than replaces, the
  portable Agent Skills installation path.
