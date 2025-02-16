# Automation Testing Framework

## Overview

This framework is designed using the **Page Object Model (POM)** design pattern, leveraging **Pytest, Selenium and Appium** to automate testing across multiple platforms, including **Web, iOS, and Mac**.

## Features

- Supports **cross-platform testing** (Web, iOS, Mac)
- Implements **explicit waits** for stable element interactions
- Supports **soft assertions** for non-blocking test validation
- **Headless execution** support for faster test execution
- Generates **detailed logs and reports** using **Allure report**
- Modular and scalable test structure following **POM design pattern**

## Installation

Clone the repository:

```bash
git clone https://github.com/uyenho-0607/pytest_selenium.git
```

## Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

## Install Dependencies

```bash
pip3 install -r requirements.txt
```

## Configuration

Stored at `config/*.yaml` file

## Running Tests

### **Run Sample Test Suite (Default: Web)**
```bash
pytest tests/web/channels_page
```

### **Run Tests on Different Platforms**
You can specify the platform using the `--platform` option:

- **Web:** (default)
  ```bash
  pytest tests/web/channels_page
  ```
- **Mac:**
  ```bash
  pytest tests/mac/channels_page --platform=mac
  ```
- **iOS:**
  ```bash
  pytest tests/ios/channels_page --platform=ios
  ```

### **Run All Tests**
```bash
pytest tests/ --platform=web  # or mac, ios
```

### **Run in Headless Mode**
```bash
pytest --headless ...
```

## Project Structure
Complete sample structure is designed for **Channels** page -> Please refer to src/pages/web/channels_page.py
