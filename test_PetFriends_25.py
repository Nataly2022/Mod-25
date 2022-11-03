from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import email, password  # файл в папке config с данными для авторизации



def test_show_my_pets(testing):
    #Проверяем что мы оказались на странице "Мои питомцы"

    # Устанавливаем явное ожидание
    element = WebDriverWait(testing, 10).until(EC.presence_of_element_located((By.ID, 'email')))
    testing.find_element(By.ID, 'email').send_keys(email)# Вводим email

    element = WebDriverWait(testing, 10).until(EC.presence_of_element_located((By.ID, "pass")))
    testing.find_element(By.ID, 'pass').send_keys(password)# Вводим пароль

    element = WebDriverWait(testing, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    testing.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()# Нажимаем на кнопку входа в аккаунт

    element = WebDriverWait(testing, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
    testing.find_element(By.LINK_TEXT, "Мои питомцы").click()# Нажимаем на ссылку "Мои питомцы"


    # Проверяем что мы оказались на странице "Мои питомцы"
    assert testing.current_url == 'https://petfriends.skillfactory.ru/my_pets'

    element = WebDriverWait(testing, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

    # Сохраняем в переменную ststistic элементы статистики
    statistic = testing.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

    element = WebDriverWait(testing, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

    # Сохраняем в переменную pets элементы карточек питомцев
    pets = testing.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Получаем количество питомцев из данных статистики
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Получаем количество карточек питомцев
    number_of_pets = len(pets)

    # Проверяем что количество питомцев из статистики совпадает с количеством карточек питомцев
    assert number == number_of_pets

    #Поверяем что на странице со списком моих питомцев хотя бы у половины питомцев есть фото

def test_photo(driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

    # Сохраняем в переменную ststistic элементы статистики
    statistic = driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

    # Сохраняем в переменную images элементы с атрибутом img
    images = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

    # Получаем количество питомцев из данных статистики
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Находим половину от количества питомцев
    half = number // 2

    # Находим количество питомцев с фотографией
    number_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            number_photos += 1

    # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
    assert number_photos >= half
    print(f'количество фото: {number_photos}')
    print(f'Половина от числа питомцев: {half}')

    #Поверяем что на странице со списком моих питомцев, у всех питомцев есть имя, возраст и порода

def test_have_full_description(driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//table/tbody/tr')))
    # Сохраняем в переменную pets_data элементы с данными о питомцах
    name = driver.find_elements(By.XPATH, '//table/tbody/tr/td[1]')
    type = driver.find_elements(By.XPATH, '//table/tbody/tr/td[2]')
    age = driver.find_elements(By.XPATH, '//table/tbody/tr/td[3]')
    for i in range(len(name)):
        assert name[i].text != ''
    for i in range(len(type)):
        assert type[i].text != ''
    for i in range(len(age)):
        assert age[i].text != ''

    #Поверяем что на странице со списком моих питомцев, у всех питомцев разные имена
def test_dubl_name(driver):
    #driver = testing
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//table/tbody/tr')))
    #Сохраняем в переменную pet_data элементы с данными о питомцах
    pets_data = driver.find_elements(By.XPATH, '//table/tbody/tr')

    # Из pets_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
    # и разделяем пробелом. Выбираем имена и добавляем их в список pets_name.
    pets_name = []
    for i in range(len(pets_data)):
        data_pets = pets_data[i].text.replace('\n', '').replace('×', '')
        split_data_pets = data_pets.split(' ')
        pets_name.append(split_data_pets[0])

    # Перебираем имена и если имя повторяется то прибавляем к счетчику r единицу.
    # Проверяем, если a == 0 то повторяющихся имен нет.
    a = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            a += 1
    assert a == 3
    print(a)
    print(pets_name)

    # Проверяем, что в списке нет повторяющихся питомцев
def test_similar_pets(driver):
    # Устанавливаем явное ожидание
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//table/tbody/tr')))

    # Сохраняем в переменную pet_data элементы с данными о питомцах
    pets_data = driver.find_elements(By.XPATH, '//table/tbody/tr')

    # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
    # и разделяем по пробелу.
    list_data = []
    for i in range(len(pets_data)):
        data_pets = pets_data[i].text.replace('\n', '').replace('×', '')
        split_data_pets = data_pets.split(' ')
        list_data.append(split_data_pets)

    # Объединяем имя, возраст и породу, в строку через пробел
    line = ''
    for i in list_data:
        line += ''.join(i)
        line += ' '

    # Получаем список из строки
    list_line = line.split(' ')

    # Превращаем список в множество
    set_list_line = set(list_line)

    # Находим количество элементов списка и множества
    x = len(list_line)
    y = len(set_list_line)

    # Из количества элементов списка вычитаем количество элементов множества
    result = x - y

    # Если количество элементов == 0 значит карточки с одинаковыми данными отсутствуют
    assert result == 0
