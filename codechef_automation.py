
# Importing all required files
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import win32clipboard

# Get username and password from login.txt file
with open ('login.txt','r') as f:
    data=f.readlines()
    user=data[0][:-1]
    pswd=data[1]

browser=webdriver.Chrome("")
browser.maximize_window()

# opening and log in

browser.get('https://codechef.com')
browser.get('https://www.codechef.com/login?destination=/')
time.sleep(4)
username=browser.find_elements(By.ID,'edit-name')[1]
username.send_keys(user)
password=browser.find_elements(By.ID,'edit-pass')[1]
password.send_keys(pswd)

pyautogui.press('pagedown')
time.sleep(1.2)

#time.sleep(5)
# print(pyautogui.position())
pyautogui.click(539,355)
time.sleep(3)

# opening problem page

browser.get('https://www.codechef.com/practice')
browser.get('https://www.codechef.com/practice-old')
browser.get('https://www.codechef.com/problems/FOODCOST')
time.sleep(3)

# Writing code

with open('code.cpp','r')as f:
    codes=f.read()

#time.sleep(5)
# print(pyautogui.position())
pyautogui.click(1520,400) #also can be select by XPATH
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
pyautogui.hotkey('ctrl','a')
pyautogui.press('backspace')
win32clipboard.SetClipboardText(codes)
win32clipboard.CloseClipboard()
time.sleep(1.5)
pyautogui.hotkey('ctrl','v')


# Running and submitting code

run=browser.find_element(By.XPATH,'//*[@id="compile_btn"]').click()
time.sleep(8)
submit=browser.find_element(By.XPATH,'//*[@id="submit_btn"]').click()
time.sleep(12)