# Version 0.11.1 release gate

A release is eligible only when the pull-request validation workflow succeeds on
the complete candidate tree, the squash merge succeeds, the main-branch
validation succeeds, and the release packages are rebuilt from the merged commit.

The release must contain the two self-contained standalone ZIPs, the combined
bundle, and `SHA256SUMS`. Version metadata, filenames, tag, changelog, and source
commit must agree.
