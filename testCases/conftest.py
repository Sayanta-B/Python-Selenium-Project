from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    # driver = webdriver.Remote(
    #     command_executor='http://localhost:4444/wd/hub',
    #     options=options
    # )
    driver = webdriver.Chrome()
    return driver
