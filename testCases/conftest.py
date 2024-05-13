from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver
