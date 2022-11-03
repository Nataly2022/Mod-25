
from selenium.webdriver.common.by import By
from config import email, password  # файл в папке config с данными для авторизации


def test_show_all_pets(testing):
    # Вводим email
    testing.find_element(By.ID, 'email').send_keys(email)
    # Вводим пароль
    testing.find_element(By.ID, 'pass').send_keys(password)

    # Настраиваем неявные ожидания
    testing.implicitly_wait(5)

    # Нажимаем на кнопку входа в аккаунт
    testing.find_element(By.CSS_SELECTOR, 'button[type = "submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert testing.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    images = testing.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = testing.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = testing.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''  # на странице нет питомцев без фото
        assert names[i].text != ''  # на странице нет питомцев без Имени
        assert descriptions[i].text != ''  # на странице нет питомцев с пустым полем для указания Породы и возраста
        assert ', ' in descriptions[i]  # проверяем, что между породой и лет есть запятая (значит есть оба значения)
        parts = descriptions[i].text.split(", ")  # Создаём список, где разделитель значений - запятая
        assert len(parts[0]) > 0  # Проверяем, что длина текста в первой части списка и
        assert len(parts[1]) > 0  # ...и во второй > 0, значит там что-то да указано! Если нет -> FAILED!

    assert testing.find_element(By.TAG_NAME, 'h1').text == "PetFriends"  # Проверяем, что мы были на главной
    # есть утверждение для проверки заголовка страницы, что <title> Label содержит текст «PetFriends»:
    assert 'PetFriends' in testing.title  # да, работает

