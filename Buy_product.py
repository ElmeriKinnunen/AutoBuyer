from Options import color

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

END = color.DEFAULT
url = input

while url != "exit":
    try:

        url = input ("Enter url: ")
        browser.get(url)
        logging.info("Url entered")

    except Exception as e:
        print(color.HEADER + "Url is missing or not found." + END)
        print(color.ERROR + "ERROR: " + END)
        print(e)

    logging.info("Waking up the bot")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print(color.HEADER + "Start" + END)

    try:

        #add product to the cart while bot is in the product page.

        while browser.current_url != "<enter url from page after the product is succesfully added to cart>":

            try:
                #Currently "add cart" button HTML class need to change manually
                addCart = browser.find_element(By.CLASS_NAME, "site-btn-addToBasket-lg")
                addCart.click()
            except NoSuchElementException:
                pass

            logging.info(color.WARNING + "Product can't add to the cart!" + END)

            browser.refresh()

        logging.info(color.GREEN + color.BLINK + "proruct added succesfully to the cart!" + END)
        
    except Exception as e:
        print(color.HEADER + "Shit hits the fan.." + END)
        print(color.ERROR + "ERROR: " + END)
        print(e)

