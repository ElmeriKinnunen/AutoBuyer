from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import logging
import Options as opt


def openBrowser():

    browser = webdriver.Firefox()

    logging.info("Browser opened")
    logging.info("Session ID: " + browser.session_id)

    return browser

def checkout(browser):

    checkout = browser.find_element(By.CLASS_NAME, "btn-success")
    checkout.click()

    field = browser.find_element(By.ID, "Name").send_keys("etunimi sukunimi")
    field = browser.find_element(By.ID, "Address1").send_keys("testitie 4")
    field = browser.find_element(By.ID, "ZipCode").send_keys("00100")
    field = browser.find_element(By.ID, "City").send_keys("Helsinki")
    field = browser.find_element(By.ID, "CountryCode").send_keys("Suomi")
    field = browser.find_element(By.ID, "Phone").send_keys("0402340000")
    field = browser.find_element(By.ID, "AnonymousUser_Email").send_keys("testi.testi@gmail.com")
    field = browser.find_element(By.ID, "AnonymousUser_ConfirmEmail").send_keys("testi.testi@gmail.com")

    next = browser.find_element(By.CLASS_NAME, "input__login")
    next.submit()

    time.sleep(0.5)

    terms = browser.find_element(By.ID, "traidConditionsAnswer")
    terms.click()

    delivery = browser.find_element(By.CLASS_NAME, "btn-success")
    delivery.click()
    
    logging.info(opt.color.GREEN + opt.color.BLINK + "product succesfully ordered! (almost, only payment method missing)" + opt.color.DEFAULT)