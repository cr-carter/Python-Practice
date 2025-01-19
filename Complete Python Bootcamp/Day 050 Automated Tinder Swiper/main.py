'''
The purpose of this project was to gain more experience using selenium and web scraping.
Detail was given to the flow of the program, allowing time for web pages to load, and
utilizing webdriver options to switch between windows as neccessary.
'''

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()
ACCOUNT_EMAIL = os.getenv('TINDER_EMAIL')
ACCOUNT_PASSWORD = os.getenv('TINDER_PASSWORD')

# Optional - Keep the browser open if the script crashes.
driver = webdriver.Firefox()
driver.get("https://www.tinder.com")

time.sleep(2)
log_in = driver.find_element(By.LINK_TEXT, 'Log in')
log_in.click()

time.sleep(2)
log_in = driver.find_element(By.CSS_SELECTOR, 'div.My\(12px\):nth-child(2) > button:nth-child(1)')
log_in.click()

time.sleep(3)
handles = driver.window_handles

driver.switch_to.window(handles[1])
time.sleep(1)
email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys(ACCOUNT_EMAIL)
password = driver.find_element(By.ID, 'pass')
password.send_keys(ACCOUNT_PASSWORD)
log_in = driver.find_element(By.NAME, 'login')
log_in.click()

time.sleep(3)
continue_login = driver.find_element(By.CSS_SELECTOR, '.xtk6v10 > span:nth-child(1)')
continue_login.click()

time.sleep(3)
driver.switch_to.window(handles[0])
input("Press enter when you complete the puzzle.")

allow_location = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
allow_location.click()
input("Press enter if popups cleared.")
allow_location = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[2]/div[2]/div[2]/div')

for n in range(100):
    try:
        time.sleep(2)
        like = driver.find_element(By.LINK_TEXT, 'Like')
        like.click()
    except ElementClickInterceptedException:
        try:
            match = driver.find_element(By.CSS_SELECTOR, '.itsAMatch a')
            match.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
