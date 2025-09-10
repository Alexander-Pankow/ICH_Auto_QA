"""
Задание 1: Проверка наличия текста в iframe

Открыть страницу
Перейти по ссылке: https://bonigarcia.dev/selenium-webdriver-java/iframes.html.
Проверить наличие текста
Найти фрейм (iframe), в котором содержится искомый текст.
Переключиться в этот iframe.
Найти элемент, содержащий текст "semper posuere integer et senectus justo curabitur.".
Убедиться, что текст отображается на странице.
"""
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    yield driver
    driver.quit()

def test_iframe_lead_text(driver):
    wait = WebDriverWait(driver, 10)
    # Ждем появления хотя бы одного iframe и переключаемся в него
    iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(iframe)
    # Находим все элементы с классом lead внутри iframe
    lead_elements = driver.find_elements(By.CLASS_NAME, "lead")
    # Проверяем, что нужный текст есть хотя бы в одном элементе
    assert any("semper posuere integer et senectus justo curabitur." in el.text for el in lead_elements), \
        "Текст 'semper posuere integer et senectus justo curabitur.' не найден ни в одном элементе lead"
    # Возвращаемся на главную страницу
    driver.switch_to.default_content()


"""
Задание 2: Тестирование Drag & Drop (Перетаскивание изображения в корзину)

Открыть страницу Drag & Drop Demo.
Перейти по ссылке: https://www.globalsqa.com/demo-site/draganddrop/.
Выполнить следующие шаги:
Захватить первую фотографию (верхний левый элемент).
Перетащить её в область корзины (Trash).
Проверить, что после перемещения:
В корзине появилась одна фотография.
В основной области осталось 3 фотографии.
Ожидаемый результат:
Фотография успешно перемещается в корзину.
Вне корзины остаются 3 фотографии.
"""

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    yield driver
    driver.quit()


def test_drag_and_drop(driver):
    time.sleep(5) # это для меня у меня банер с настройками появляется

    wait = WebDriverWait(driver, 20)
    # Ждем iframe и переключаемся в него
    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame")))
    driver.switch_to.frame(iframe)
    # Находим первую фотографию и корзину
    image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#gallery li")))
    trash = driver.find_element(By.ID, "trash")
    # Перетаскиваем фотографию в корзину
    actions = ActionChains(driver)
    actions.click_and_hold(image).move_to_element(trash).release().perform()
    time.sleep(1)  # ждем, пока JS обработает событие
    # Проверяем количество фотографий
    trash_images = driver.find_elements(By.CSS_SELECTOR, "#trash li")
    gallery_images = driver.find_elements(By.CSS_SELECTOR, "#gallery li")
    assert len(trash_images) == 1
    assert len(gallery_images) == 3