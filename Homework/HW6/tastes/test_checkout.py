import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Homework.HW6.pages.login_page import LoginPage
from Homework.HW6.pages.inventory_page import InventoryPage
from Homework.HW6.pages.cart_page import CartPage
from Homework.HW6.pages.checkout_page import CheckoutPage
from Homework.HW6.pages.checkout_overview_page import CheckoutOverviewPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_checkout_total(driver):
    # 1. Login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # 2. Add products
    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack()
    inventory_page.add_tshirt()
    inventory_page.add_onesie()
    inventory_page.go_to_cart()

    # 3. Go to checkout
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # 4. Fill checkout form
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("John", "Doe", "12345")

    # 5. Get total price
    checkout_overview = CheckoutOverviewPage(driver)
    total_text = checkout_overview.get_total()

    # 6. Assert total
    assert "$58.29" in total_text