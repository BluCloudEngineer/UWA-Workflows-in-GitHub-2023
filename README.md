# UWA Workflows in GitHub - Hands On Lab

![GitHub Contributors](https://img.shields.io/github/contributors-anon/BluCloudEngineer/UWA-Workflows-in-GitHub-2023)
![GitHub Downloads](https://img.shields.io/github/downloads/BluCloudEngineer/UWA-Workflows-in-GitHub-2023/total)
![GitHub Forks](https://img.shields.io/github/forks/BluCloudEngineer/UWA-Workflows-in-GitHub-2023)
![GitHub Issues](https://img.shields.io/github/issues/BluCloudEngineer/UWA-Workflows-in-GitHub-2023)
![GitHub Last Commit](https://img.shields.io/github/last-commit/BluCloudEngineer/UWA-Workflows-in-GitHub-2023)
![GitHub License](https://img.shields.io/github/license/BluCloudEngineer/UWA-Workflows-in-GitHub-2023)
![GitHub Open Issues](https://img.shields.io/github/issues-raw/BluCloudEngineer/UWA-Workflows-in-GitHub-2023)
![GitHub Open Pull Requests](https://img.shields.io/github/issues-pr-raw/BluCloudEngineer/UWA-Workflows-in-GitHub-2023)
![GitHub Python Version](https://img.shields.io/badge/python%20version-3.10.12-blue)
![GitHub Repository Size](https://img.shields.io/github/repo-size/BluCloudEngineer/UWA-Workflows-in-GitHub-2023)
![GitHub Stars](https://img.shields.io/github/stars/BluCloudEngineer/UWA-Workflows-in-GitHub-2023)
![GitHub Weekly Commit Activity](https://img.shields.io/github/commit-activity/w/BluCloudEngineer/UWA-Workflows-in-GitHub-2023)

## Overview

This GitHub repository deploys a simple Python Flask web application.

## Assumptions

* You have Python 3.x installed on your local machine.
* You have PIP3 Python package manager installed on your local machine.
* You have the Virtual Python Environment builder installed on your local machine.

## Setting Up Your Development Environment

1.  Create a new Python virtual environment:

    ```bash
    python3 -m venv .venv
    ```

2.  Activate the virtual environment:

    ```bash
    source .venv/bin/activate
    ```

3.  Install the required Python dependencies:

    ```bash
    pip3 install -r requirements.txt
    ```

## Usage

After creating and configuring your virtual environment, run the following command to start the Python Flask web application:

```bash
python3 application.py
```

Next, open a web browser and navigate to:

```text
http://127.0.0.1:5000
```

## Unit Tests

After creating and configuring your virtual environment, run the following command to run the unit tests:

```bash
pytest
# OR
pytest --junitxml=tests/report.xml
```

Alternatively, you can run the unit tests in the `Testing` extension of Visual Studio Code.
