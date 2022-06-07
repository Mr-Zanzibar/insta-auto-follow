from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import random


chrome_driver_path = "" # your chromedriver path
similar_account = "" # you wanna auto add the ig's account
username = "" # your ig account name
password = "" # your ig password


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        user_input = self.driver.find_element_by_name('username')
        user_pass = self.driver.find_element_by_name('password')
        user_input.send_keys(username)
        user_pass.send_keys(password)
        time.sleep(2)
        user_pass.send_keys(Keys.ENTER)
        time.sleep(5)
        
    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{similar_account}")
        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(random.randint(500,1000)/1000)
        
    
    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(random.randint(500,1000)/1000)
                
                
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
