import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import pyautogui

def like_with_hashtags(driver):
    random_number = random.randint(2, 5)
    hashtags = ["motivation", "fitness"]
    for i in hashtags:
        comploted_likes = 0
        wait = WebDriverWait(driver, 10)
        url = "https://www.instagram.com/explore/tags/"+i+"/"
        driver.get(url)
        path = "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]"
        first_photo = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
        first_photo.click()
        for i in range(1,20):
            path = "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button"
            like_button = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
            like_button.click()
            pyautogui.press('right') 
            time.sleep(random_number)
            comploted_likes+=1
            