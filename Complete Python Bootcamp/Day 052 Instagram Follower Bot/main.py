'''
The purpose of this project was to gain more experience using selenium and web scraping.
Detail was given to the flow of the program, utilizing WebDriverWait and expected_conditions
to wait for HTML elements to appear, and using try/except/else arguments to manage HTML interactions.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait

INSTAGRAM_EMAIL = os.getenv('INSTAGRAM_EMAIL')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

driver = webdriver.Firefox()
driver.get('https://www.instagram.com')

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.xdj266r:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')))
email_input = driver.find_element(By.CSS_SELECTOR, 'div.xdj266r:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
email_input.send_keys(INSTAGRAM_EMAIL)

password_input = driver.find_element(By.CSS_SELECTOR, 'div.x1m39q7l:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
password_input.send_keys(INSTAGRAM_PASSWORD)

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._acap')))
login_button = driver.find_element(By.CSS_SELECTOR, '._acap')
login_button.click()

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.x1i10hfl')))
dont_save = driver.find_element(By.CSS_SELECTOR, 'div.x1i10hfl')
dont_save.click()

driver.get('https://www.instagram.com/cybersecuritygirl/')

try:
    followers = driver.find_element(By.CSS_SELECTOR, 'li.xl565be:nth-child(2) > div:nth-child(1) > a:nth-child(1)')
except Exception as error:
    print(f'Could not find followers.\n{error}')
else:
    followers.click()

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.x1dm5mii:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(1)')))
try:
    follower_list = driver.find_elements(By.CSS_SELECTOR, '._acan')
except Exception as error:
    print(f'Could not find new users to follow.\n{error}')
else:
    for i in range(3, len(follower_list)):
        try:
            follower_list[i].click()
        except Exception as error:
            print(f'Error in following account.\n{error}')
