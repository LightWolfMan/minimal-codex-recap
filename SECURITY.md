# Security Policy

## Scope

Minimal Codex Recap contains no executable runtime code. Its security boundary
is the instruction contract in `SKILL.md`.

Please report any behavior that causes `$recap` to:

- call a tool or command;
- read a file or persistent memory;
- access the network;
- change local or remote state;
- disclose information not already present in the current conversation;
- run through implicit invocation.

## Reporting

Do not open a public issue if a report contains sensitive conversation data.
Use GitHub's private security advisory flow for this repository instead.

Include the Codex version, surface (App or CLI), exact invocation, sanitized
output, and whether the skill was installed globally or per project.
