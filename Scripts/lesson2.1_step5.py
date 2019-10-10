from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
  
  x_element = browser.find_element_by_id("input_value")
  x = x_element.text
  y = calc(x)
  
    input1 = browser.find_element_by_id("answer")
    input1.send_keys("y")
	checkbox1 = browser.find_element_by_id("robotCheckbox")
	checkbox1.click()
	radibutton1 = browser.find_element_by_id("roborsRule")
	radibutton1.click()
	
	button = browser.find_element_by_css_selector("button.btn")
    button.click()
 
 finally:
    
    time.sleep(30)
    
    browser.quit()
    