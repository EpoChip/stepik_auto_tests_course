from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    element = WebDriverWait(browser, 12, poll_frequency=0.1).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
        )
    button = browser.find_element(By.ID, 'book')
    button.click()
    browser.execute_script("window.scrollBy(0, 500);")

    element = browser.find_element(By.ID, "input_value")
    x = element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button = browser.find_element(By.ID, "solve")   
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()