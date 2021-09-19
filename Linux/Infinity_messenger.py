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
        self.driver=webdriver.Firefox()
        self.login()
        
    def login(self):
        self.driver.get('https://www.instagram.com')
        sleep(2)
        #Login
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input"))).send_keys(self.username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(self.password)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(Keys.ENTER)
        sleep(4)

        #Go to Target Profile
        self.driver.get('https://www.instagram.com/' + target)
        sleep(2)

        #Follow Target
        try:
            WebDriverWait(self.driver,3).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Follow')]"))).click()
        except:
            print(target + " is followed by you!")

        #Go to Inbox
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "sqdOP.L3NKy._8A5w5    "))).click()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

        #Now Sending Messages       
        for x in range(int(times)):
           WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea"))).send_keys(message,Keys.ENTER)          


        sleep(3)


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
    logo()
    username = input("  Enter your Username Or Email Or Phone : ")
    password = input("  Enter your Password : ")
    target = input("  Enter Target username : ")
    message = input("  Enter the message you want to send : ")
    times = input("  How many times to send the message : ")
    print("      ")
    print('   Keep Calm and Watch !!!')
    print("      ")
    InstagramBot(username, password)

