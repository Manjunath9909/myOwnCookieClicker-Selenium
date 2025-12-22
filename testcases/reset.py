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
    reset = driver.find_element(By.ID, cookiePageElements.getElement("reset")['id'])

    #set window size and position
    driver.set_window_size(sizeWidth, sizeHeight)
    driver.set_window_position(positionX, positionY)
    time.sleep(2)
    clickCookieFor(bigCookie, 1000)
    time.sleep(2)
    reset.click()
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