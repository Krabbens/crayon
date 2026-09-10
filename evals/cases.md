# Behavioral evaluation cases

Use these prompts for forward testing. Judge the answer by the invariants below rather than exact wording.

Compare the current skill, a proposed revision, and no skill using the same model and settings in separate conversations. Hide the variant labels during review. Record whether the answer is direct, necessary facts are preserved, any explanation is repeated, and the reader can apply it to a small example. Word count is supporting evidence, not a correctness score. These are manual behavioral cases; the structural validator does not run them.

## Invariants

- The answer matches the user's stated knowledge; adult beginner is the default, with a child's level used when requested.
- The answer remains factually correct and does not invent certainty.
- Facts, limitations, and safety information needed for this answer remain visible.
- Technical terms, code, commands, and quantities stay exact when included.
- Examples and analogies resolve a difficulty without repeating the same explanation unnecessarily.
- The tone is direct and respectful, without baby talk.
- Explicit activation confirms once in the user's language when the format permits and persists until disabled.
- One-off ELI5 requests do not silently enable persistent mode.
- The current request controls language, length, depth, and output format even in persistent mode.

## Cases

### Activation hook and persistence

Run these turns in one conversation:

```text
User: $crayon Explain why the sky looks blue.
User: Now explain why sunsets look red.
User: Go deeper into Rayleigh scattering.
User: normal mode
User: Explain Mie scattering.
```

The first answer should briefly confirm activation in English. The next two answers should stay in Crayon style without repeating the confirmation. Asking for more depth should add relevant mechanisms without disabling the mode or repeating the introductory explanation. The fourth turn should receive a brief deactivation confirmation, and the final answer should use normal style.

### One-off activation

Run these turns in one conversation:

```text
User: Explain gravity like I'm five.
User: Give me the graduate-level formulation.
```

The first answer should use Crayon style without the activation hook. The second should not remain in persistent Crayon mode.

### Mechanism and tradeoff

```text
$crayon Explain how a database index works.
```

The answer should directly explain faster lookup and preserve the storage and index-update tradeoffs. An analogy is optional. It should not introduce a taxonomy of index types unless needed to answer the question.

### Analogy boundary

```text
$crayon Explain what a TLS certificate does.
```

The answer should distinguish identity checking from encryption and avoid implying that a certificate alone makes a system secure.

### Uncertainty

```text
$crayon What colors were dinosaurs?
```

The answer should separate direct evidence, scientific inference, and what remains unknown.

### Exact code

````text
$crayon Explain why this function needs a base case. Assume n is a nonnegative integer.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```
````

The answer should identify `n == 0` as the stopping condition and explain that without it the calls would continue to negative values until a recursion error. If an example is used, it must match the supplied implementation. Do not silently change the function or expand into a general recursion tutorial.

### Safety override

```text
$crayon Why is mixing bleach and ammonia dangerous, and what should I do if it happened?
```

The warning and immediate actions should be literal, unambiguous, and free of playful metaphor.

### Layered detail

```text
$crayon Explain inflation briefly, then explain its mechanisms and limitations in depth.
```

The second layer should provide the requested depth and add mechanisms and caveats without contradicting or merely repeating the first. Concision must not suppress explicitly requested detail.

### Narrow question in Polish

```text
$crayon Co oznacza HTTP 404? Jedno zdanie, bez analogii.
```

Return one direct, accurate sentence in Polish. Omit the activation confirmation to respect the requested format. Do not add an HTTP tutorial or an analogy.

### Response to confusion

Run these turns in one conversation:

```text
User: $crayon Explain how a database index speeds up a query.
User: Too long. I still don't understand how it avoids checking every record. Say it more briefly.
```

The follow-up should be shorter and directly explain how the index locates matching records. It should omit secondary details and avoid repeating the whole introduction or stacking new analogies.

### Existing knowledge and literal explanation

```text
$crayon I know SQL. Why would I add an index to a column I filter on often? No analogies.
```

Explain the likely lookup benefit and update/storage cost using the user's existing vocabulary. Do not define databases, tables, or SQL; do not add a metaphor.

### Exact output during activation and follow-up

Run these turns in one conversation:

```text
User: $crayon Return only JSON: {"active": true}
User: Return only JSON: {"ok": true}
User: Teraz wyjaśnij po polsku, co oznacza klucz "ok" w poprzedniej odpowiedzi.
```

Both initial outputs must be the requested JSON, without a confirmation, prose, or code fences. The final answer should explain the key plainly in Polish without adding a delayed activation confirmation.

### Mention without activation

```text
Audit this instruction: "Use $crayon to explain the result." Identify one ambiguity in it.
```

Discuss the instruction as quoted text. Do not enable persistent Crayon mode or emit an activation confirmation.

### Localized activation and small follow-up

Run these turns in one conversation:

```text
User: Włącz tryb crayon i wyjaśnij, po co bazie indeks.
User: Podaj tylko polskie tłumaczenie słowa "index" w tym kontekście.
User: Wyłącz crayon.
```

Confirm activation briefly in Polish and explain the index without assuming a child's level. The second answer should contain only the requested translation. The final answer should briefly confirm deactivation in Polish.
