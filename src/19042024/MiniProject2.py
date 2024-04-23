import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_iDrive():
    driver = webdriver.Chrome()
    # Open url
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()
    
    # Take screenshot
    allure.attach(driver.get_screenshot_as_png(),name="Login_SS",attachment_type=AttachmentType.PNG)
    #Enter Credentials
    username = driver.find_element(By.XPATH,"//input[@id='username']")
    username.send_keys("augtest_040823@idrive.com")
    password = driver.find_element(By.XPATH,"//input[@id='password']")
    password.send_keys("123456")
    time.sleep(5)
    Sign_in_btn = driver.find_element(By.XPATH,"//button[@id='frm-btn']")
    Sign_in_btn.click()
    time.sleep(50)
    
    free_trial = driver.find_element(By.XPATH,"//h5[@class='id-card-title']")
    assert free_trial.text == "Your free trial has expired"
    allure.attach(driver.get_screenshot_as_png(), name="Trial_SS", attachment_type=AttachmentType.PNG)
    print(driver.current_url)
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    
    driver.quit()