from selenium import webdriver
import time

from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")


    x = browser.find_element(By.CSS_SELECTOR, "#num1").text
    y = browser.find_element(By.CSS_SELECTOR, "#num2").text
    z = int(x) + int(y)
    z = str(z)

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
    select.select_by_value(z)
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
finally:
    # успеваем скопировать код за 30
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла