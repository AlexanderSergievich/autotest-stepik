from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    alert = browser.switch_to.alert
    alert.accept()


    # решение капчи
    x_element = browser.find_element(By.ID, "input_value").text
    n = calc(x_element)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(n)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
finally:
    # успеваем скопировать код за 30
    math.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла