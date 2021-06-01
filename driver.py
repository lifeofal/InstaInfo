import os
import pickle
import sys
from multiprocessing import Pool
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from browser_creation import save_cookie, multi
from chrome_options_args import chromeOptions_args
from webdriver_manager.chrome import ChromeDriverManager
from chrome_Window_init import starter_driver
from Unfollowers import UnfollowerClass
from Non_Followers import non_followers


def main():
    #----------------------------------------------------------------------------------#
    #   Driver to initialize starter window. User will have menu to choose different
    #   info retrieval actions. Actions like Follower/Following comparison will run in
    #   multiprocessing module.
    #
    #
    #Created by Alejandro Cervantes (4/25/2021)
    #----------------------------------------------------------------------------------#

    print("Welcome to InstaInfo")

    # ----------User Menu---------#

    print("""
     ______  __    __   ______  ________   ______   ______  __    __  ________   ______  
    |      \|  \  |  \ /      \|        \ /      \ |      \|  \  |  \|        \ /      \ 
     \$$$$$$| $$\ | $$|  $$$$$$|\$$$$$$$$|  $$$$$$\ \$$$$$$| $$\ | $$| $$$$$$$$|  $$$$$$|
      | $$  | $$$\| $$| $$___\$$  | $$   | $$__| $$  | $$  | $$$\| $$| $$__    | $$  | $$
      | $$  | $$$$\ $$ \$$    \   | $$   | $$    $$  | $$  | $$$$\ $$| $$  \   | $$  | $$
      | $$  | $$\$$ $$ _\$$$$$$\  | $$   | $$$$$$$$  | $$  | $$\$$ $$| $$$$$   | $$  | $$
     _| $$_ | $$ \$$$$|  \__| $$  | $$   | $$  | $$ _| $$_ | $$ \$$$$| $$      | $$__/ $$
    |   $$ \| $$  \$$$ \$$    $$  | $$   | $$  | $$|   $$ \| $$  \$$$| $$       \$$    $$
     \$$$$$$ \$$   \$$  \$$$$$$    \$$    \$$   \$$ \$$$$$$ \$$   \$$ \$$        \$$$$$$ 
    
     Created by Alejandro Cervantes
    
    -----------------------------------------------------------------------------------------
    """)

    print("""
    
    Enter Credentials
    
                    Disclaimer: 
    InstaInfo does not save you username or password.
    InstaInfo is also not responsible for your account.
    """)
    user = input("Username: ")
    pw = input("Password: ")

    answer = int(input())

    print("""
    Would you like to run in Headless mode? (y/n)
    
    
    
    """)

    headless = input()
    #-----Create Starter Driver -----
    url = 'http://www.instagram.com/{}'.format(user)
    d1 = starter_driver(user,pw,headless)


    save_cookie(d1.driver)
    print('Closing initial driver')
    d1.driver.close()
    multi(url,headless)



if __name__ == '__main__':
    main()
    non_followers()


