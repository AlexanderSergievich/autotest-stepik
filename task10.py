from selenium import webdriver
import time
import os

from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, "div[class='form-group'] :nth-child(2)").send_keys("Alexander")
    browser.find_element(By.CSS_SELECTOR, ".form-group [name='lastname']").send_keys('Stainberg')
    browser.find_element(By.CSS_SELECTOR, "div[class='form-group'] :nth-child(6)").send_keys('hi@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'textempty')  # добавляем к этому пути имя файла
    browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляциfor
    browser.quit()

