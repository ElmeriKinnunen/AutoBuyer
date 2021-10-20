import time
import sys
import logging
#import validators

import Actions as action
import Options as opt

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

color = opt.color
END = color.DEFAULT
command = input

browser = action.openBrowser()


while command != "exit":
    try:
        command = input ("Enter url/exit: ")
        browser.get(command) #set url to browser
        logging.info("Url entered")

    except Exception as e:
        if command == "exit":
            print("Exiting from bot..")
            sys.exit(1)
        else:
            print(color.HEADER + "Url is missing or url type is wrong" + END)
            print(color.ERROR + "ERROR: " + END)
            print(e)
            sys.exit(1)


    logging.info("Waking up the bot")
    time.sleep(1)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    print(color.HEADER + "Start" + END)

    try:

        #add product to the cart while bot is in the product page.

        while browser.current_url != "<url>":

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

    try:

        command = input ("Check your browser! Is the product correct? yes/no : ")
        
        if command != "yes":
            print("Exiting from bot..")
            sys.exit(1)
        else:
            action.checkout(browser)

    except Exception as e:
        print(color.HEADER + "Shit hits the fan.." + END)
        print(color.ERROR + "ERROR: " + END)
        print(e)

