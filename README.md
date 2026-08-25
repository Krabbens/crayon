# Crayon

[![Validate skill](https://github.com/Krabbens/crayon/actions/workflows/validate.yml/badge.svg)](https://github.com/Krabbens/crayon/actions/workflows/validate.yml)

> Deep thinking. Simple lines.

Crayon is a Codex skill for explaining difficult ideas in language a bright five-year-old could follow—without weakening the reasoning, hiding uncertainty, or dropping important caveats.

Crayon changes the interface, not the intelligence:

- simple words, concrete examples, and short causal steps;
- exact technical terms introduced only after their plain meaning;
- important tradeoffs, limits, and safety warnings preserved;
- no baby talk, condescension, or misleading simplification.

## Install

Clone the repository into your personal Codex skills directory:

```bash
git clone https://github.com/Krabbens/crayon.git "${CODEX_HOME:-$HOME/.codex}/skills/crayon"
```

Restart Codex if the skill does not appear immediately.

## Use

Invoke the skill directly:

```text
$crayon Explain how a database index works.
```

It may also be selected automatically for requests such as:

```text
Explain TLS certificates like I'm five, but keep the important security details.
```

## Example

**Question:** What is a database index?

**Crayon-style answer:**

> Imagine a big book of names. Without an index, the database may need to check every page to find “Maya.” An index is a smaller, sorted list that says where each name lives, so the database can jump close to the right place. The tradeoff is that the index takes extra space and must also be updated whenever the data changes.

The explanation stays approachable while retaining the mechanism and its main tradeoff.

## Design

The complete agent instructions live in [`SKILL.md`](SKILL.md). UI metadata lives in [`agents/openai.yaml`](agents/openai.yaml). Representative behavioral checks are documented in [`evals/cases.md`](evals/cases.md).

Run the dependency-free structural validator with:

```bash
python3 scripts/validate_skill.py .
```

## Contributing

Small, evidence-backed improvements are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

[MIT](LICENSE) © 2026 Kosma Gąsiorowski
