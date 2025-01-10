'''
The purpose of this project was to gain further experience with selenium. This project (and lesson in Udemy)
focused on using selenium to input text and click on objects within a webpage.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get('https://orteil.dashnet.org//experiments/cookie/')
cookie = driver.find_element(By.ID, 'cookie')

timeout = 5
while True:
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        cookie.click()
    money = int(driver.find_element(By.ID, 'money').text)
    upgrades = {
                'time_machine': {'cost': driver.find_element(By.CSS_SELECTOR, '#buyTime\ machine > b:nth-child(1)').text.split(' - ')[1].replace(',',''),
                                 'button': driver.find_element(By.ID, 'buyTime\ machine')},
                'portal': {'cost': driver.find_element(By.CSS_SELECTOR, '#buyPortal > b:nth-child(1)').text.split(' - ')[1].replace(',',''),
                           'button': driver.find_element(By.ID, 'buyPortal')},
                'alchemy_lab': {'cost': driver.find_element(By.CSS_SELECTOR, '#buyAlchemy\ lab > b:nth-child(1)').text.split(' - ')[1].replace(',',''),
                                'button': driver.find_element(By.ID, 'buyAlchemy\ lab')},
                'shipment': {'cost': driver.find_element(By.CSS_SELECTOR, '#buyShipment > b:nth-child(1)').text.split(' - ')[1].replace(',',''),
                             'button': driver.find_element(By.ID, 'buyShipment')},
                'mine': {'cost': driver.find_element(By.CSS_SELECTOR, '#buyMine > b:nth-child(1)').text.split(' - ')[1].replace(',',''),
                         'button': driver.find_element(By.ID, 'buyMine')},
                'factory': {'cost': driver.find_element(By.CSS_SELECTOR, '#buyFactory > b:nth-child(1)').text.split(' - ')[1],
                            'button': driver.find_element(By.ID, 'buyFactory')},
                'grandma': {'cost': driver.find_element(By.CSS_SELECTOR, '#buyGrandma > b:nth-child(1)').text.split(' - ')[1],
                            'button': driver.find_element(By.ID, 'buyGrandma')},
                'cursor': {'cost': driver.find_element(By.CSS_SELECTOR, '#buyCursor > b:nth-child(1)').text.split(' - ')[1],
                           'button': driver.find_element(By.ID, 'buyCursor')},
                }
    for upgrade in upgrades:
        if money > int(upgrades[upgrade]['cost']):
            upgrades[upgrade]['button'].click()
#driver.quit()
