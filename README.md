# OrderLab

Python CI/CD practice project using Ruff, pytest, FastAPI, and GitHub Actions.

## Features

- Subtotal calculation
- Discount and shipping calculation
- CSV revenue reporting
- FastAPI order creation and retrieval

## Development

Install dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Run lint and format checks:

```bash
ruff check .
ruff format --check .
```

Run tests:

```bash
python -m pytest -q
```

## CI

GitHub Actions automatically checks:

- Ruff lint and formatting
- pytest on Ubuntu
- pytest on Windows
- Test coverage artifact
 
## CI/CD Verification

- Ruff lint and format checks passed.
- pytest tests passed on Ubuntu and Windows.
- Pull requests run CI without deployment.
- GitHub Pages deployment runs after successful CI on main.
- An intentional test failure blocked deployment.
- The failing test was restored after verification.
