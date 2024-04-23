from selenium import webdriver
import time
import pytest
import logging

from selenium.webdriver.common.by import By


def test_open_vwologin_negative():
    driver = webdriver.Chrome()
    # Open URL
    driver.get("https://app.vwo.com")
    
    #Enter username and Password
    email_address_element = driver.find_element(By.NAME,"username")
    email_address_element.send_keys("admin")
    time.sleep(30)
    password_ele = driver.find_element(By.NAME,"password")
    password_ele.send_keys("admin")
    
    sign_in_btn = driver.find_element(By.ID,"js-login-btn")
    sign_in_btn.click()
    time.sleep(5)
    error_msg_1 = driver.find_element(By.ID,"js-notification-box-msg")
    assert error_msg_1.text == "Your email, password, IP address or location did not match"
    
    
    
