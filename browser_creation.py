import os
import pickle
from multiprocessing import Pool
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from chrome_options_args import chromeOptions_args
from webdriver_manager.chrome import ChromeDriverManager
from chrome_Window_init import starter_driver
from Unfollowers import UnfollowerClass
from path_config import my_path, cookie_path, list_path

my_path = os.path.dirname(os.path.abspath(__file__))
cookie_path = os.path.join(my_path, "resources/cookies.txt")
list_path = os.path.join(my_path, "resources/")


def save_cookie(driver):
    with open(cookie_path, 'wb') as filehandler:
        print(cookie_path)
        pickle.dump(driver.get_cookies(), filehandler)


def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)
    return driver


def create_browser_with_cookies(headless, url):
    if headless == 'n' or headless == 'N':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    else:
        chromeOptions = chromeOptions_args.chromeOptions()
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chromeOptions)
    driver.implicitly_wait(5)
    driver.get('http://www.instagram.com')
    driver = load_cookie(driver, cookie_path)
    driver.get(url)

    return driver


def write_list(num, url, option):
    driver = create_browser_with_cookies(option, url)
    if num == 0:
        UnfollowerClass(driver, 'following')
    else:
        UnfollowerClass(driver, 'followers')


def multi(url, option):
    pool = Pool(processes=2)
    for i in range(2):
        print(i)
        async_result = pool.apply_async(write_list, args=(i, url, option))
#creating diff pools of multi threads
    pool.close()
    pool.join()
