from selenium import webdriver
import time
import pytest
import logging

from selenium.webdriver.common.by import By


#@pytest.mark.smoke
def test_open_website():
    
    driver = webdriver.Chrome()
    # Open the url
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    
    #clcik on Make appointment button using link text works only with anchor teext
    # By.Link Test - exact or full match
    # if there are two elements with same link texet it will return first onre
    
    # element = driver.find_element(By.LINK_TEXT,"Make Appointment")
    # element.click()
    # time.sleep(10)
    
    # Partial text
    # works with anchor
    # partial match
    # PARTIAL_LINK_TEXT
    # it works with appointment, make, make appointment , app, ment, contains keyword
    
    # element1 = driver.find_element(By.PARTIAL_LINK_TEXT,"Make")
    # element1.click()
    # time.sleep(5)
    
    # By. TagName
    element_list = driver.find_elements(By.TAG_NAME, "a")
    make_appt_btn = element_list[5]
    make_appt_btn.click()
    time.sleep(5)
    
    
    # #Verify url Changes
    # # assert
    # assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    # print(driver.current_url)
    #
    # # Enter Credentials and clcik on Login button
    # username = driver.find_element(By.ID,"txt-username")
    # username.send_keys("John Doe")
    # password = driver.find_element(By.ID,"txt-password")
    # password.send_keys("ThisIsNotAPassword")
    # Loginbtn = driver.find_element(By.ID,"btn-login")
    # Loginbtn.click()
    #
    # # Verify Make appointment text on the web page
    # verify_Make_Appnt = driver.find_element(By.XPATH,"//div//h2")
    # assert verify_Make_Appnt.text == "Make Appointment"
    # time.sleep(20)
    