import pytest
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
    driver.get("https://suninjuly.github.io/cats.html")
    # Передача драйвера в тест
    yield driver
    # Закрытие браузера
    driver.quit()

def test_open_cats_page(driver):
    page_header = driver.find_element(By.CSS_SELECTOR, "[class='jumbotron-heading']")
    assert page_header.text == "Cat memes"


def test_name_of_second_cat(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    second_cat = driver.find_element(By.CSS_SELECTOR, "p.card-text.second")
    # Проверяем текст
    assert second_cat.text == "Serious cat", f"Expected 'Serious cat' but got '{second_cat.text}'"
#Check that name of the second cat card is "Serious cat"


# #XPath //p[contains(@class, 'second')]
def test_name_of_second_cat_1(driver):
    second_cat = driver.find_element(By.XPATH, "//p[contains(@class, 'second')]")
    # Проверяем текст
    assert second_cat.text == "Serious cat"


# XPath  (//div[@class="col-sm-4"])[5]//small
# CSS_SELECTOR .col-sm-4:nth-child(5) .text-muted
def test_fifth_cat_card_time(driver):
    fifth_cat_time = driver.find_element(By.CSS_SELECTOR,".col-sm-4:nth-child(5) small")
    assert fifth_cat_time.text == "9 mins"


#Написать тест, который проверяет наличия теста "Cats album"возле иконки фото
def test_cats_album(driver):
    cats_album = driver.find_element(By.CSS_SELECTOR,".navbar-brand")
    assert cats_album.text == "Cats album"


#работа с картинками (картинка фотика в начале)
def test_photo_img_is_dispalyed(driver):
    photo_img = driver.find_element(By.CSS_SELECTOR, "svg.mr-2")
    assert photo_img.is_displayed() == True



#поиск по TAG_NAME
def test_photo_img_is_dispalyed_1(driver):
    photo_img = driver.find_element(By.TAG_NAME, "svg")
    assert photo_img.is_displayed() == True



#Check that Edit button if 4th cat card is displayed

def test_edit_button_4th_card_is_displayed(driver):
    edit_button = driver.find_element(By.CSS_SELECTOR, ".col-sm-4:nth-child(4) button:nth-child(2)")
    assert edit_button.is_displayed()


#XPath (//div[@class="col-sm-4"])[4]//button[2]
def test_edit_button_4th_card_is_displayed(driver):
    edit_button = driver.find_element(By.XPATH, "(//div[@class='col-sm-4'])[4]//button[2]")
    assert edit_button.is_displayed()


# проверяем коллекцию элементов по классу
def test_cat_cards_quantity(driver):
    cat_cards = driver.find_elements(By.CLASS_NAME, "col-sm-4")
    assert len(cat_cards) == 6

# Проверить что на странице 6 картинок c котиками
def test_images_quantity(driver):
    images = driver.find_elements(By.TAG_NAME, "img")
    assert len(images) == 6


