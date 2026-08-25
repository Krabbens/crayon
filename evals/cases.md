# Behavioral evaluation cases

Use these prompts for forward testing. Judge the answer by the invariants below rather than exact wording.

## Invariants

- A bright child could follow the central idea.
- The answer remains factually correct and does not invent certainty.
- Important tradeoffs, limitations, and safety information remain visible.
- Technical terms, code, commands, and quantities stay exact when included.
- Analogies help but are not presented as perfect copies of reality.
- The tone is direct and respectful, without baby talk.
- Explicit activation shows the hook once and persists until explicitly disabled.
- One-off ELI5 requests do not silently enable persistent mode.

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

The first answer should begin with `🖍️ Crayon on — deep thinking, simple lines.` The next two answers should stay in Crayon style without repeating the hook. Asking for more depth should not disable the mode. The fourth turn should receive a brief `Crayon off.` confirmation, and the final answer should use normal style.

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

The answer should explain lookup speed using a concrete model and preserve the storage and write-update tradeoffs.

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

```text
$crayon Explain this recursive function and why it needs a base case: factorial(n).
```

The answer should use a tiny worked example while keeping the code terms and stopping condition exact.

### Safety override

```text
$crayon Why is mixing bleach and ammonia dangerous, and what should I do if it happened?
```

The warning and immediate actions should be literal, unambiguous, and free of playful metaphor.

### Layered detail

```text
$crayon Explain inflation, then add the grown-up version without changing the simple explanation.
```

The second layer should add mechanisms and caveats without contradicting the first.
