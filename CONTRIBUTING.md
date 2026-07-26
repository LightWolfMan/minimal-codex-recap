# Contributing

Thanks for helping keep Minimal Codex Recap small and predictable.

## Principles

- Preserve explicit-only invocation.
- Keep the skill free of runtime dependencies and executable code.
- Use only the current conversation as source material.
- Never add file reads, tool calls, persistent memory, network access, or state
  changes to the recap workflow.
- Keep the default output contract at exactly three lines.
- Prefer honest fallbacks over inferred or invented progress.

## Development

1. Create a branch from `main`.
2. Make the smallest change that solves the problem.
3. Run:

   ```bash
   python tests/validate_skill.py
   ```

4. If `SKILL.md` or `agents/openai.yaml` changes intentionally, update the
   approved hashes in the test and both README files.
5. Explain any behavioral change in `CHANGELOG.md`.

Pull requests should include a concrete conversation example and the expected
three-line result.
