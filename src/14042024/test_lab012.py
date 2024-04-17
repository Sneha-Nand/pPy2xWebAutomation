from selenium import webdriver
import time
import pytest
import logging


@pytest.mark.smoke
def test_open_website():
    
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    time.sleep(10) # here python interpreter waits for 10 n0t webdriver
    driver.get("https://www.google.com")
    # this basically acts like a navigation command