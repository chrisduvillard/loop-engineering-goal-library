# Security policy

## Supported versions

Security fixes are applied to the latest tagged release and the default branch.
Pre-1.0 versions are beta software and may change incompatibly when a safety
boundary needs strengthening.

## Reporting a vulnerability

Do not open a public issue for a vulnerability that could enable unauthorized
repository changes, secret disclosure, workflow compromise, path traversal,
unsafe archive extraction, approval bypass, lease bypass, or false completion.
Use GitHub's private vulnerability reporting feature for this repository.
Include the affected version, reproduction steps, impact, and any proposed
mitigation. Remove credentials, customer data, and other private material from
reports.

## Response principles

Reports are triaged by severity and exploitability. A fix is not considered
complete until a regression test covers the failure mode and packaged artifacts
have been revalidated. Release notes describe the security impact without
publishing unnecessary exploit detail before users can update.
