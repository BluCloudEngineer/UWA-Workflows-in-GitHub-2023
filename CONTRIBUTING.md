# How to Contribute

Thank you for your interest in this repository! Contributions are always welcome, whether you are working solo or as a team (preferred).

## Table of Contents

- [How to Contribute](#how-to-contribute)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [Submitting Changes](#submitting-changes)
    - [Desired Changes](#desired-changes)
    - [Additional Features](#additional-features)
    - [Pull Request Process](#pull-request-process)
  - [Standards and Conventions](#standards-and-conventions)
    - [Coding](#coding)
    - [Git Branching](#git-branching)
  - [Running Unit Tests](#running-unit-tests)
  - [CI / CD Pipeline Overview](#ci--cd-pipeline-overview)
  - [Reporting Bugs and Requesting Features](#reporting-bugs-and-requesting-features)
  - [Questions](#questions)

---

## Getting Started

Before making any changes, set up your local development environment by following the steps in the [README.md](README.md) file.

In summary:

1. Create and activate a Python virtual environment:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2. Install all required dependencies:

    ```bash
    pip3 install -r requirements.txt
    ```

---

## Submitting Changes

### Desired Changes

1. Check the [Issues](https://github.com/BluCloudEngineer/UWA-Workflows-in-GitHub-2023/issues) page and pick an issue to work on.
2. Prioritise these issues before working on anything else.

### Additional Features

If there are no open issues to address, or you want to add something new, feel free to open a pull request for review.

### Pull Request Process

1. Create a new branch off the `main` branch following the [branch naming conventions](#git-branching) below.
2. Make your changes and ensure all unit tests pass locally (see [Running Unit Tests](#running-unit-tests)).
3. Open a pull request against the `main` branch. The [pull request template](.github/pull_request_template.md) will load automatically — complete every item in the checklist.
4. Link any related GitHub issues in your pull request (e.g. `Closes #10`).
5. Your pull request will be reviewed before it is merged.

The pull request checklist covers the following key points:

- Your changes are on a correctly named branch.
- Your code follows the project's style guidelines.
- You have run all linting and formatting scripts.
- You have added comments to your code where applicable.
- You have updated relevant documentation (e.g. `README.md`).
- You have added working unit tests for any new features.
- All existing unit tests pass.
- You have not committed any secrets or sensitive information.
- You have linked all related GitHub issues.

---

## Standards and Conventions

### Coding

- All Python code must follow the [PEP 8](https://peps.python.org/pep-0008/) coding standard.
- An automated PEP 8 linting workflow (`autopep8`) runs on every push to `main`. If your code does not conform, an automated pull request will be raised on the `refactor/python-formatting-linting` branch to fix the formatting. Review and merge this PR promptly to keep `main` clean.
- There is no local linting configuration file (`.flake8`, `setup.cfg`, etc.) — compliance is enforced entirely through the GitHub Actions workflow.

### Git Branching

- Do **not** commit directly to the `main` branch.
- Create a new branch for every piece of work, following the [Conventional Branch](https://conventionalbranch.org/) naming standard.

Use the following prefixes to name your branch:

| Prefix           | When to use                                           |
| ---------------- | ----------------------------------------------------- |
| `feature/`       | Adding new functionality                              |
| `bugfix/`        | Fixing a reported bug                                 |
| `hotfix/`        | Emergency fix for a production issue                  |
| `refactor/`      | Code improvements with no new features                |
| `documentation/` | Documentation only changes                            |
| `security/`      | Addressing a security vulnerability / vulnerabilities |

Examples:

```text
feature/add-division-operation
bugfix/fix-hexadecimal-conversion
documentation/update-readme
```

---

## Running Unit Tests

Unit tests are located in the `tests/` directory and use [pytest](https://docs.pytest.org/).

Run all tests locally with:

```bash
pytest
```

To generate a JUnit XML report (as used by [AWS CodeBuild](https://aws.amazon.com/codebuild/)):

```bash
pytest --junitxml=tests/report.xml
```

Tests are also run automatically by GitHub Actions:

- On every **pull request** to `main` — via the `Run PyTest Unit Tests` workflow.
- On every **push to `main`** — via the `Run pytest Unit Tests, build Docker Container and push to Docker Hub` workflow.

All tests must pass before a pull request can be merged.

---

## CI / CD Pipeline Overview

This project uses GitHub Actions for CI / CD. Understanding the automated workflows helps you know what to expect after you push code or open a pull request.

| Workflow                                                               | Trigger                | What it does                                                                                                                         |
| ---------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `Run PyTest Unit Tests`                                                | Pull request to `main` | Runs all pytest unit tests                                                                                                           |
| `Run Python PEP8 Linting`                                              | Push to `main`         | Runs `autopep8` and opens an automated PR if formatting fixes are needed; also runs unit tests                                       |
| `Run pytest Unit Tests, build Docker Container and push to Docker Hub` | Push to `main`         | Runs unit tests, then builds and pushes the Docker image to [Docker Hub](https://hub.docker.com/r/blucloudengineer/uwaworkflows2023) |

---

## Reporting Bugs and Requesting Features

Use the GitHub issue templates to report bugs or request features. Templates load automatically when you create a new issue.

- **Bug report** — Use this template to report unexpected behaviour. Provide your OS, browser, steps to reproduce and what you expected vs what actually happened.
- **Feature request** — Use this template to suggest new ideas. Describe what you want to add and why it would benefit the project.

Before submitting, check existing [Issues](https://github.com/BluCloudEngineer/UWA-Workflows-in-GitHub-2023/issues) to avoid duplicates. If your bug or feature has already been reported, add a comment to the existing issue rather than opening a new one.

---

## Questions

If you need help, clarification, or guidance at any point, don't hesitate to open a [GitHub issue](https://github.com/BluCloudEngineer/UWA-Workflows-in-GitHub-2023/issues) or leave a comment on the relevant issue or pull request.
