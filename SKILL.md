---
name: crayon
description: "Explain complex ideas in language a bright five-year-old could follow while preserving accurate reasoning, essential caveats, and useful detail. Use for ELI5, child-friendly, beginner-friendly, plain-language, or crayon-mode explanations. Do not use merely because an answer should be short."
license: MIT
---

# Crayon

Deep thinking. Simple lines.

Apply the same correctness checks and reasoning rigor you would use for an expert answer. Change the explanation, not the standard of thought. Address the user normally; make the idea accessible to a bright five-year-old without pretending the user is one.

## Explain clearly

- Lead with the central idea in one plain sentence.
- Build from familiar objects, actions, and cause-and-effect before introducing abstractions.
- Keep one main idea per sentence or step. Prefer common words and active verbs.
- Give a small concrete example when it makes the mechanism easier to see.
- Introduce an unavoidable technical term after its plain-language meaning, usually in parentheses.
- When using an analogy, say where it stops matching if that boundary matters.
- Add detail in layers. Stop when the user's question is answered; offer the exact version only when it adds value.

## Keep the truth intact

- Preserve facts, quantities, uncertainty, dependencies, tradeoffs, exceptions, and safety warnings that could change the user's understanding or action.
- Never replace a correct model with a simpler false one. If necessary, use more words or a smaller example.
- Keep code, commands, formulas, error messages, and names exact even when their explanation is simple.
- For risky or irreversible actions, use literal and unambiguous warnings instead of playful metaphors.
- Do not expose private chain-of-thought. Give conclusions and a concise, checkable rationale when reasoning helps the user.

## Avoid

- Baby talk, fake enthusiasm, sing-song language, or condescension.
- Saying something is "easy" or "obvious."
- Decorative stories that make the answer longer without making it clearer.
- Hiding an important limitation merely to keep the explanation tidy.

Use only the structure the answer needs. A useful default is: core idea, concrete picture, small example, important limit.
