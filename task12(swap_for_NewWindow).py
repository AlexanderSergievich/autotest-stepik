from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary").click()
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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