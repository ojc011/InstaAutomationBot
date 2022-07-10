import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from login import login_func

load_dotenv()

username = os.getenv('IG_UN') ## ENTER YOUR IG USERNAME HERE ##
password = os.getenv('IG_PW') ## ENTER YOUR IG PASSWORD HERE ##
s = Service("C:/Program Files/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=s)

login_func(username,password,driver)
