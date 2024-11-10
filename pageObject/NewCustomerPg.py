from selenium import webdriver
from selenium.webdriver.common.by import By

from ui_driver import BaseClass


class NewCustomer(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    @property
    def _NewCustomer(self):
        return self.driver.find_element(By.XPATH, "//a[text() ='New Customer']")

    @property
    def _customeName_textbox(self):
        return self.driver.find_element(By.XPATH, "//input[@name='name']")

    @property
    def _gender_male_radioButton(self):
        return self.driver.find_element(By.XPATH, "//input[@value='m']")

    @property
    def _gender_female_radioButton(self):
        return self.driver.find_element(By.XPATH, "//input[@value='f']")
    @property
    def _DOB_callender(self):
        return self.driver.find_element(By.NAME, "uid")

    @property
    def _address_textBox(self):
        return self.driver.find_element(By.XPATH, "//textarea[@name='addr']")

    @property
    def _city_textfield(self):
        return self.driver.find_element(By.XPATH, "//input[@name='city']")
    @property
    def _state_textfield(self):
        return self.driver.find_element(By.XPATH, "//input[@name='state']")
    @property
    def _pin_textfield(self):
        return self.driver.find_element(By.XPATH, "//input[@name='pinno']")
    @property
    def _mobileNumber_textfield(self):
        return self.driver.find_element(By.XPATH, "//input[@name='telephoneno']")
    @property
    def _email_textfield(self):
        return self.driver.find_element(By.XPATH, "//input[@name='emailid']")
    @property
    def _password_textfield(self):
        return self.driver.find_element(By.XPATH, "//input[@name='password']")
    @property
    def _submit_button(self):
        return self.driver.find_element(By.XPATH, "//input[@name='sub']")



    def navigateTo_NewCustomer(self):
        newCustomer = self._NewCustomer
        self.click_on(newCustomer)
