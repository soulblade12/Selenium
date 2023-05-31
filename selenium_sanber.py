
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID,"user-name").send_keys("standard_user") 
        driver.find_element(By.CSS_SELECTOR,"[data-test='password']").send_keys("secret_sauce") 
        driver.find_element(By.NAME,"login-button").click()
        error_message = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
        self.assertIn("Epic sadface: Password is required",error_message)

    def test_failed_login(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID,"user-name").send_keys("user") 
        driver.find_element(By.NAME,"login-button").click()
        error_message = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
        self.assertIn("Epic sadface: Password is required",error_message)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()