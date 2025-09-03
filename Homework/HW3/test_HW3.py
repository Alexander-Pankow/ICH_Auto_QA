import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    # Инициализация WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Максимизация окна
    driver.maximize_window()
    driver.get("https://itcareerhub.de/ru")
    # Передача драйвера в тест
    yield driver
    # Закрытие браузера
    driver.quit()


# Логитип ITCareerHub
def test_logo_ICH(driver):
    edit_logo_ICH = driver.find_element(By.CSS_SELECTOR, "img.tn-atom__img")
    assert edit_logo_ICH.is_displayed()

# Ссылка “Программы”
def test_programs_ICH(driver):
    programs_ICH = driver.find_element(By.CSS_SELECTOR, "a.tn-atom.t794__tm-link")
    assert programs_ICH.is_displayed()

# Ссылка “Способы оплаты”
def test_payment_methods_ICH(driver):
    payment_methods_ICH = driver.find_element(By.XPATH,  "//*[normalize-space(text())='Способы оплаты' and contains(@class, 'tn-atom')]")
    assert payment_methods_ICH.is_displayed()

#Ссылка “Новости”
def test_news_ICH(driver):
    news_ICH = driver.find_element(By.XPATH,  "//*[normalize-space(text())='Новости' and contains(@class, 'tn-atom')]")
    assert news_ICH.is_displayed()

#Ссылка “О нас”
def test_about_us_ICH(driver):
    about_us_ICH = driver.find_element(By.XPATH,  "//*[normalize-space(text())='О нас' and contains(@class, 'tn-atom')]")
    assert about_us_ICH.is_displayed()

#Ссылка “Отзывы”
def test_reviews_ICH(driver):
    reviews_ICH = driver.find_element(By.XPATH,  "//*[normalize-space(text())='Отзывы' and contains(@class, 'tn-atom')]")
    assert reviews_ICH.is_displayed()

#Кнопки переключения языка (ru и de)
def test_switching_language_ru_ICH(driver):
    switching_language_ru_ICH = driver.find_element(By.XPATH,  "//*[normalize-space(text())='ru' and contains(@class, 'tn-atom')]")
    assert switching_language_ru_ICH.is_displayed()

def test_switching_language_de_ICH(driver):
    switching_language_de_ICH = driver.find_element(By.XPATH,  "//a[@href='/']")
    assert switching_language_de_ICH.is_displayed()

# Кликнуть по иконке с телефонной трубкой
def test_click_phone_icon(driver):
    phone_icon = driver.find_element(By.XPATH, '//a[@href="#popup:form-tr3"]//img[contains(@src,"Group_3800.svg")]')
    phone_icon.click()


#Проверить что текст “Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами” отображается.
def test_phone_popup(driver):
    phone_button = driver.find_element(By.CSS_SELECTOR, 'a[href="#popup:form-tr3"] img[src*="Group_3800.svg"]')
    phone_button.click()

    sleep(3)

    expected_text = "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"
    popup_element = driver.find_element(By.XPATH, f'//*[contains(text(), "{expected_text}")]')
    assert popup_element.is_displayed()
    driver.quit()