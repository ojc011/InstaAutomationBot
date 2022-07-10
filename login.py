from selenium.webdriver.common.by import By
import time

def login_func(username,password,driver):
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
    time.sleep(3)

    path = "/html/body/div[1]/section/main/div/div/div/div/button" # 'Not Now' for save info button #
    not_now_button = driver.find_element(By.XPATH,path)
    not_now_button.click()
    time.sleep(4)

    path = "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]"
    not_now_button1 = driver.find_element(By.XPATH,path)
    not_now_button1.click()
    time.sleep(4)