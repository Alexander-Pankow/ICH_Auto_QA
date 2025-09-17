from selenium.webdriver.common.by import By

class CheckoutPage:
    FIRSTNAME_INPUT = (By.ID, "first-name")
    LASTNAME_INPUT = (By.ID, "last-name")
    ZIP_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name: str, last_name: str, zip_code: str):
        self.driver.find_element(*self.FIRSTNAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LASTNAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.ZIP_INPUT).send_keys(zip_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()