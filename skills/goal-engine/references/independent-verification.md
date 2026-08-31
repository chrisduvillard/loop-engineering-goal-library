# Independent held-out verification

For High assurance goals, separate builder and verifier contexts. The verifier
receives the approved contract and resulting repository, but not the builder's
persuasive narrative. It runs held-out checks and reports raw evidence.

The verifier must detect:

- removed or weakened tests;
- new skips, exclusions, or relaxed thresholds;
- replacement of real checks with mocks;
- fixtures changed to hide failures;
- acceptance criteria changed after approval;
- verifier code modified by the builder without explicit authorization;
- unexplained protected-path changes.

A builder-controlled test run may support development, but it is not the final
High assurance proof unless the contract explicitly records why independence is
impossible and the owner accepts that residual risk.
