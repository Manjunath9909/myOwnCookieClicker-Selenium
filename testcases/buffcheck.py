from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import cookiePageElements 

def run(winPosSize, finalNumber):
    
    sizeWidth = winPosSize[0]
    sizeHeight = winPosSize[1]  
    positionX = winPosSize[2]
    positionY = winPosSize[3]

    service = Service(executable_path="testcases/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("file:///E:/projects/selenium2/index.html")
    
    time.sleep(2)

    #element declaration
    bigCookie = driver.find_element(By.ID, cookiePageElements.getElement("cookieButton")['id'])
    x2multiplier = driver.find_element(By.ID, cookiePageElements.getElement("x2buff")['id'])
    x3multiplier = driver.find_element(By.ID, cookiePageElements.getElement("x3buff")['id'])
    x4multiplier = driver.find_element(By.ID, cookiePageElements.getElement("x4buff")['id'])
    x5multiplier = driver.find_element(By.ID, cookiePageElements.getElement("x5buff")['id'])
    x6multiplier = driver.find_element(By.ID, cookiePageElements.getElement("x6buff")['id'])
    reset = driver.find_element(By.ID, cookiePageElements.getElement("reset")['id'])

    #set window size and position
    driver.set_window_size(sizeWidth, sizeHeight)
    driver.set_window_position(positionX, positionY)
    time.sleep(2)
    clickCookieFor(bigCookie, 200)
    x2multiplier.click()
    time.sleep(1)
    x3multiplier.click()
    driver.switch_to.alert.dismiss()
    clickCookieFor(bigCookie, 300)
    time.sleep(1)
    x4multiplier.click()
    clickCookieFor(bigCookie, 50)
    time.sleep(1)
    x5multiplier.click()
    driver.switch_to.alert.dismiss()
    time.sleep(1)
    clickCookieFor(bigCookie, 50)
    x5multiplier.click()
    clickCookieFor(bigCookie, 120)
    x6multiplier.click()
    clickCookieFor(bigCookie, 10)
    time.sleep(1)
    cookieJar = driver.execute_script("return getCookieJar();")
    if cookieJar == finalNumber:
        print("------------- Test complete -------------")
        time.sleep(2)
        driver.quit()
    elif cookieJar != finalNumber:
        print("------------- Test failed -------------")
        time.sleep(2)
        driver.quit()


def clickCookieFor(bigCookie, clicks):
    for i in range(0, clicks):
        bigCookie.click()

#debug code
def run1():
    print("buff checker reporting")