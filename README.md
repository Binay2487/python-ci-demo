# Python CI Demo

Demo Python project to demonstrate GitHub Actions: build, test (pytest), lint (flake8), and optional publish to PyPI.

## Quick start (local)
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
# create repo on GitHub and add remote, then:
git remote add origin git@github.com:<OWNER>/<REPO>.git
git push -u origin main
```

## What runs in CI
- Install dependencies from `requirements.txt`
- Run `pytest`
- Run `flake8`
- Optional: publish to PyPI when pushing to `main` and `PYPI_API_TOKEN` secret is set

## Files of interest
- `.github/workflows/ci-demo-python.yml` — the workflow
- `src/hello.py` — sample source
- `tests/test_hello.py` — sample test
- `requirements.txt` — test/lint deps
