from selenium.webdriver.common.by import By

class CheckoutOverviewPage:
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver

    def get_total(self) -> str:
        return self.driver.find_element(*self.TOTAL_LABEL).text