import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from login import login_func
from like_comment_follow import *
from followers_following import *

load_dotenv()
username = os.getenv('IG_UN') ## ENTER YOUR IG USERNAME HERE ##
password = os.getenv('IG_PW') ## ENTER YOUR IG PASSWORD HERE ##
driver = webdriver.Chrome("C:/Program Files/chromedriver/chromedriver.exe")
url = "https://www.instagram.com/"
driver.get(url)
time.sleep(2)
login_func(username,password,driver)
wait = WebDriverWait(driver, 10)
profilename = "oliver.cronk"


filename = "not_following_back.txt"
unfollow_with_file(driver,filename)

