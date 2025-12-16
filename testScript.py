from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

def clickCookieFor(clicks):
    for i in range(0, clicks):
        bigCookie.click()


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("file:///E:/projects/selenium2/index.html")
driver.maximize_window()
time.sleep(2)

bigCookie = driver.find_element(By.ID, "cookie")
x2multiplier = driver.find_element(By.ID, "x2")
x3multiplier = driver.find_element(By.ID, "x3")
x4multiplier = driver.find_element(By.ID, "x4")
x5multiplier = driver.find_element(By.ID, "x5")
x6multiplier = driver.find_element(By.ID, "x6")

clickCookieFor(100)
x3multiplier.click()
clickCookieFor(100)
x5multiplier.click()
clickCookieFor(100)
time.sleep(10)
driver.quit()





