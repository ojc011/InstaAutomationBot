import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from login import login_func
from like_comment_follow import like_with_hashtags, only_comments, follow_with_hashtags, like_comment_follow
from followers_following import get_following_names, get_followers_names
from random import randint

load_dotenv()
username = os.getenv('IG_UN') ## ENTER YOUR IG USERNAME HERE ##
password = os.getenv('IG_PW') ## ENTER YOUR IG PASSWORD HERE ##
driver = webdriver.Chrome("C:/Program Files/chromedriver/chromedriver.exe")
url = "https://www.instagram.com/"
driver.get(url)
time.sleep(2)
#login_func(username,password,driver)
wait = WebDriverWait(driver, 10)
profilename = "oliver.cronk"

def names_not_following_back(followers_file,following_file):
    f = open(followers_file,"r")
    follower_names = f.readlines()
    f = open(following_file,"r")
    following_names = f.readlines()
    not_following_back = []
    for i in following_names:
        if i not in follower_names and i !="":
            not_following_back.append(i[:-1])
    f = open("not_following_back.txt","w")
    for i in not_following_back:
        f.write(i)
        f.write("\n")
        
names_not_following_back("follower_names.txt", "following_names.txt")

