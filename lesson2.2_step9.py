from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    find_a = browser.find_element(By.ID, "num1")
    a = find_a.text
    find_b = browser.find_element(By.ID, "num2")
    b = find_b.text
    c = str(int(a)+int(b))
    
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(c) 

    button = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]')
    button.click()

finally:
    time.sleep(20)
    browser.quit()