# Changelog

## 0.4.0

- CI/CD & DevOps:
  - New GitHub Actions workflow template for Python projects (`.github/workflows/ci.yml`)
  - Optional generation via wizard flags
- Tooling:
  - `pre-commit` support with Black, isort, Flake8, MyPy
  - Optional Poetry `pyproject.toml` template
- CLI & API:
  - Wizard flags: `--ci`, `--pre-commit`, `--package-manager {pip|poetry}`
  - `scaffold_project` extended with `include_ci`, `include_pre_commit`, `package_manager`
- Docs:
  - README updated with 0.4.0 features and visuals

## 0.3.0

- CLI:
  - New `devboiler new` interactive wizard (framework, DB, Docker, tests, linters)
- API:
  - Added `scaffold_project` high-level generator
- Templates:
  - Docker: `Dockerfile` and `docker-compose.yml` for Python and Node/Express
  - Tests: pytest samples for FastAPI, Flask, Python
  - Linters: basic `.flake8`
- Docs:
  - README updated with wizard examples and `scaffold_project`

## 0.2.0

- Features:
  - Added new boilerplates: Flask app, FastAPI app, Node.js script, Express.js app, Python CLI (argparse), React component with CSS module
  - Added `devboiler list` command to display available boilerplates
  - Enhanced CLI help with examples and epilog
- Docs:
  - Rewrote README to English with full CLI/API examples
- Packaging:
  - Included templates in wheel and sdist
  - Published to PyPI as `devboiler` 0.2.0

## 0.1.0

- Initial release: Python class, HTML page, React component, Python project skeleton, CLI entrypoint
