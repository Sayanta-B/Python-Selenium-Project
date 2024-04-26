
import pytest
from selenium import webdriver
from pageObject.LoginPage import LoginPage

class Test_001_Login:
    baseURL="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username ="admin@yourstore.com"
    password="admin"

    def test_homePageTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        accutualTitle= self.driver.title
        self.driver.close()
        if accutualTitle == "Your store. Login":
            assert True
        else:
            assert False
    def test_loginTest(self):
        pass

