import os
import pickle

from selenium.common.exceptions import NoSuchElementException
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class UnfollowerClass:

    def __init__(self, objectDriver, path):
        self.driver = objectDriver
        self.my_path = os.path.dirname(os.path.abspath(__file__))

        self.list_path = os.path.join(self.my_path, "resources")
        if path == 'following':
            self.following('following_list.txt')
        else:
            self.followers('followers_list.txt')

    def following(self, file_name):
        print('following search started')
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a") \
            .click()

        self._get_names("Following", file_name)

        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()
        # self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[2]/button") \
        #     .click()
        print('following search ended')

    def followers(self, file_name):
        print('follower search started')
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a") \
            .click()

        self._get_names("Followers", file_name)
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()

        # self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[2]/button") \
        #     .click()
        print('follower search ended')

    def _get_names(self, methodName, file_name):
        print("the {} method has called the _get_names method".format(methodName))
        try:
            suggestion = self.driver.find_element(By.XPATH, "//h4[contains(text(), 'Suggestions')]")

            self.driver.execute_script('arguments[0].scrollIntoView()', suggestion)
        except NoSuchElementException:
            print("No suggestions tab found. Continuing..")

        last_ht, ht = 0, 1
        try:
            if methodName == "Followers":
                scroll_box = self.driver.find_element(By.XPATH,
                    "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
            else:
                scroll_box = self.driver.find_element(By.XPATH,
                    "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        except NoSuchElementException:
            print('No scroll found')

        while last_ht != ht:
            last_ht = ht
            sleep(3)

            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)

        sleep(10)
        links = scroll_box.find_elements(By.TAG_NAME, 'a')
        print(len(links))
        names = [name.text for name in links if name.text != '']

        print('{} {}: {}'.format(methodName, len(names), names))

        print('list creation done. Starting pickling to file location')
        listPath = os.path.join(self.list_path, file_name)
        print(listPath)
        with open(listPath, 'wb') as fp:
            pickle.dump(names, fp)
