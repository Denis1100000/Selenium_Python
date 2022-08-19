from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


link = "http://suninjuly.github.io/selects2.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)


    element1 = browser.find_element(By.ID, "num1")
    element2 = browser.find_element(By.ID, "num2")
    x = element1.text
    x1 = element2.text
    y = int(x) + int(x1)
    y1 = str(y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y1))

    button1 = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    button1.click()

    time.sleep(1)

finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
  time.sleep(5)
  # закрываем браузер после всех манипуляций
  browser.quit()




