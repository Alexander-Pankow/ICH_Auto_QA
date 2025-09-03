import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    #1 Пример не явного универсально ожидания через driver.implicitly_wait(20) 20 секунд
    #1 driver.implicitly_wait(20)
    driver.get("http://www.uitestingplayground.com/ajax")
    yield driver
    driver.quit()

def test_wait_text_after_button_click(driver):
    button = driver.find_element(By.ID, "ajaxButton")
    button.click()
    #2 Пример явного не универсального ожидания wait = WebDriverWait(driver, 20)
    #2 wait = WebDriverWait(driver, 20)
    wait = WebDriverWait(driver, 20)
    #2 result_text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-success")))
    result_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success")))
    #1 result_text = driver.find_element(By.CSS_SELECTOR, ".bg-success")
    assert result_text.text == "Data loaded with AJAX get request."
