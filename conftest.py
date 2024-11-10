from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from pageObject.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


@pytest.fixture()
def setup():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    # driver = webdriver.Remote(
    #     command_executor='http://localhost:4444/wd/hub',
    #     options=options
    # )
    driver = webdriver.Chrome()
    logger.info("**************** Opening the URL *****************")
    driver.get(baseURL)
    lp = LoginPage(driver)
    lp.setUserName(username)
    lp.setPassword(password)
    lp.clickLogin()
    return driver

