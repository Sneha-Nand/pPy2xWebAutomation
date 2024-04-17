from selenium import webdriver
import time
import pytest
import logging


@pytest.mark.smoke
def test_open_website():
    
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    driver.back()
    driver.forward()
    driver.refresh()