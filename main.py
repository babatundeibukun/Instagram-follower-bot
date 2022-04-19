from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException

EMAIL = 'YOUR_EMAIL'
PASSWORD = 'YOUR_PASSWORD '
SIMILAR_ACCOUNT = 'bellabookss'
chrome_driver_path = "C:\\Users\\Hp EliteBook\\Desktop\\chrome Driver\\chromedriver.exe"


class InstaFollower:
    def __init__(self, chrome_driver_path):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get(f'https://instagram.com/{SIMILAR_ACCOUNT}/')
        time.sleep(5)
        log_in_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div['
                                                          '3]/div/span/a[1]/button/div')
        log_in_button.click()
        time.sleep(5)
        email_login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_login.send_keys(EMAIL)
        time.sleep(5)
        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        save_info_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        save_info_button.click()
        time.sleep(10)
        followers_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')
        followers_button.click()
        time.sleep(5)
        elements_in_popup = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", elements_in_popup)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_class_name('wo9IH button')
        try:
            follow_buttons = [print("followed") for button in all_buttons]
            for buttons in all_buttons:
                buttons.click()
                time.sleep(3)
        except ElementClickInterceptedException:
            cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
            cancel_button.click()


bot = InstaFollower(chrome_driver_path)
bot.login()
bot.find_followers()
bot.follow()
