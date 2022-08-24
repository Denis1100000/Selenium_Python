import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def link(linked):
        browser = webdriver.Chrome()
        browser.get(linked)

        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.first")
        input1.send_keys("Valeria")

        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.second")
        input2.send_keys("Vasilevskaya")

        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.third")
        input3.send_keys("Lera_the_best")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        return welcome_text_elt.text
        
        browser.quit()

class TestLink(unittest.TestCase):

    def test_link1(self):
        link1 = 'http://suninjuly.github.io/registration1.html'
        self.assertEqual(link(link1), "Congratulations! You have successfully registered!")

    def test_link2(self):
        link2 = 'http://suninjuly.github.io/registration2.html'
        self.assertEqual(link(link2), "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()