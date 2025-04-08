# Web-Agent

A Python-based web automation tool using Playwright that navigates to specified web pages and performs automated tasks.

## Overview

Web-Agent allows you to automate web interactions by navigating directly to desired pages and executing predefined tasks. This project leverages Playwright for Python to enable reliable and powerful browser automation.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/Web-Agent.git
   cd Web-Agent
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv env
   ```

3. **Activate the virtual environment**
   
   On macOS/Linux:
   ```bash
   source env/bin/activate
   ```
   
   On Windows:
   ```bash
   env\Scripts\activate
   ```

4. **Install dependencies**
   
   Option 1: Install all dependencies at once:
   ```bash
   pip install -r requirements.txt
   ```
   
   Option 2: Install Playwright manually:
   ```bash
   pip install pytest-playwright
   playwright install
   ```

## Usage

1. Create test files following the naming convention `test_*.py`
2. Define your web automation tasks within test functions
3. Run tests using pytest:
   ```bash
   pytest -v
   ```

## Example

Here's a simple example that navigates to Claude.ai:

```python
# test_claude.py
import pytest
from playwright.sync_api import Page, expect

def test_open_claude(page: Page):
    """Test to navigate to Claude.ai website and verify it loads correctly."""
    # Navigate to Claude.ai
    page.goto("https://claude.ai/")
    
    # Verify we're on the right page
    expect(page).to_have_title("Claude")
    
    # Optional: Take a screenshot
    page.screenshot(path="claude_home.png")
    
    print("Successfully navigated to Claude.ai")
```
