import os

class TakeScreenshot:

    def __init__(self, setup):
        self.driver = setup

    def takeScreenshot(self, methodName):
        current_directory = os.getcwd()
        # Navigate up two levels to reach the parent directory and then to the Screenshots folder
        relative_screenshot_directory = os.path.join(current_directory, "..", "Screenshots")
        screenshot_directory = os.path.abspath(relative_screenshot_directory)
        print(screenshot_directory)
        screenshot_path = os.path.join(screenshot_directory, f"{methodName}.png")
        self.driver.save_screenshot(screenshot_path)