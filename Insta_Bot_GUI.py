from main import *
from tkinter import *
from PIL import ImageTk, Image
import pyautogui
root = Tk()


def login_phase(driver, username, password):
    login_func(username, password, driver)
    get_followers_names_button = Button(
        root, text="Get Followers Names", bg="#19e5cc", command=lambda: get_followers_names(driver, username))
    get_followers_names_button.grid(
        padx=5, pady=5)

    get_following_names_button = Button(
        root, text="Get Following Names", bg="#19e5cc", command=lambda: get_following_names(driver, username))
    get_following_names_button.grid(
        padx=5, pady=5)

    get_not_following_back_names_button = Button(
        root, text="Not Following Back Names", bg="#19e5cc", command=lambda: names_not_following_back(
            "follower_names.txt", "following_names.txt"))
    get_not_following_back_names_button.grid(padx=5, pady=5)

    unfollow_with_file_button = Button(
        root, text="Unfollow Not Following Back", bg="#19e5cc", command=lambda: unfollow_with_file(driver, "not_following_back.txt"))
    unfollow_with_file_button.grid(padx=5, pady=5)

    Label(root, text="Hashtags:").grid()
    hashtags = Entry(root, bd=5)
    hashtags.grid()

    like_button = Button(
        root, text="Like With Hashtags", bg="#19e5cc", command=lambda: like_with_hashtags(
            driver, hashtags.get().split(",")))
    like_button.grid(padx=5, pady=5)

    comment_button = Button(
        root, text="Comment With Hashtags", bg="#19e5cc", command=lambda: only_comments(driver, hashtags.get().split(",")))
    comment_button.grid(
        padx=5, pady=5)

    follow_button = Button(
        root, text="Follow With Hashtags", bg="#19e5cc", command=lambda: follow_with_hashtags(driver, hashtags.get().split(",")))
    follow_button.grid(
        padx=5, pady=5)

    like_comment_follow_button = Button(
        root, text="Like Comment And Follow", bg="#19e5cc", command=lambda: like_comment_follow(driver, hashtags.get().split(",")))
    like_comment_follow_button .grid(
        padx=5, pady=5)


def start_browser():

    driver = webdriver.Chrome("C:/Program Files/chromedriver/chromedriver.exe")
    url = "https://www.instagram.com/"
    driver.get(url)
    time.sleep(3)
    login_phase(driver, username_input.get(), password_input.get())
    
file = Image.open("image.jpg")
file = file.resize((200, 200), Image.ANTIALIAS)
image = ImageTk.PhotoImage(file)
Label(root, image=image).grid(row=0, column=0, padx=150)
root.title("Instagram Automation Application")
    
Label(root, text="username:").grid()
username_input = Entry(root, bd=5)
username_input.grid()

Label(root, text="password:").grid(padx=5, pady=5)
password_input = Entry(root, bd=5, show="*")
password_input.grid()

Login_button = Button(root, text="Login", fg="white", bg="green", command=lambda: start_browser())
Login_button.grid(padx=5, pady=5)
root.geometry("500x900")
creater = Label(root, text="Created By Oliver Cronk",
                fg="white", bg="green")
creater.place(relx=0.4, rely=0.95)

root.mainloop()