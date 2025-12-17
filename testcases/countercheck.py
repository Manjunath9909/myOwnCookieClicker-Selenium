from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
def run(winPosSize,  finalExpectedCookieJar):

    sizeWidth = winPosSize[0]
    sizeHeight = winPosSize[1]
    positionX = winPosSize[2]
    positionY = winPosSize[3]

    service = Service(executable_path="testcases/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("file:///E:/projects/selenium2/index.html")

    #element declaration
    bigCookie = driver.find_element(By.ID, "cookie")
    x2multiplier = driver.find_element(By.ID, "x2")
    x3multiplier = driver.find_element(By.ID, "x3")
    x4multiplier = driver.find_element(By.ID, "x4")
    x5multiplier = driver.find_element(By.ID, "x5")
    x6multiplier = driver.find_element(By.ID, "x6")

    #set window size and position
    driver.set_window_size(sizeWidth, sizeHeight)
    driver.set_window_position(positionX, positionY)
    time.sleep(2)
    clickCookieFor(bigCookie,10)
    x3multiplier.click()
    time.sleep(2)
    driver.switch_to.alert.dismiss()
    clickCookieFor(bigCookie, 100)
    x5multiplier.click()
    time.sleep(2)
    driver.switch_to.alert.dismiss()
    clickCookieFor(bigCookie, 100)
    x2multiplier.click()
    clickCookieFor(bigCookie, 100)

    #check if final value matches and close test
    cookieJar = driver.execute_script("return getCookieJar();")
    if cookieJar == finalExpectedCookieJar:
        print("------------- Test complete -------------")
        time.sleep(2)
        driver.quit()

    else:
        print("------------- The test failed -----------")
        time.sleep(2)
        driver.quit()
        
def clickCookieFor(bigCookie, clicks):
    for i in range(0, clicks):
        bigCookie.click()

#debug code
def run1():
    print("counter checker reporting")

#run([300,600,300,0], 210)