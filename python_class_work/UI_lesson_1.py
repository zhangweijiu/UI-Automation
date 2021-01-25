from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.maximize_window()
time.sleep(2)
driver.get("http://taobao.com")
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()

