from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)



    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button1 = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    button1.click()

    time.sleep(10)

finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()




