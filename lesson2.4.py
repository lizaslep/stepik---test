from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    text1 = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_id("book")
    button.click()
        
    element = browser.find_element_by_css_selector("#input_value")
    x_element = element.text
    y = calc(x_element)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    submit = browser.find_element_by_id("solve")
    submit.click()
finally:
    time.sleep(10)
    browser.quit()
