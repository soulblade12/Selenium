
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class TestCheckout(unittest.TestCase): #test Case 3

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_checkout(self): 
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID,"user-name").send_keys("standard_user") 
        driver.find_element(By.CSS_SELECTOR,"[data-test='password']").send_keys("secret_sauce") 
        driver.find_element(By.NAME,"login-button").click()
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID,"shopping_cart_container").click()
        driver.find_element(By.ID,"checkout").click()
        driver.find_element(By.ID,"first-name").send_keys("irfan") 
        driver.find_element(By.ID,"last-name").send_keys("Adi") 
        driver.find_element(By.ID,"postal-code").send_keys("55262") 
        driver.find_element(By.ID,"continue").click()
        driver.find_element(By.ID,"finish").click()

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()