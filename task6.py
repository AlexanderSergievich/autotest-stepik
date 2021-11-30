from selenium import webdriver
import math

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    n = calc(x)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(n)
    browser.find_element(By.CSS_SELECTOR, ".form-check.form-check-custom input").click()
    browser.find_element(By.CSS_SELECTOR, "[value='robots']").click()
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
finally:
    # успеваем скопировать код за 30
    math.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла