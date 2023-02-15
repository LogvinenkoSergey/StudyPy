from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math


import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
    
link = "http://suninjuly.github.io/alert_accept.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
       
    button1 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value").text
    x = int(x_element)
    y = calc(x) 
        
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    
           
    
   
   

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла