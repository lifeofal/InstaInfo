from Non_Followers import non_followers
from browser_creation import save_cookie, multi
from chrome_Window_init import starter_driver
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
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
    InstaInfo does not save your username and we will never ask you for log in credentials such as passwords or emails.
    InstaInfo is also not responsible for your account.
    """)
    user = input("Username: ")
    #pw = input("Password: ")

    #answer = int(input())

    print("""
    Would you like to run in Headless mode? (y/n)
    
    
    
    """)

    headless = input()
    #-----Create Starter Driver -----
    url = 'http://www.instagram.com/{}'.format(user)
    login_user = os.getenv('USER')
    login_pass = os.getenv('PASSWORD')
    d1 = starter_driver(login_user,login_pass,headless)


    save_cookie(d1.driver)
    print('Closing initial driver')
    d1.driver.close()
    multi(url,headless)



if __name__ == '__main__':
    main()
    non_followers()


