from selenium.common.exceptions import NoSuchElementException
from time import sleep

class UnfollowerClass:

    def __init__(self, objectDriver, path):
        self.driver = objectDriver
        if(path == 'following'):
            self.following()
        else:
            self.followers()

    def following(self):
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[3]/a") \
            .click()

        self.following_names = self._get_names("Following")

        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button") \
            .click()
        print('returning list')
        return self.following_names

    def followers(self):

        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a") \
            .click()

        self.followers_names = self._get_names("Followers")

        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button") \
            .click()
        print('returning list')
        return self.followers_names

    def _get_names(self, methodName):
        print("the {} method has called the _get_names method".format(methodName))
        try:

            sugs = self.driver.find_element_by_xpath("//h4[contains(text(), 'Suggestions')]")

            self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        except NoSuchElementException:
            print("No suggestions tab found. Continuing..")




        last_ht, ht = 0, 1
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
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
        return names