from selenium import webdriver
import math

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    n = calc(x)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(n)

    button = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()



    browser.find_element(By.CSS_SELECTOR, "[value='robots']").click()
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
finally:
    # успеваем скопировать код за 30
    math.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла