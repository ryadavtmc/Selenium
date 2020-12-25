import time

import driver as driver
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(4)


# useHere = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[2]/div[2]/div/div')
# useHere.click()
def searchUser():
    # search = input("Enter username to search: ")
    user = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    user.send_keys('Enter the name which you want to search from your contactlist')
    time.sleep(4)
    searchUser = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]')
    searchUser.click()


def typeMsg():
    # msg = input("Enter your message to send ")
    sendMsg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    sendMsg.send_keys('Enter the message to send')
    sendMsgButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
    sendMsgButton.click()


while True:
    searchUser()
    typeMsg()
