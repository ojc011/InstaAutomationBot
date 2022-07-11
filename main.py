import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import login_func
from like_comment_follow import like_with_hashtags
load_dotenv()
username = os.getenv('IG_UN') ## ENTER YOUR IG USERNAME HERE ##
password = os.getenv('IG_PW') ## ENTER YOUR IG PASSWORD HERE ##
driver = webdriver.Chrome("C:/Program Files/chromedriver/chromedriver.exe")
url = "https://www.instagram.com/"
driver.get(url)
time.sleep(2)
wait = WebDriverWait(driver, 10)
login_func(username,password,driver)
like_with_hashtags(driver)