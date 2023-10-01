#Github automatic login through selenium 4
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
username="your username"
password="your password"
driver.get("https://github.com/login")
uname=driver.find_element("id","login_field")
uname.send_keys("username")
pword=driver.find_element("id","password")
pword.send_keys("password")
driver.find_element("name","commit").click()
WebDriverWait(driver=driver,timeout=10).until(lambda x:execute_script("returndocument.readyState==='complete'"))
error=driver.find_elements(By.CLASS_NAME,"flash-error")
if any(error_message in e.text for e in errors):
    print("[!] login failed")
else:
    print("[+] login successful")
driver.close()