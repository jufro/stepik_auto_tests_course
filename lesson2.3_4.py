from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element(By.ID, "input_value").text
    y = func(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    print(browser.switch_to.alert.text)

finally:
    # time.sleep(10)
    browser.quit()
