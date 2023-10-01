#below code is in SELENIUM 4 
from selenium import webdriver
from selenium.webdriver.common.by import By
#executable is optional if write it then it  is treated as key arguement otherwise as positionala arguement
driver=webdriver.Chrome("C:\DRIVERS\chromedriver_win32.zip\chromedriver.exe")
#driver here is object
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("Admin123")
driver.find_element(By.ID,"oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()
act_tittle=driver.tittle
exp_tittle="OrangeHRM"
if act_tittle==exp_tittle:
    print("login test passed")
else:
    print("login test failed")
    
driver.close()