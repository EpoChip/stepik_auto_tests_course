from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, '//button[contains(text(), "I want to go on a magical journey!")]')   
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    element = browser.find_element(By.ID, "input_value")
    x = element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]')   
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()