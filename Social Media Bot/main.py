# Import necessary modules
import os
import imghdr
from dotenv import load_dotenv
import tweepy
from atproto import Client, client_utils
import datetime
import json
import smtplib
import requests

# Load the .env file and get keys/login for APIs
load_dotenv()

X_CONSUMER_KEY = os.getenv("X_CONSUMER_KEY")
X_CONSUMER_SECRET = os.getenv("X_CONSUMER_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")

BLUESKY_USER = os.getenv("BLUESKY_USER")
BLUESKY_PASS = os.getenv("BLUESKY_PASS")

THREADS_USER_ID = os.getenv("THREADS_USER_ID")
THREADS_ACCESS_TOKEN = os.getenv("THREADS_ACCESS_TOKEN")

EMAIL_ADDR = os.getenv("EMAIL_ADDR")
EMAIL_PASS = os.getenv("EMAIL_PASS")
SEND_EMAIL = os.getenv("SEND_ADDR")


# Function to send me an email if there are errors posting.
def error_report(platform, report):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDR, password=EMAIL_PASS)
        connection.sendmail(from_addr=EMAIL_ADDR,
                            to_addrs=SEND_EMAIL,
                            msg=f"There was an error posting today's quote on {platform}.\n{report}")


# Calculate the number of days since January 1 (Jan 1 is day 0)
d0 = datetime.date(datetime.date.today().year, 1, 1)
d1 = datetime.date.today()
delta = (d1 - d0).days

# Get quote of the day from the quotes.json file, based on number of days since Jan 1
# Use text_builder to properly create tags for Bluesky post. Use string with hashtags
# for X/Twitter post.
with open("quotes.json", "r") as file:
    data = json.load(file)
    quote = f'"{data["quotes"][delta]["quote"]}"\n-{data["quotes"][delta]["author"]}'

if delta % 2 == 0:
    thread_tag = "#motivation"
else:
    thread_tag = "#inspiration"

x_tags = "#Motivation #Inspiration #Quote #Quotes #QuoteOfTheDay #365DaysOfQuotes"

# Connect to X/Twitter, post today's quote. Send me an email for any errors.
try:
    x_client = tweepy.Client(consumer_key=X_CONSUMER_KEY, consumer_secret=X_CONSUMER_SECRET,
                             access_token=X_ACCESS_TOKEN, access_token_secret=X_ACCESS_SECRET)
    response = x_client.create_tweet(text=f'{quote}\n{x_tags}')
    print(response)
except Exception as error:
    error_report("X/Twitter", repr(error))

# Connect to Bluesky, post today's quote. Send me an email for any errors.
bs_client = Client()
profile = bs_client.login(BLUESKY_USER, BLUESKY_PASS)
text_builder = client_utils.TextBuilder()
text_builder.text(f'{quote}\n')
text_builder.tag('#Inspiration', 'Inspiration').text(' ').tag("#Motivation", 'Motivation').text(' ').tag('#Quote',
                                                                                                         'Quote').text(
    ' ')
text_builder.tag('#QuoteOfTheDay', 'QuoteOfTheDay').text(' ').tag('#365DaysOfQuotes', '365DaysOfQuotes')

try:
    profile = bs_client.login(BLUESKY_USER, BLUESKY_PASS)
    response = bs_client.send_post(text=text_builder)
    print(response)
except Exception as error:
    error_report("Bluesky", repr(error))

# The Threads access token lasts 60 days, so every 50 days renew the token.
if delta % 50 == 0:
    try:
        response = requests.get(
            f'https://graph.threads.net/refresh_access_token?grant_type=th_refresh_token&access_token={THREADS_ACCESS_TOKEN}')
        THREADS_ACCESS_TOKEN = response.json()['access_token']
        os.putenv('THREADS_ACCESS_TOKEN', THREADS_ACCESS_TOKEN)
    except Exception as error:
        error_report("Threads", repr(error))

# Connect to Threads, post today's quote. Send me an email for any errors.
post_url = f'https://graph.threads.net/v1.0/{THREADS_USER_ID}/threads'
publish_url = f'https://graph.threads.net/v1.0/{THREADS_USER_ID}/threads_publish'
headers = {
    'Content-Type': 'application/json'
}
post_params = {
    'media_type': 'TEXT',
    'text': f"{quote}\n{thread_tag}",
    'access_token': THREADS_ACCESS_TOKEN
}

try:
    response = requests.post(url=post_url, headers=headers, params=post_params)
    print(response.json())
    media_container = response.json()['id']
    publish_params = {
        'creation_id': media_container,
        'access_token': THREADS_ACCESS_TOKEN
    }
    response = requests.post(url=publish_url, headers=headers, params=publish_params)
    print(response.json())
except Exception as error:
    error_report("Threads", repr(error))# Import necessary modules
