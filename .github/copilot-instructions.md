<!-- Repo-specific instructions for AI coding agents -->
# Copilot instructions — hillel_school

This repository contains standalone Python homework scripts (single-file programs) used for learning exercises. The goal of these instructions is to help an AI coding agent be immediately productive with minimal context.

- Scope: small, independent scripts named using the pattern `Homework_lesson{N}` and `Homework_lesson{N}_t{M}.py` (examples: Homework_lesson5_t1.py, Homework_lesson6_t2.py).
- Language: Python 3 — prefer code that runs on modern CPython (3.8+). A virtualenv `.venv/` is present; use it when executing code.

Key patterns and conventions
- Entry points: each file is a script intended to be executed directly (uses `input()` and `print()`); avoid changing the CLI behavior unless the change is a deliberate refactor that preserves I/O.
- User-facing text is in Ukrainian — preserve prompt wording when modifying behavior or improving validation.
- Minimal modularization: most files do not define functions or classes. Refactors should preserve the original script's external behavior and filename.
- Filenames are the de-facto API: tests or instructors may invoke scripts by filename, so avoid renaming files without explicit consent.

Project-specific guidance for edits
- Safe refactor: extract logic into functions only if you keep a small `if __name__ == '__main__':` wrapper so the script still runs directly.
- Input handling: many scripts read from `input()` and cast to `int` without validation; when improving, add graceful validation and preserve original prompt text.
- Encoding: files use UTF-8. Keep Unicode prompts intact.

How to run (developer workflow)
- Activate the virtual environment (if available):

```bash
source .venv/bin/activate
python Homework_lesson6_t2.py
```

- Alternatively on systems where `python` maps to Python 2, use `python3`.

Files to inspect when making changes
- Example scripts that show common patterns and entry points:
  - Homework_lesson6_t2.py — uses `input()`/`print()` and integer parsing
  - Homework_lesson5_t1.py — simple validation script demonstrating string/int checks

Testing and validation
- There is no test harness in the repo. Quick validation is to run the modified script and exercise typical inputs.
- When refactoring into functions, add a small test scaffold or use simple asserts guarded by `if __name__ == '__main__':`.

Merge/update rules for this file
- If an existing `.github/copilot-instructions.md` is present, preserve any high-value guidance (project-specific commands or CI notes) and merge these repository-specific points under a "Repo-specific guidance" heading.

If anything is unclear (missing CI, env setup, or intended grading commands), ask the repository maintainer for the expected run command and any hidden test harness details.

Quick summary (what to do first)
- Read the target script you will modify. Keep prompts and filenames unchanged. Run the script locally using `.venv` and validate behavior with typical inputs.

---
Please review and tell me which parts need more detail (CI, Python version pinning, or grading commands) and I will iterate.
