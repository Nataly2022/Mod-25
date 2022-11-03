from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from config import email, password  # файл в папке config с данными для авторизации


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome('C:/test/chromedriver.exe')
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')
    driver.find_element(By.ID, 'email').send_keys(email)  # Вводим email
    driver.find_element(By.ID, 'pass').send_keys(password)  # Вводим пароль
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()  # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.LINK_TEXT, "Мои питомцы").click()  # Нажимаем на ссылку "Мои питомцы"

    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def testing():
    testing = webdriver.Chrome('C:/test/chromedriver.exe')
    # Переходим на страницу авторизации
    testing.get('https://petfriends.skillfactory.ru/login')

    yield testing
    testing.quit()
