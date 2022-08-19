from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pathlib import Path

link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//div/input[@placeholder='Enter first name']")
    input1.send_keys("Denis")

    input2 = browser.find_element(By.XPATH, "//div/input[@placeholder='Enter last name']")
    input2.send_keys("Makarov")

    input3 = browser.find_element(By.XPATH, "//div/input[@placeholder='Enter email']")
    input3.send_keys("Makarov@gmail.com")

    element = browser.find_element(By.XPATH, "//form/input[@id='file']")
    element1 = "C:\selenium_course"
    element.send_keys(element1)
    
    button1 = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    button1.click()

    time.sleep(5)

finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
  time.sleep(5)
  # закрываем браузер после всех манипуляций
  browser.quit()

