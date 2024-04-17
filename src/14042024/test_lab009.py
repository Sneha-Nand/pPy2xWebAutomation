from selenium import webdriver
import time
import pytest
import logging


@pytest.mark.smoke
def test_open_website():
    # LOGGER = logging.getLogger(name)
    driver = webdriver.Chrome()
    # when we type this command new session id is created
    # unique 16 digit id
    # fresh copy of browser is created
    # open new tabs , open url, those will be different from normal browsers
    # for Automation
    # when the browser is closed everything is deleted
    
    # create a session - w3 new session  post req only open browser
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    print(driver.title)
    # print(driver.page_source)
    print(driver.session_id)
    assert driver.title == "Login - VWO"
    time.sleep(10)
    driver.close() # close current tab - session id is not null
    driver.quit() # close all windows - session id is null
    # open chrome brower is automaticaly closed if there is no command

# pytest -s src\12022024\test_lab005.py --alluredir=allure-results - run from command promt

# -s is basically used to print the messages

# we can explore rest other comments as well
