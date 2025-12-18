from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import cookiePageElements 

def run(winPosSize, finalNumber):
    
    sizeWidth = winPosSize[0]
    sizeHeight = winPosSize[1]  
    positionX = winPosSize[2]
    positionY = winPosSize[3]

    service = Service(executable_path="testcases/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("file:///E:/projects/selenium2/index.html")
    
    #element declaration
    bigCookie = driver.find_element(By.ID, cookiePageElements.getElement("cookie")['id'])
    x2multiplier = driver.find_element(By.ID, cookiePageElements.getElement("x2buff")['id'])
    x3multiplier = driver.find_element(By.ID, cookiePageElements.getElement("x3buff")['id'])
    x4multiplier = driver.find_element(By.ID, cookiePageElements.getElement("x4buff")['id'])
    x5multiplier = driver.find_element(By.ID, cookiePageElements.getElement("x5buff")['id'])
    x6multiplier = driver.find_element(By.ID, cookiePageElements.getElement("x6buff")['id'])
    reset = driver.find_element(By.ID, cookiePageElements.getElement("reset")['id'])

    #set window size and position
    driver.set_window_size(sizeWidth, sizeHeight)
    driver.set_window_position(positionX, positionY)



#debug code
def run1():
    print("buff checker reporting")