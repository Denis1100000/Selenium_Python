from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))


try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    message = WebDriverWait(browser, "12").until(
        EC.text_to_be_present_in_element((By.XPATH, "//div/div/h5[2] [contains(text(),'100')]"), "100")
    )
    button1 = browser.find_element(By.XPATH, "//div/div/button[@id='book']").click()

    x_element = browser.find_element(By.XPATH, "//div/label/span[2][@id='input_value']")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.XPATH, "//div/input[@name='text']").send_keys(y)

    button2 = browser.find_element(By.XPATH, "//button[@id='solve']").click()



finally:
    time.sleep(5)
    browser.quit()

