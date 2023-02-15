from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

    
link = "http://suninjuly.github.io/cats.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
       
    button1 = browser.find_element(By.ID, "button")
    button1.click()


    
           
    
   
   

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла