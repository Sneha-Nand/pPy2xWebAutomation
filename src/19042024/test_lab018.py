from allure_commons.types import AttachmentType
from selenium import webdriver
import time
import pytest
import allure
import logging

from selenium.webdriver.common.by import By


@pytest.mark.smoke
@allure.title("Verify that Login is working in Cura website")
@allure.description("TC#1 - Simple Login check on Cura")
def test_open_website():
    
    driver = webdriver.Chrome()
    # Open the url
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    
    #clcik on Make appointment button using link text works only with anchor teext
    # By.Link Test - exact or full match
    # if there are two elements with same link texet it will return first onre
    
    element = driver.find_element(By.LINK_TEXT,"Make Appointment")
    element.click()
    time.sleep(10)
    
    #Verify url Changes
    print(driver.current_url)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login" , "Assertion Fail message - Error matching URL "
    
    allure.attach(driver.get_screenshot_as_png(), name="Login-Screenshot", attachment_type=AttachmentType.PNG)
    
    #Enter Credentials and clcik on Login button
    username = driver.find_element(By.NAME,"username")
    username.send_keys("John Doe")
    password = driver.find_element(By.ID,"txt-password")
    password.send_keys("ThisIsNotAPassword")
    Loginbtn = driver.find_element(By.ID,"btn-login")
    Loginbtn.click()
    
    
    
    allure.attach(driver.get_screenshot_as_png(),name="Appointment-Screenshot",attachment_type=AttachmentType.PNG)
    #Verify Make appointment text on the web page
    verify_Make_Appnt = driver.find_element(By.XPATH,"//div//h2")
    assert verify_Make_Appnt.text == "Make Appointment"
    time.sleep(20)
    driver.quit()
    