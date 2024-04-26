from selenium import webdriver

class LoginPage:
    textbox_username_id ="Email"
    textbox_password_id ="Password"
    button_login_xpath ="//input[@class='button-1 login-button']"

    def __init__(self,driver):
        self.driver = driver;

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).sendkeys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).sendkeys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()


