import pyautogui
import webbrowser as wb
import time
from time import sleep
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import os
class InstagramBot:

    def __init__(self, username, password):
        self.username=username
        self.password=password
        self.driver=webdriver.Chrome('./chromedriver.exe')
        self.login()
        
    def login(self):
        self.driver.get('https://www.instagram.com')
        sleep(2)

        #Login
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input"))).send_keys(self.username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(self.password)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(Keys.ENTER)
        sleep(4)

        #Starting Following 
        print("Starting Following !!!")    
        for i in userstofollow:
            self.driver.get('https://www.instagram.com/' + i)
            sleep(2)
            try:
                WebDriverWait(self.driver,4).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Follow')]"))).click()
                print("Followed " + i)
                userstounfollow.append(i)

            except:
                print("You already follow " + i)

        
        #Starting Unfollowing
        print("Starting Unfollowing !!!")
        try:
            userstounfollow.remove("ishuxrajput")
        except:
            print(" ")
            
        for i in userstounfollow:
            self.driver.get('https://www.instagram.com/' + i)
            sleep(2)
            try:
                WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.CLASS_NAME, "_5f5mN.-fzfL._6VtSN.yZn4P   "))).click()
                WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Unfollow')]"))).click()
                print("Unfollowed " + i)
            except:
                print("You don't follow " + i)

        sleep(5)


class logo:
    print("      ")
    print("      ")
    print("      ")
    print("      █████████████████████████████████████████   ")
    print("      █▄─▄█▄─▀█▄─▄█─▄▄▄▄█─▄─▄─█▄─▄▄▀█▄─▄█▄─▀─▄█   ")
    print("      ██─███─█▄▀─██▄▄▄▄─███─████─▄─▄██─███▀─▀██   ")
    print("      ▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▄▄█▄▄▀   ")
    print("      ")
    print("      █████████  𝙱𝚢 𝙸𝚜𝚑𝚞 𝚂𝚒𝚗𝚐𝚑 𝚁𝚊𝚓𝚙𝚞𝚝  █████████   ")
    print("      ")
    print("    ")
        
        
        
        

if __name__=='__main__':
    userstofollow = ["therock", "instagram", "cristiano" , "arianagrande" , 'kyliejenner' , 'leomessi' , 'selenagomez' , 'kimkardashian' , 'beyonce' , 
    'justinbieber' , 'ishuxrajput', 'kendalljenner' , 'natgeo' , 'taylorswift' , 'jlo' , 'nike' , 'neymarjr', 'virat.kohli', 'mileycyrus', 'zendaya' , 'ddlovato',
    'billieeilish' , 'vindiesel' , 'dualipa', 'nasa' , 'priyankachopra', 'snoopdogg' , 'shawnmendes', 'nehakakkar' , 'gal_gadot' , 'emmawatson', 'deepikapadukone', 'narendramodi', 'nba',
    '9gag', 'marvel', 'willsmith', 'aliaabhatt' , 'jacquelinef143', 'akshaykumar', 'katrinakaif', 'anushkasharma', 'robertdowneyjr', 'chrishemsworth', 'leonardodicaprio', 'ladygaga', 'bts.bighitofficial', 'sunnyleone',
    'tomholland2013', 'milliebobbybrown', 'dishapatani', 'gucci', 'pankajtripathi', 'nawazuddin._siddiqui', 'iamsrk', 'chrisevans', 'hrithikroshan', 'amitabhbachchan', 'lamborghini', 'djsnake']
    userstounfollow = []
    logo()
    username = input("  Enter your Username Or Email Or Phone : ")
    password = input("  Enter your Password : ")
    print("      ")
    print('   Keep Calm and Watch !!!')
    print("      ")
    InstagramBot(username, password)