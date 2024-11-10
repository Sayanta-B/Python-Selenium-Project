from selenium import webdriver
from selenium.webdriver.common.by import By

from ui_driver import BaseClass


class LoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    @property
    def _textbox_username_name(self):
        return self.driver.find_element(By.NAME, "uid")

    @property
    def _textbox_password_name(self):
        return self.driver.find_element(By.NAME, "password")

    @property
    def _loginButton(self):
        return self.driver.find_element(By.NAME, "btnLogin")

    def setUserName(self,username):
        userNameBox = self._textbox_username_name
        userNameBox.clear()
        userNameBox.send_keys(username)


    def setPassword(self, password):
        passwordField = self._textbox_password_name
        passwordField.clear()
        passwordField.send_keys(password)


    def clickLogin(self):
        button = self._loginButton
        self.click_on(button)
