# Repository Guidelines

## Project Structure & Module Organization

This is a small Poetry-managed Python project for real-estate market extraction and analysis.

- `src/`: importable application code. Current extraction logic lives in `src/extract/scraper.py`.
- `notebooks/`: exploratory notebooks and CSV datasets used for analysis.
- `transform/`: reserved for transformation code or outputs; keep generated artifacts separated from source modules.
- `pyproject.toml` and `poetry.lock`: dependency and packaging source of truth.

Keep reusable logic in `src/`. Use notebooks for exploration only; when notebook code becomes operational, move it into a module under `src/`.

## Build, Test, and Development Commands

- `poetry install`: create the virtual environment and install locked dependencies.
- `poetry check`: validate Poetry project metadata.
- `poetry run python -m compileall src`: quick syntax check for source files.
- `poetry build`: build distributable package artifacts.

Example local import check:

```bash
poetry run python -c "from src.extract.scraper import Scraper; print(Scraper)"
```

Network scraping calls depend on the upstream `sub100.com.br` API, so keep small page limits during development.

## Coding Style & Naming Conventions

Use Python 3.13 syntax. Follow PEP 8: 4-space indentation, `snake_case` for functions and variables, `PascalCase` for classes, and uppercase names for constants. Keep module names lowercase.

Prefer typed public methods and small helper methods. Avoid hard-coded output paths inside business logic when a parameter or configuration value would make tests simpler.

## Testing Guidelines

No test suite is currently present. Add tests under `tests/` using `test_*.py` naming. Prefer focused unit tests for URL construction, response parsing, path handling, and error behavior. Mock HTTP calls instead of hitting the live API in tests.

Once `pytest` is added as a development dependency, run:

```bash
poetry run pytest
```

## Commit & Pull Request Guidelines

Git history currently uses short descriptive subjects such as `Initial commit` and `base project, turning to Codex Development`. Keep commits concise, imperative, and scoped, for example `fix scraper CSV save path` or `add extraction parser tests`.

Pull requests should include purpose, key changes, validation commands run, and any data/API assumptions. Include screenshots only for notebook visual changes. Do not commit secrets, local virtual environments, or large generated datasets unless they are intentionally part of the analysis source.

## Security & Configuration Tips

Do not store API keys or credentials in notebooks, CSVs, or source files. Treat upstream API schema changes as expected: validate missing columns and preserve raw response samples only when needed for debugging.
