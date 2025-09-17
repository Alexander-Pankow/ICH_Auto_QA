from selenium.webdriver.common.by import By

class InventoryPage:
    BACKPACK_ADD = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT_ADD = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_backpack(self):
        self.driver.find_element(*self.BACKPACK_ADD).click()

    def add_tshirt(self):
        self.driver.find_element(*self.TSHIRT_ADD).click()

    def add_onesie(self):
        self.driver.find_element(*self.ONESIE_ADD).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()