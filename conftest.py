import os
import re

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)


@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=options)
    yield driver
    failed = hasattr(request.node, "rep_call") and request.node.rep_call.failed
    if failed:
        os.makedirs("reports/screenshots", exist_ok=True)
        name = re.sub(r"[^A-Za-z0-9_.-]", "_", request.node.name)
        driver.save_screenshot(f"reports/screenshots/{name}.png")
    driver.quit()