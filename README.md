# Selenium and pytest Framework

![Selenium Tests](https://github.com/Shahzaib-A-Khan/selenium-pytest-framework/actions/workflows/selenium-tests.yml/badge.svg)

Selenium WebDriver tests in Python, run with pytest, for the saucedemo.com login page. A page object holds the locators and actions, and a pytest fixture gives every test a fresh headless Chrome browser.

## What it shows
- A page object (`pages/login_page.py`) with an explicit wait for the error message
- A pytest fixture in `conftest.py` that starts and quits a browser around every test
- `@pytest.mark.parametrize` to run one test against several rows of data
- A self-contained HTML report, with a screenshot saved for every failed test
- CI in GitHub Actions on pushes, pull requests and nightly, uploading the report as an artifact

## Run it
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest

The HTML report is written to reports/report.html, and failure screenshots go to reports/screenshots/.

## Notes
- Selenium does not wait for elements automatically the way Playwright does, so the page object uses an explicit wait (WebDriverWait) for elements that appear after an action.
- The target is saucedemo.com, a public practice site.
- Versions are pinned in requirements.txt.

## Project structure
- pages/: page objects
- tests/: test files
- conftest.py: the browser fixture and the failure screenshot hook
- pytest.ini: pytest settings, including the report options
- .github/workflows/selenium-tests.yml: CI workflow