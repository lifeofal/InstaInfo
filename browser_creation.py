import os
import pickle
from multiprocessing import Pool
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from chrome_options_args import chromeOptions_args
from webdriver_manager.chrome import ChromeDriverManager
from chrome_Window_init import starter_driver
from Unfollowers import UnfollowerClass

my_path = os.path.dirname(os.path.abspath(__file__))
cookie_path = os.path.join(my_path, "resources\\cookies.txt")
list_path = os.path.join(my_path, "resources\\")

def save_cookie(driver):
    with open(cookie_path, 'wb') as filehandler:
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

def write_list(num,url):
    driver = create_browser_with_cookies('n', url)
    if (num == 0):
        flist = UnfollowerClass(driver, 'following')
        file_name = 'following_list.txt'

    else:
        flist = UnfollowerClass(driver, 'followers')
        file_name = 'followers_list.txt'
    print('list creation done')
    with open(os.path.join(list_path, file_name), 'w') as fp:
        pickle.dump(flist, fp)


def multi(url):
    pool = Pool(processes=2)
    for i in range(2):
        print(i)
        async_result = pool.apply_async(write_list, args=(i,url))

    pool.close()
    pool.join()