# Contributing

Crayon should stay small, precise, and easy to inspect.

## Before proposing a change

1. Identify a real explanation failure that the current instructions produce.
2. Prefer the smallest instruction change that corrects that failure.
3. Add or adjust a case in `evals/cases.md` when behavior changes.
4. Run both validators:

   ```bash
   python3 scripts/validate_skill.py .
   python3 /path/to/skill-creator/scripts/quick_validate.py .
   ```

Do not add universal rules for speculative edge cases. Keep examples only when they clarify an important boundary: accuracy, uncertainty, analogy limits, exact syntax, or safety.

## Pull requests

Explain the observed problem, the narrow change, and how you checked the result. Avoid unrelated formatting or repository changes.
