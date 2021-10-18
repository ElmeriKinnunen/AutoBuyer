from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

browser = webdriver.Firefox()
logging.info("Browser opened")

try:

    url = input ("Enter url: ")
    browser.get(url)
    logging.info("Url entered")

except Exception as e:
    print("Url is missing or not found.")
    print("ERROR: ")
    print(e)

#time.sleep(3)

try:

    while browser.current_url == (browser): #add product to the cart while bot is in the product page
        try:
            addCart = browser.find_element(By.CLASS_NAME, "site-btn-addToBasket-lg") #Currently "add cart" button class need to change manually
            addCart.click()
        except NoSuchElementException:
            pass
        logging.info("Product can't add to the cart!")

    logging.info("proruct added to cart!")
    
except Exception as e:
    print("Can't add product to the cart.")
    print("ERROR: ")
    print(e)

