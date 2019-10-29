from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(x))))
   
try: 

  
  
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
     
    button = browser.find_element_by_id("book")
    button.click()
    
    time.sleep(1)
    
      
    x_element = browser.find_element_by_css_selector(".form-group #input_value")
    x = int(x_element.text)
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

   
  
    # Отправляем заполненную форму
    button2 = browser.find_element_by_css_selector("button[type=submit]")
    button2.click()

    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

