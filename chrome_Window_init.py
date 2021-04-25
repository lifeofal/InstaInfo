from secrets import pw
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from chrome_options_args import chromeOptions_args
from webdriver_manager.chrome import ChromeDriverManager

class InstaBot:


    def __init__(self, user, pw):
        self.user = user
        self.chrome_options = chromeOptions_args

        print("Would you like to run this in headless? (y/n)")
        answer = input()

        #
        #Initiate the headless or webbrowser run
        #

        if answer == 'n' or answer == 'N':
            try:
                self.driver = webdriver.Chrome()
            except Exception:
                print("Default webdriver not found. Switching to path")
                self.driver = webdriver.Chrome(ChromeDriverManager().install())
        else:
            try:
                self.driver = webdriver.Chrome(options=self.chrome_options)
            except Exception:
                print("Default webdriver not found. Switching to path")
                self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options)



        #
        #Try catch for if Log in or Verification code pop up fails
        #
        try:
            self.driver.get("https://instagram.com")
            self.agent = self.driver.execute_script("return navigator.userAgent")
            #print(self.agent)
            #self.driver.get_screenshot_as_file("errorcapture1.png")
            self.driver.implicitly_wait(5)


            try:
                self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
                    .send_keys(user)
            except Exception:
                print("xpath Element not found with \"//input[@name=\"username\"]\"")
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
            #self.driver.find_element_by_xpath("//input[@name=\"username\"]")

            self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
                .send_keys(pw)

            self.driver.find_element_by_xpath("//button[@type=\"submit\"]") \
                .click()


            try:
                self.driver.find_element_by_xpath("//input[@name=\"verificationCode\"]").send_keys()

                self.driver.find_element_by_xpath("//button[contains(text(),'Confirm')]").click()



                self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()



            except NoSuchElementException:
                print("Verification pop up did not appear. Continuing..")

                pass
        except Exception:
            print("Error occured in \'Log in\' phase. Capturing screenshot of page")
            self.driver.get_screenshot_as_file("LogInError.png")
            exit()
        print("Log In complete.. Running after_Log")
        self.after_Log()



    def after_Log(self):
        try:


            try:
                self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()

            except Exception:
                print("\'Save info\' page not found. Continuing.. ")
                pass
            try:
                self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()

            except Exception:
                print("\'Notification pop up\' not found. Continuing.. ")
                pass

            try:
                self.driver.find_element_by_xpath("//a[contains(@href, '/{}/')]".format(self.user)) \
                    .click()

            except NoSuchElementException:
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img') \
                    .click()


                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div') \
                    .click()

        except Exception:
            print("Error occurred in \'After Log\' phase. Capturing screenshot of page")
            self.driver.get_screenshot_as_file("AfterLogError.png")
            exit()
