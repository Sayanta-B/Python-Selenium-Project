class BaseClass:
    def __init__(self, raise_exception = True):
        self.raise_exception = raise_exception

    def handle_timeout_exception(self, element, t_exception):
        if self.raise_exception:
            raise TimeoutError("Element not found")
        else:
            # Ignore the error and continue the flow.
            pass

    def click_on(self, element):
        try:
            element.click()
        except TimeoutError as te:
            self.handle_timeout_exception(element, te)
        except Exception as ex:
            print(ex)
