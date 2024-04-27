from selenium import webdriver
import time

def test_open_website():
    driver = webdriver.Chrome() # create a session - w3 new session  post req
    driver.get('https://www.google.com/')
    time.sleep(10)
    
    # open chrome brower is automaticaly closed if there is no command