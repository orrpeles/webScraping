#!/bin/python
# log into reddit with selenium

import selenium
from selenium import webdriver
import getpass # keep passpord safe

pswd = getpass.getpass('Password:') # reddit password passed to pswd obj

browser = webdriver.Firefox()
browser.get('https://www.reddit.com/login/?')
loginElem = browser.find_element_by_id('loginUsername')
loginElem.send_keys('orrpel')
passElem = browser.find_element_by_id('loginPassword')
passElem.send_keys(pswd) #pswd obj called
passElem.submit()

