import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.negativescenario
@allure.title("Verify Validations for Username field")
@allure.description("Verify error message for Username field when it is empty and click on Submit button")
def test_Error():
    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    driver.maximize_window()
    time.sleep(10)
    
    # switch to frame
    driver.switch_to.frame(driver.find_element(By.ID, "result"))
    
    # Enter details for email
    email = driver.find_element(By.XPATH, "//input[@id='email']")
    email.send_keys("test@test.com")
    
    # Enter details for Password
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys("1234567")
    
    # Enter details for Confirm Password
    conPassword = driver.find_element(By.XPATH, "//input[@id='password2']")
    conPassword.send_keys("1234567")
    
    # Click on submit button
    btn = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    btn.click()
    
    time.sleep(3)
    
    # take screenshot
    allure.attach(driver.get_screenshot_as_png(), name='Error_SS', attachment_type=AttachmentType.PNG)
    
    # find error messsage
    err_msg = driver.find_element(By.XPATH, "//div[@class='form-control error']/child::small")
    assert err_msg.text == "Username must be at least 3 characters"
    
    driver.quit()
