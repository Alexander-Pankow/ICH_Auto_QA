import pytest
import math
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from typing_extensions import assert_type
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.maximize_window()
#     driver.get("http://suninjuly.github.io/huge_form.html")
#     yield driver
#     driver.quit()
#
#
# def test_alert_text(driver):
#     input_fields = driver.find_elements(By.CSS_SELECTOR, "[type='text']")
#     for field in input_fields:
#         field.send_keys("Hello")
#     submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
#     submit_button.click()
#     #sleep(20)
#     wait = WebDriverWait(driver, 10)
#     alert = wait.until(EC.alert_is_present())
#     #alert = driver.switch_to.alert
#     assert "Congrats, you've passed the task!" in alert.text


# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.maximize_window()
#     driver.get("https://suninjuly.github.io/math.html")
#     yield driver
#     driver.quit()
#
# def math_calc(x):
#     return math.log(abs(12 * math.sin(x)))
#
# def test_math_calc(driver):
#     x_value = driver.find_element(By.ID, "input_value").text
#     result = math_calc(int(x_value))
#     answer_input = driver.find_element(By.ID, "answer")
#     answer_input.send_keys(str(result))
#     check_box = driver.find_element(By.CSS_SELECTOR, "[type='checkbox']")
#     check_box.click()
#     radio_box = driver.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
#     radio_box.click()
#     submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
#     submit_button.click()
#     wait = WebDriverWait(driver,20)
#     alert = wait.until(EC.alert_is_present())
#     assert "Congrats, you've passed the task!" in alert.text



# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.maximize_window()
#     driver.get("http://suninjuly.github.io/get_attribute.html")
#     yield driver
#     driver.quit()
#
# def math_calc(x):
#         return math.log(abs(12 * math.sin(x)))
#
# def test_get_attr(driver):
#     x_value = driver.find_element(By.ID, "treasure").get_attribute("valuex")
#     result = math_calc(int(x_value))
#     answer_input = driver.find_element(By.ID, "answer")
#     answer_input.send_keys(str(result))
#     check_box = driver.find_element(By.CSS_SELECTOR, "[type='checkbox']")
#     check_box.click()
#     radio_box = driver.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
#     radio_box.click()
#     submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
#     submit_button.click()
#     wait = WebDriverWait(driver, 20)
#     alert = wait.until(EC.alert_is_present())
#     assert "Congrats, you've passed the task!" in alert.text


# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.maximize_window()
#     driver.get("https://suninjuly.github.io/redirect_accept.html")
#     yield driver
#     driver.quit()
#
# def math_calc(x):
#         return math.log(abs(12 * math.sin(x)))
#
#
# def test_switch_alert(driver):
#     button = driver.find_element(By.TAG_NAME, "button")
#     button.click()
#     tabs_ids = driver.window_handles
#     print(tabs_ids)
#     driver.switch_to.window(tabs_ids[1])
#
#     x_value = driver.find_element(By.ID, "input_value").text
#     result = math_calc(int(x_value))
#     answer_input = driver.find_element(By.ID, "answer")
#     answer_input.send_keys(str(result))
#     submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
#     submit_button.click()
#
#     wait = WebDriverWait(driver, 10)
#     alert = wait.until(EC.alert_is_present())
#     assert "Congrats, you've passed the task!" in alert.text


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://crossbrowsertesting.github.io/hover-menu.html")
    yield driver
    driver.quit()

def test_hover(driver):
    dropdown = driver.find_element(By.XPATH, "(//a[@class = 'dropdown-toggle'])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(dropdown).perform()
    secondary_menu = driver.find_element(By.LINK_TEXT, "Secondary Menu")
    actions.move_to_element(secondary_menu).perform()
    secondary_action = driver.find_element(By.LINK_TEXT, "Secondary Action")
    secondary_action.click()
    header = driver.find_element(By.XPATH, "(//h1)[2]")
    assert header.text == "Secondary Page"