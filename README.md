# Crayon

[![Validate skill](https://github.com/Krabbens/crayon/actions/workflows/validate.yml/badge.svg)](https://github.com/Krabbens/crayon/actions/workflows/validate.yml)

> Deep thinking. Simple lines.

Crayon is a Codex skill for explaining difficult ideas in plain language, with the detail needed to answer your question.

It adapts to what you already know:

- adult beginner explanations by default; child-level explanations when requested;
- direct answers, with examples or analogies when they help;
- standard technical names, with unfamiliar terms briefly explained;
- facts, limits, and warnings needed for an accurate answer;
- persistent mode when Crayon is explicitly activated;
- length and depth matched to the current request.

## Install

Clone the repository into your personal Codex skills directory:

```bash
git clone https://github.com/Krabbens/crayon.git "${CODEX_HOME:-$HOME/.codex}/skills/crayon"
```

Restart Codex if the skill does not appear immediately.

## Use

Invoke the skill directly to turn on persistent mode:

```text
$crayon Explain how a database index works.
```

Crayon briefly confirms activation in your language, for example:

```text
🖍️ Crayon on.
```

The confirmation is omitted when you request an exact output format, such as JSON only. The plain-language preference remains active across follow-ups and topic changes; your current request still determines language, depth, length, and format. Turn it off with any of:

```text
stop crayon
crayon off
normal mode
```

Crayon may also be selected automatically for a one-off request such as:

```text
Explain TLS certificates like I'm five, but keep the important security details.
```

One-off ELI5 or plain-language requests do not enable persistent mode unless the user explicitly invokes Crayon. Quoting or discussing the skill's name does not activate it.

## Example

**Question:** What is a database index?

**Crayon-style answer:**

> An index helps a database find matching records without checking every record in turn. It takes extra space and needs updating when the indexed data changes.

Ask for more depth to explore how the index works internally.

## Design

The complete activation, persistence, and explanation rules live in [`SKILL.md`](SKILL.md). UI metadata and implicit-invocation policy live in [`agents/openai.yaml`](agents/openai.yaml). Representative behavioral checks are documented in [`evals/cases.md`](evals/cases.md).

Run the dependency-free structural validator with:

```bash
python3 scripts/validate_skill.py .
```

This checks repository structure. Evaluate clarity, accuracy, and unnecessary repetition separately using the behavioral cases.

## Contributing

Small, evidence-backed improvements are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

[MIT](LICENSE) © 2026 Kosma Gąsiorowski
