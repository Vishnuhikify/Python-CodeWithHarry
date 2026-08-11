# AI Agent Guidance for Python-CodeWithHarry

## Purpose
This repository is a simple Python learning project with one small script per concept. Use AI assistance to help the user understand Python fundamentals, improve readability, and keep examples beginner-friendly.

## Project structure
- Root contains `README.md` and a `Code-With-Harry/` folder.
- `Code-With-Harry/` holds individual Python lesson files such as `01_Hello.py`, `02_Variables.py`, `03_Typecasting.py`, etc.
- Each file is a standalone script demonstrating a single Python concept.

## How to run
```bash
python Code-With-Harry/<filename>.py
```

## Recommended agent behavior
- Keep changes minimal and concept-focused.
- Preserve the single-topic lesson style; avoid merging unrelated concepts into one file.
- Prefer clear beginner-friendly Python code and concise explanations.
- Do not introduce complex project structure changes unless the user explicitly asks for a larger refactor.
- If asked to add examples or exercises, keep them simple and consistent with the existing file naming style.

## When assisting
- Use plain language and educational examples when explaining code.
- Fix syntax issues, runtime errors, and inconsistent naming with beginner clarity in mind.
- Recommend `python filename.py` for running the lessons.
- Avoid adding unnecessary dependencies or external tooling.

## Notes
- There is no formal build system or test suite; the repository is intended for learning and practice.
- Keep instructions focused on code edits, explanations, and small improvements.
