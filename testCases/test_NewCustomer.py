import inspect
import time

import pytest

from conftest import setup
from pageObject.NewCustomerPg import NewCustomer
class Test_001_NewCustomer():

    @pytest.mark.regression
    def test_createCustomer_with_validData(self, setup):
        self.driver = setup
        get_current_method = inspect.currentframe().f_code.co_name
        try:
            newCustomer = NewCustomer(self.driver)
            newCustomer.navigateTo_NewCustomer()
            time.sleep(5)
        finally:
            self.driver.quit()

