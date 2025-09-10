"""
Задание 1: Проверка изменения текста кнопки
Тестируемый сайт:
http://uitestingplayground.com/textinput
Шаги теста:
Перейдите на сайт Text Input.
Введите в поле ввода текст "ITCH".
Нажмите на синюю кнопку.
Проверьте, что текст кнопки изменился на "ITCH".
"""

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
    driver.get("http://uitestingplayground.com/textinput")
    yield driver
    driver.quit()

def test_text_itch(driver):
    itch_input = driver.find_element(By.CSS_SELECTOR, ".form-control")
    itch_input .send_keys("ITCH")
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    blue_button.click()
    change_itch = driver.find_element(By.XPATH, "//*[text()='ITCH']")
    assert  change_itch.text == "ITCH"

"""
Задание 2: Проверка загрузки изображений
Тестируемый сайт:
https://bonigarcia.dev/selenium-webdriver-java/loading-images.html
Шаги теста:
Перейдите на сайт Loading Images.
Дождитесь загрузки всех изображений.
Получите значение атрибута alt у третьего изображения.
Убедитесь, что значение атрибута alt равно "award".
"""

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    yield driver
    driver.quit()

def test_attribute_alt_award(driver):
    wait = WebDriverWait(driver, 15)
    third_image = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#image-container img:nth-of-type(3)")))
    third_image_alt = third_image.get_attribute("alt")
    assert third_image_alt == "award"