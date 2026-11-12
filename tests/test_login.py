import pytest

from pages.login_page import LoginPage


def test_valid_login_shows_products_page(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    page.wait.until(lambda d: "inventory" in d.current_url)
    assert "inventory" in driver.current_url


def test_wrong_password_shows_error(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "wrong_password")
    assert "do not match" in page.error_text()


@pytest.mark.parametrize(
    "username, password, message",
    [
        ("locked_out_user", "secret_sauce", "locked out"),
        ("standard_user", "", "Password is required"),
        ("", "secret_sauce", "Username is required"),
    ],
)
def test_invalid_logins_are_rejected(driver, username, password, message):
    page = LoginPage(driver)
    page.open()
    page.login(username, password)
    assert message in page.error_text()