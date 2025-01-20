'''
The purpose of this project was to gain more experience using selenium and web scraping.
Detail was given to the flow of the program, allowing time for web pages to load.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

class InternetSpeedTwitterBot:
    def __init__(self):
        load_dotenv()
        self.ACCOUNT_EMAIL = os.getenv('TWITTER_EMAIL')
        self.ACCOUNT_PASSWORD = os.getenv('TWITTER_PASSWORD')

        self.PROMISED_DOWNLOAD = 300
        self.PROMISED_UPLOAD = 100
        self.download_speed = 0
        self.upload_speed = 0

        self.driver = webdriver.Firefox()

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net')

        start = self.driver.find_element(By.CLASS_NAME, 'js-start-test')
        start.click()

        time.sleep(45)
        self.download_speed = self.driver.find_element(By.CLASS_NAME, 'download-speed').text
        self.upload_speed = self.driver.find_element(By.CLASS_NAME, 'upload-speed').text
        self.driver.close()

    def tweet_at_provider(self):
        self.driver.get('https://www.x.com/login')
        time.sleep(5)
        input_username = self.driver.find_element(By.CLASS_NAME, 'r-30o5oe')
        input_username.send_keys(self.ACCOUNT_EMAIL)
        next_button = self.driver.find_element(By.CSS_SELECTOR, 'button.css-175oi2r:nth-child(6) > div:nth-child(1)')
        next_button.click()
        time.sleep(5)
        input_username = self.driver.find_element(By.CLASS_NAME, 'r-30o5oe')
        input_username.send_keys(self.ACCOUNT_EMAIL.split('@')[0])
        next_button = self.driver.find_element(By.CSS_SELECTOR, '.r-19yznuf > div:nth-child(1)')
        next_button.click()
        time.sleep(5)
        input_password = self.driver.find_element(By.CLASS_NAME, 'r-homxoj')
        input_password.send_keys(self.ACCOUNT_PASSWORD)
        next_button = self.driver.find_element(By.CSS_SELECTOR, '.r-19yznuf > div:nth-child(1)')
        next_button.click()

        time.sleep(5)
        if self.download_speed < 0.9 * self.PROMISED_DOWNLOAD or self.upload_speed < 0.9 * self.PROMISED_UPLOAD:
            tweet = (f'Hey @Comcast, why is my internet speed {self.download_speed}down/{self.upload_speed}up when '
                     f'I pay for {self.PROMISED_DOWNLOAD}down/{self.PROMISED_UPLOAD}up?')
        else:
            tweet = (f'Hey @Comcast, my internet speed {self.download_speed}down/{self.upload_speed}up, '
                     f'I pay for {self.PROMISED_DOWNLOAD}down/{self.PROMISED_UPLOAD}up. Keep up the good work!')
        tweet_input = self.driver.find_element(By.CSS_SELECTOR, '.notranslate')
        tweet_input.click()
        tweet_input.send_keys(str(tweet))

        time.sleep(5)
        tweet_send = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        tweet_send.click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
