# Sensor report cleanup

This repository contains a small utility used by a research group to summarize temperature readings from laboratory sensors. The program works, but its style has not yet been brought in line with the project's automated checks.

Your job is to use Ruff to format and lint the code, verify that its behavior has not changed, and commit the cleaned-up version.

## Set up

Create or activate a Python environment, then install the development tools:

```bash
python -m pip install -r requirements-dev.txt
```

## Establish the baseline

Run the program and its tests before changing anything:

```bash
python sensor_report.py
python -m pytest
```

Both commands should succeed. Now ask Ruff to report the current problems:

```bash
python -m ruff format --check .
python -m ruff check .
```

Read the output. Notice that the formatter and linter report different kinds of problems.

## Clean up the project

Let Ruff format the Python files:

```bash
python -m ruff format .
```

Apply Ruff's safe lint fixes:

```bash
python -m ruff check --fix .
```

Inspect what changed:

```bash
git diff
```

## Verify and submit

Run the same checks used by the autograder:

```bash
python -m ruff format --check .
python -m ruff check .
python -m pytest
```

Also run the program once more and compare its output with the baseline. Then commit and submit your work:

```bash
git status
git add sensor_report.py
git commit -m "Apply Ruff formatting and lint fixes"
gh student submit
```

## Add pre-commit

After the Ruff checks pass, make them run automatically before future commits. Create `.pre-commit-config.yaml` with the following content:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.16.2
    hooks:
      - id: ruff-check
        args: [--fix, --show-fixes]
      - id: ruff-format
```

Enable and exercise the hooks:

```bash
pre-commit install
pre-commit run --all-files
git add .pre-commit-config.yaml
git commit -m "Run Ruff with pre-commit"
```

The hook installation lives inside `.git/` and is local to your clone. The YAML configuration is committed so every contributor can install the same hooks.
