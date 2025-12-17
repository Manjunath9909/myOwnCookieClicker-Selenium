from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

def run(positionX, positionY, sizeWidth, sizeHeight, finalExpectedCookieJar):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("file:///E:/projects/selenium2/index.html")
    bigCookie = driver.find_element(By.ID, "cookie")
    x2multiplier = driver.find_element(By.ID, "x2")
    x3multiplier = driver.find_element(By.ID, "x3")
    x4multiplier = driver.find_element(By.ID, "x4")
    x5multiplier = driver.find_element(By.ID, "x5")
    x6multiplier = driver.find_element(By.ID, "x6")
    driver.set_window_size(sizeWidth, sizeHeight)
    driver.set_window_position(positionX, positionY)
    time.sleep(2)
    clickCookieFor(10)
    x3multiplier.click()
    time.sleep(2)
    driver.switch_to.alert.dismiss()
    clickCookieFor(100)
    x5multiplier.click()
    time.sleep(2)
    driver.switch_to.alert.dismiss()
    clickCookieFor(100)
    x2multiplier.click()
    clickCookieFor(300)

    #check if final value matches and close test
    cookieJar = driver.execute_script("return getCookieJar();")
    if cookieJar == finalExpectedCookieJar:
        print("------------- Text complete -------------")
        time.sleep(2)
        driver.quit()

    else:
        print("------------- The test failed -----------")
        driver.quit()
        
bigCookie = None
def clickCookieFor(clicks):
    for i in range(0, clicks):
        bigCookie.click()

def run1():
    print("counter checker reporting")


