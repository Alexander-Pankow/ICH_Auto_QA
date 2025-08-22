
#без фикстуры

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def test_home_page_title():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://itcareerhub.de/ru")
    sleep(2)

    assert "IT CAREER HUB" in driver.title

    driver.quit()


def test_about_page_title():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://itcareerhub.de/ru")
    about_link = driver.find_element(By.LINK_TEXT, "О нас")
    about_link.click()
    sleep(2)

    assert "О нас" in driver.title

    driver.quit()

#👉 Минус: одинаковый блок с driver = webdriver.Chrome(...) и driver.quit() повторяется в каждом тесте.


#с фикстурой


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_home_page_title(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(2)
    assert "IT CAREER HUB" in driver.title


def test_about_page_title(driver):
    driver.get("https://itcareerhub.de/ru")
    about_link = driver.find_element(By.LINK_TEXT, "О нас")
    about_link.click()
    sleep(2)
    assert "О нас" in driver.title

#Плюсы:
# Весь код инициализации/закрытия браузера вынесен в фикстуру.
# Тесты сами по себе читаются как чистые сценарии.
# Если захочешь поменять, например, Chrome → Firefox, то меняешь только в фикстуре.