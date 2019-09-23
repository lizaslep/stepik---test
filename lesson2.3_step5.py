from selenium import webdriver
import os 
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
     
    button = browser.find_element_by_css_selector("button.trollface")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    element = browser.find_element_by_css_selector("#input_value")
    x_element = element.text
    
    y = calc(x_element)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button2 = browser.find_element_by_css_selector("button.btn")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()
