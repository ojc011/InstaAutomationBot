from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def login_func(username,password,driver):
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.NAME,"username")))
    username_input.send_keys(username)
    passwd_input = wait.until(EC.presence_of_element_located((By.NAME,"password")))
    passwd_input.send_keys(password)
    path = "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div"
    time.sleep(1)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
    login_button.click()
    time.sleep(5)
    path = "/html/body/div[1]/section/main/div/div/div/div/button"
    not_now_button1 = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
    not_now_button1.click()
    time.sleep(2)
    path = "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]"
    not_now_button2 = wait.until(EC.element_to_be_clickable((By.XPATH,path)))
    not_now_button2.click()
    time.sleep(3)