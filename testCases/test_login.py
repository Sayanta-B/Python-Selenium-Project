import os
import time

import pytest
from selenium import webdriver
from pageObject.LoginPage import LoginPage
from utilities.readProperties import  ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.logger.info("**************** Opening the URL *****************")
        self.driver.get(self.baseURL)
        accutualTitle= self.driver.title
        self.driver.maximize_window()
        # time.sleep(5)

        if accutualTitle == "Your store. Login":
            self.logger.info("**************** Closing the Browser *****************")
            self.driver.close()
            assert True
        else:
            # Get the current working directory
            current_directory = os.getcwd()
            # Construct the file path for saving the screenshot
            screenshot_path = os.path.join(current_directory, "Screenshots")
            print(f"this is sc path __________>>", screenshot_path)
            self.driver.save_screenshot(screenshot_path, "test_homePageTitle.png")
            self.driver.close()
            assert False
    def test_loginTest(self,setup):
        self.driver = setup
        self.logger.info("**************** Opening the URL *****************")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        accutualTitle = self.driver.title
        if accutualTitle == "Dashboard / nopCommerce administration":
            self.logger.info("**************** Closing the Browser *****************")
            self.driver.quit()
            assert True
        else:
            assert False
        self.driver.quit()

