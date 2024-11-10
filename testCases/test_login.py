import inspect

from pageObject.LoginPage import LoginPage
from utilities.TakeScreenshot import TakeScreenshot
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    def test_homePageTitle(self, setup):
        self.driver = setup
        get_current_method = inspect.currentframe().f_code.co_name
        self.logger.info("**************** Opening the URL *****************")
        self.driver.get(self.baseURL)
        accutualTitle = self.driver.title.strip()
        self.driver.maximize_window()
        try:
            if accutualTitle == "Guru99 Bank Home Page":
                self.logger.info("**************** Closing the Browser *****************")
                assert True
            else:
                sc = TakeScreenshot(self.driver)
                sc.takeScreenshot(get_current_method)
                assert False
        finally:
            self.driver.quit()

    def test_loginTest(self, setup):
        self.driver = setup
        self.logger.info("**************** Opening the URL *****************")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        accutualTitle = self.driver.title
        try:
            if accutualTitle == "Guru99 Bank Manager HomePage":
                self.logger.info("**************** Closing the Browser *****************")

                assert True
            else:
                assert False
        finally:
            self.driver.quit()