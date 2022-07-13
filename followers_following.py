from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_follower(driver,profilename):
    time.sleep(1)
    scroll_box = driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]')        
    last_ht = 0
    ht = 1
    while last_ht != ht:
        last_ht = ht
        ht = driver.execute_script(     ##Selenium Method to simulate scrolldown behavior##
            """
            arguments[0].scrollTo(0,arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """ ##Scrolls to bottom of followers list until it reaches end##
        ,scroll_box)
        time.sleep(2)
    links = scroll_box.find_elements(By.TAG_NAME, "a")
    names = []
    for i in links:
        if i.text != "":
            names.append(i.text)
    url = "https://www.instagram.com/"+profilename+"/"
    driver.get(url)
    return names

def get_followers_names(driver,profilename):
    url = "https://www.instagram.com/"+profilename+"/"
    driver.get(url)
    time.sleep(3)
    path = "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a"
    wait = WebDriverWait(driver, 10)
    followers_button = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
    followers_button.click()
    name_of_followers = get_follower(driver,profilename)
    f = open("follower_names.txt","w")
    for i in name_of_followers:
        f.write(i)
        f.write("\n")
    return name_of_followers

def get_following(driver,profilename):
    time.sleep(1)
    scroll_box = driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]')        
    last_ht = 0
    ht = 1
    while last_ht != ht:
        last_ht = ht
        ht = driver.execute_script(     ##Selenium Method to simulate scrolldown behavior##
            """
            arguments[0].scrollTo(0,arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """ ##Scrolls to bottom of followers list until it reaches end##
        ,scroll_box)
        time.sleep(2)
    links = scroll_box.find_elements(By.TAG_NAME, "a")
    names = []
    for i in links:
        if i.text != "":
            names.append(i.text)
    url = "https://www.instagram.com/"+profilename+"/"
    driver.get(url)
    return names
        
def get_following_names(driver,profilename):
    url = "https://www.instagram.com/"+profilename+"/"
    driver.get(url)
    time.sleep(3)
    path = "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]/a"
    wait = WebDriverWait(driver, 10)
    following_button = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
    following_button.click()
    name_of_following = get_following(driver,profilename)
    f = open("following_names.txt","w")
    for i in name_of_following:
        f.write(i)
        f.write("\n")
    return name_of_following   