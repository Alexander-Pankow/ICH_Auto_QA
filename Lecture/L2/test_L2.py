from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest

# делаем скрин хром

# # Setup ChromeDriver / Настройка ChromeDriver
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# # Open first site / Открытие первого сайта
# driver.get("https://itcareerhub.de/ru")
#
# # Open second site / Открытие второго сайта
# driver.get("https://www.berlin.de")
#
# # Save screenshot / Сохранение скриншота
# driver.save_screenshot("./berlin_screenshot.png")
#
# # Wait 3 seconds / Ждём 3 секунды
# sleep(3)
#
# # Close browser / Закрытие браузера
# driver.quit()


# для фокса тоже самое

# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
# # Настройка драйвера для Firefox с использованием WebDriverManager
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# driver.get("https://itcareerhub.de/ru")
#
# driver.get("https://www.berlin.de")
# driver.save_screenshot("./berlin_screenshot.png")
#
# sleep(3)
# driver.quit()


# ищем текст на сайте хром

# Setup ChromeDriver / Настройка ChromeDriver
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# # Open first site / Открытие первого сайта
# driver.get("https://itcareerhub.de/ru")
#
# about_link = driver.find_element(By.LINK_TEXT, "О нас")
# about_link.click()
#
# sleep(3)

# ищем текст на сайте хром c фикстурой

@pytest.fixture
def driver():
    # Setup WebDriver / Инициализация WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    # Teardown / Закрытие браузера
    driver.quit()


def test_open_about_page(driver):
    # Open site / Открытие сайта
    driver.get("https://itcareerhub.de/ru")

    # Find "О нас" link / Поиск ссылки "О нас"
    about_link = driver.find_element(By.LINK_TEXT, "О нас")
    about_link.click()

    # Wait a bit to see result / Пауза для наглядности
    sleep(3)

    # Проверяем, что заголовок страницы содержит "О нас"
    assert "О нас" in driver.title