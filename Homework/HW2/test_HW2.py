"""
Написать скрипт, который:
Открывает в браузере Firefox https://itcareerhub.de/ru
Переходит в раздел “Способы оплаты”
Делает скриншот этой секции страницы
В качестве ответа на задание необходимо приложить ссылку на git репозиторий.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
# получилось решить только с использованием дополнительных методов
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

@pytest.fixture
def driver():
    service = FirefoxService(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    driver_instance = webdriver.Firefox(
        service=service,
        options=options
    )
    yield driver_instance
    driver_instance.quit()

def test_payment_section_screenshot(driver):
    driver.get("https://itcareerhub.de/ru")

    #payment_link = driver.find_element(By.LINK_TEXT, "Способы оплаты") заменил на
    payment_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Способы оплаты"))
    )
    payment_link.click()

    #payment_section = driver.find_element(By.ID, "payment-methods") заменил на
    payment_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//h2[contains(text(), 'Способы оплаты')]/..")
        )
    )

    #Сохраняю скриншот в той же папке, где находится скрипт
    current_dir = os.path.dirname(os.path.abspath(__file__))
    screenshot_path = os.path.join(current_dir, "payment_methods_section.png")
    payment_section.screenshot(screenshot_path)

    payment_section.screenshot("payment_methods_section.png")



