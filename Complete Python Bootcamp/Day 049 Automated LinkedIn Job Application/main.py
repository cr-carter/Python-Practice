'''
The purpose of this project was to gain more experience using selenium. Attention was paid to having a good flow
to ensure that the automated tasks allowed time for pages to load.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv


load_dotenv()
ACCOUNT_EMAIL = os.getenv('LINKEDIN_EMAIL')
ACCOUNT_PASSWORD = os.getenv('LINKEDIN_PASS')
PHONE = os.getenv('PHONE_NUMBER')


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


# Optional - Keep the browser open if the script crashes.
driver = webdriver.Firefox()

driver.get("https://www.linkedin.com/jobs/search/?geoId=101165590&keywords=python%20developer&origin=JOBS_HOME_KEYWORD_AUTOCOMPLETE&refresh=true")

## Click Reject Cookies Button
#time.sleep(2)
#reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
#reject_button.click()

# Click Sign in Button
time.sleep(5)
sign_in_button = driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div/section/div/div/div/div[2]/button")
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="base-sign-in-modal_session_key")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="base-sign-in-modal_session_password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# CAPTCHA
input("Press Enter when you have solved the Captcha")

# Get Listings
time.sleep(5)
easy_apply_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".artdeco-entity-lockup__content")

# Apply for Jobs
for listing in easy_apply_listings:
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CLASS_NAME, value="jobs-apply-button")
        apply_button.click()

        # Insert Phone Number
        time.sleep(2)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
        else:
            # Click Submit Button
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()


time.sleep(2)
driver.quit()
