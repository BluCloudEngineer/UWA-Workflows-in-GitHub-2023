# UWA Workflows in GitHub - Hands On Lab

## Overview

This GitHub repository deploys a simple Python Flask web application.

## Assumptions

*   You have Python 3.x installed on your local machine.
*   You have PIP3 Python package manager installed on your local machine.
*   You have the Virtual Python Environment builder installed on your local machine.

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
```

Alternatively, you can run the unit tests in the `Testing` extension of Visual Studio Code.
