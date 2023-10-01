from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element("q").send_keys("javapoint")
time.sleep(3)
driver.find_elements("btnK").send_keys(Keys.ENTER)