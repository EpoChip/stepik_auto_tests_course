from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"][required]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"][required]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, 'input[name="email"][required]')
    input3.send_keys("Test@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'new.txt')  
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)

    button = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]')   
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()