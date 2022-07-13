import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from random import randint
import pyautogui

def like_with_hashtags(driver):
    hashtags = ["fitness", "motivation"]
    for i in hashtags:
        completed_likes = 0
        wait = WebDriverWait(driver, 10)
        url = "https://www.instagram.com/explore/tags/"+i+"/"
        driver.get(url)
        path = "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]"
        first_photo = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
        first_photo.click()
        for i in range(1,100):
            path = "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button"
            like_button = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
            like_button.click()
            pyautogui.press('right') 
            time.sleep(randint(2, 5))
            completed_likes+=1

def only_comments(driver):
    comments = ["Looking great", "Awesome work", "Keep it up", "Nice!"]
    hashtags = ["fitness", "motivation"]
    for i in hashtags:
        completed_comments = 0
        wait = WebDriverWait(driver, 10)
        url = "https://www.instagram.com/explore/tags/"+i+"/"
        driver.get(url)
        path = "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]"
        first_photo = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
        first_photo.click()
        for i in range(1,100):
            path = "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form"
            comment_area = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
            comment_area.click()
            path = "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea"
            time.sleep(3)
            comment_text = wait.until(EC.presence_of_element_located((By.XPATH,path)))
            comment = comments[randint(0,len(comments)-1)]  
            comment_text.send_keys(comment)
            time.sleep(3)
            path = "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button"
            post_button = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
            post_button.click()
            pyautogui.press('right') 
            time.sleep(randint(2,5))
            completed_comments+=1
    print("Completed comments : "+ completed_comments)
    
def follow_with_hashtags(driver):
    hashtags = ["fitness", "motivation"]
    for i in hashtags:
        completed_follows = 0
        wait = WebDriverWait(driver, 10)
        url = "https://www.instagram.com/explore/tags/"+i+"/"
        driver.get(url)
        path = "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]"
        first_photo = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
        first_photo.click()
        for i in range(1,100):
            path = "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button"
            follow_button = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
            if(follow_button.text != "Following"):
                follow_button.click()
            else: pass
            pyautogui.press('right') 
            time.sleep(randint(2,5))
            completed_follows+=1
    print("Completed follows : "+ completed_follows)
    
def like_comment_follow(driver):
    comments = ["Lookin good", "Handsome", ":)"]
    hashtags = ["fitness","motivation"]
    for i in hashtags: 
        wait = WebDriverWait(driver, 10)
        url = "https://www.instagram.com/explore/tags/"+i+"/"
        driver.get(url)
        path = "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]"
        first_photo = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
        first_photo.click()
        for i in range(1,100):
            completed_lcf = 0
            path = "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form"
            comment_area = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
            comment_area.click()
            path = "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea"
            time.sleep(3)
            comment_text = wait.until(EC.presence_of_element_located((By.XPATH,path)))
            comment = comments[randint(0,len(comments)-1)]  
            comment_text.send_keys(comment)
            time.sleep(3)
            path = "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button"
            post_button = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
            post_button.click()
            time.sleep(3)
            path = "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button"
            like_button = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
            like_button.click()
            time.sleep(3)
            path = "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button"
            follow_button = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
            if(follow_button.text != "Following"):
                follow_button.click()
            else: pass
            pyautogui.press('right') 
            time.sleep(randint(2,5))
            completed_lcf+=1
        print("Completed LCF : "+ completed_lcf)

            