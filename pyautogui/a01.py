#1)open web browser(chrome/firefox/edge)
#2)open url https://opensource-demo.orangehrmlive.com/
#3)enter username(Admin)
#4)enter password(admin123)
#5)click on login
#6)capture tittle of the home page.(actual title)
#7)verify tittle of the page:OrangeHRM (Expected)
#8)close browser
#below code is wriitten in selenium 3 but we have install selenium 4
from selenium import webdriver
#executable is optional if write it then it  is treated as key arguement otherwise as positionala arguement
driver=webdriver.Chrome("C:\DRIVERS\chromedriver_win32.zip\chromedriver.exe")
#driver here is object
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_elements_by_name("username").send_keys("Admin")
driver.find_elements_by_placeholder("Password").send_keys("Admin123")
driver.find_elements_by_id("oxd-button oxd-button--medium oxd-button--main orangehrm-login-button")
act_tittle=driver.tittle
exp_tittle="/web/images/orangehrm-logo.png?1672659722816"
if act_tittle==exp_tittle:
    print("login test passed")
else:
    print("login test failed")
    
driver.close()