from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.chrome(ChromeDriverManager().install())
print("test cases started")
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_namr("q").send_keys("HARMAN")
time.sleep(2)
driver.find_element_by_namr("btnK").send_keys(Keys.ENTER)
time.sleep(10)
driver.close()
print("testcase completed")