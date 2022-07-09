from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

username = "" ## ENTER YOUR IG USERNAME HERE ##
password = "" ## ENTER YOUR IG PASSWORD HERE ##
s = Service("C:/Program Files/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "https://www.instagram.com/"
driver.get(url)

time.sleep(3)
name = "username"
username_input = driver.find_element(By.NAME,name)
username_input.send_keys(username)

name = "password"
password_input = driver.find_element(By.NAME,name)
password_input.send_keys(password)

time.sleep(3)
path = "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div" # Login button path
login_button = driver.find_element(By.XPATH,path)
login_button.click()
time.sleep(4)

