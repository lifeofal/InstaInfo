import os
import pickle

from selenium.common.exceptions import NoSuchElementException
from time import sleep


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
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[3]/a") \
            .click()

        self._get_names("Following", file_name)

        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button") \
            .click()
        print('following search ended')

    def followers(self, file_name):
        print('follower search started')
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a") \
            .click()

        self._get_names("Followers", file_name)

        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button") \
            .click()
        print('follower search ended')

    def _get_names(self, methodName, file_name):
        print("the {} method has called the _get_names method".format(methodName))
        try:

            sugs = self.driver.find_element_by_xpath("//h4[contains(text(), 'Suggestions')]")

            self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        except NoSuchElementException:
            print("No suggestions tab found. Continuing..")

        last_ht, ht = 0, 1
        scroll_box = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        while last_ht != ht:
            last_ht = ht
            sleep(1)

            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)

        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        print(names)

        print('list creation done. Starting pickling to file location')
        listPath = os.path.join(self.list_path, file_name)
        print(listPath)
        with open(listPath, 'wb') as fp:
            pickle.dump(names, fp)
