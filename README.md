# Python-Based System Validation & Automation Framework

A Python-based test automation framework built using **Pytest** to perform system validation, automated testing, log analysis, and test reporting.

The project simulates device behaviour and validates system-level parameters such as video playback, CPU usage, memory consumption, battery level, application responsiveness, and device temperature.

It also includes automated log analysis and Continuous Integration (CI) using GitHub Actions.

## Project Overview

The objective of this project is to develop a reusable automation framework that can:

- Execute automated test cases using Pytest.
- Validate simulated device and system parameters.
- Support data-driven testing using JSON and CSV test data.
- Manage test setup and teardown using Pytest fixtures.
- Capture execution logs and handle exceptions.
- Parse system logs and identify failures.
- Generate HTML and JUnit XML test reports.
- Execute tests in parallel.
- Automatically execute tests through GitHub Actions.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Automation scripting |
| Pytest | Test execution and framework |
| Pytest-xdist | Parallel test execution |
| Pytest-html | HTML test reporting |
| Pytest-rerunfailures | Retry failed tests |
| Logging | Execution and debugging logs |
| JSON / CSV | Data-driven testing |
| Git & GitHub | Version control |
| GitHub Actions | Continuous Integration |

## Project Structure

```text
Test-automation-Project/
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── logs/
│   └── device_log.txt
│
├── src/
│   ├── __init__.py
│   ├── device_simulator.py
│   ├── logger_config.py
│   └── log_parser.py
│
├── test_data/
│   ├── JSON and CSV test data files
│
├── tests/
│   ├── __init__.py
│   ├── test_video_playback.py
│   ├── test_exception_handling.py
│   └── test_log_parser.py
│
├── conftest.py
├── requirements.txt
├── run_log_analysis.py
└── README.md
```

## Features

### 1. Device Simulation

The framework uses a `DeviceSimulator` class to simulate device behaviour and provide system parameters for validation.

The simulator provides methods to retrieve:

- Video resolution
- Video frame rate (FPS)
- Dropped frames
- Video playback status
- Audio-video synchronization
- Application crash status
- Application responsiveness
- CPU usage
- Memory usage
- Battery level
- Device temperature

These simulated values allow us to develop and test automation logic without requiring a physical Android device.

### 2. Pytest Automation

Pytest is used to organize and execute automated test cases.

The framework includes:

- Test functions and assertions.
- Reusable fixtures.
- Fixture setup and teardown.
- Data-driven testing.
- Parametrized test execution.
- Exception handling.
- Test execution logging.

Run the complete test suite:

```bash
pytest -v
```

### 3. Fixtures and Test Setup

Reusable fixtures are defined in `conftest.py`.

The device fixture initializes the device simulator before test execution and performs cleanup after the tests finish.

This avoids repeated initialization code across multiple test files.

### 4. Data-Driven Testing

JSON and CSV files are used to maintain test inputs separately from the test implementation.

Pytest parametrization allows the same test logic to execute with multiple input values.

This makes it easier to extend test coverage without duplicating test functions.

### 5. Logging and Exception Handling

Python's built-in logging module is used to capture automation execution details.

The framework supports different logging levels:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

Execution logs are generated in:

```text
logs/automation.log
```

Exception handling is implemented to capture and log failures such as device connection errors.

### 6. Log Parsing and Failure Analysis

The framework includes a log parser to analyze device logs and identify potential system failures.

It supports:

- Parsing log entries.
- Identifying INFO, WARNING, and ERROR messages.
- Handling malformed log entries.
- Summarizing detected failures.
- Generating a system validation summary.

Sample device logs are maintained in:

```text
logs/device_log.txt
```

To execute log analysis:

```bash
python run_log_analysis.py
```

The generated summary is saved in:

```text
reports/system_validation_summary.txt
```

### 7. Test Reporting

The framework supports multiple test reporting formats.

**HTML report**

```bash
pytest -v --html=reports/test_report.html --self-contained-html
```

The HTML report provides a readable summary of test execution, including passed and failed tests.

**JUnit XML report**

```bash
pytest -v --junitxml=reports/junit_report.xml
```

JUnit XML reports can be consumed by CI tools for test-result publishing.

### 8. Parallel Test Execution

The framework supports parallel test execution using `pytest-xdist`.

Execute tests using two workers:

```bash
pytest -v -n 2
```

Parallel execution helps reduce test execution time when the tests can safely run independently.

### 9. Automatic Execution Using GitHub Actions

GitHub Actions is integrated to automatically execute the Pytest suite.

The workflow is maintained in:

```text
.github/workflows/python-tests.yml
```

The workflow performs the following operations:

1. Checks out the GitHub repository.
2. Sets up Python 3.12.
3. Installs dependencies from `requirements.txt`.
4. Executes automated tests using two parallel workers.
5. Generates HTML and JUnit XML reports.
6. Uploads the HTML report as a downloadable workflow artifact.
7. Publishes JUnit test results.

**Workflow triggers:**

- Push events to the `main` branch.
- Pull requests targeting the `main` branch.

Test execution results and downloadable reports are available under the **Actions** tab of the GitHub repository.

## Installation and Setup

### Prerequisites

- Python 3.12 or later.
- Git.
- pip.

### Step 1: Clone the repository

```bash
git clone https://github.com/Monalisa0311/Test-automation-project.git
```

Navigate to the project directory:

```bash
cd Test-automation-project
```

### Step 2: Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 3: Execute the test suite

```bash
pytest -v
```

### Step 4: Execute tests in parallel

```bash
pytest -v -n 2
```

### Step 5: Generate test reports

```bash
pytest -v -n 2 --html=reports/test_report.html --self-contained-html --junitxml=reports/junit_report.xml
```

Create the reports directory if it does not already exist.

### Step 6: Execute log analysis

```bash
python run_log_analysis.py
```

## Expected Results

The framework validates simulated device parameters, checks application and playback behaviour, and analyzes sample system logs.

Test execution produces:

- Pytest console output.
- HTML test reports.
- JUnit XML reports.
- Automation execution logs.
- System validation summaries.

## Project Scope

This project currently focuses on Python-based automation, simulated device validation, Pytest, log analysis, test reporting, and GitHub Actions integration.

The device simulator is used for development and validation of the automation framework. Its results should not be interpreted as measurements from actual Android hardware.

## Future Enhancements

Potential extensions include:

- Integration with actual Android devices using ADB.
- Remote Android device testing through cloud platforms.
- Additional system and multimedia validation scenarios.
- Enhanced test analytics and failure diagnostics.

---
