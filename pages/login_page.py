from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="username"]').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()

    def error_text(self):
        error = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]'))
        )
        return error.text