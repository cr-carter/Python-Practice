'''
This project was intended as a capstone for the previous web scraping lessons.
This project combined the use of Selenium and Beautiful Soup, and enforced the
knowledge gained of both of these packages.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

zillow_url = 'https://appbrewery.github.io/Zillow-Clone/'
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSe6gTIfKFA1kXRAjAfRy085z2N_lupV9EK8dL7QKXeAs-ZNCg/viewform?usp=header'
driver = webdriver.Firefox()

response = requests.get(zillow_url)
content = response.text
soup = BeautifulSoup(content, 'html.parser')
listings = soup.select('.StyledPropertyCardDataWrapper')

for listing in listings:
    address = listing.find('address', attrs={'data-test': True}).getText().strip()
    try:
        address = address.split('| ')[1]
    except:
        address = address.split(', ')
        address = [address[i] for i in range(1, len(address))]
        address = ' '.join(address)
    price = listing.find('span', attrs={'data-test': 'property-card-price'}).getText().split('/')[0]
    try:
        price = price.split('+')[0]
    except:
        pass
    link = listing.find('a', href=True)['href']

    driver.get(form_url)
    answers = driver.find_elements(By.CSS_SELECTOR, 'input.whsOnd')
    answers[0].click()
    answers[0].send_keys(address)
    answers[1].click()
    answers[1].send_keys(price)
    answers[2].click()
    answers[2].send_keys(link)

    submit = driver.find_element(By.CSS_SELECTOR, '.uArJ5e')
    submit.click()

driver.quit()
