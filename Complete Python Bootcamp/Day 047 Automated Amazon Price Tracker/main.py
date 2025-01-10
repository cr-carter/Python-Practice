'''
The purpose of this project was to continue using BeautifulSoup to enforce
the understanding and skills of web scraping. The importance of headers was 
emphasized. This project also incorporated previous lessons of using smtplib
to connect to and send emails from an email account.
'''


from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
email = os.getenv('EMAIL_ADDRESS')
email_password = os.getenv('EMAIL_PASSWORD')

url = 'https://www.amazon.com/dp/B075CYMYK6?psc=1'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
    'Accept-Language': 'en-US,en;q=0.5'
}

response = requests.get(url=url, headers=headers)
content = response.text
try:
    soup = BeautifulSoup(content, 'html.parser')
    price = soup.select_one('.aok-offscreen').getText().replace('$','').strip()
    item = soup.select_one('productTitle').getText().strip()
except Exception as error:
    connection = smtplib.SMTP(os.getenv("SMTP_ADDRESS"), port=587)
    with connection:
        connection.starttls()
        connection.login(email, email_password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f'Subject:Issue searching for Amazon deals\n\n{error}'
       )
else:
    connection = smtplib.SMTP(os.getenv("SMTP_ADDRESS"), port=587)
    with connection:
       connection.starttls()
       connection.login(email, email_password)
       connection.sendmail(
           from_addr=email,
           to_addrs=email,
           msg=f'Subject:Deal Found!\n\n{item}\nNow only {price}!\n{url}'
       )
