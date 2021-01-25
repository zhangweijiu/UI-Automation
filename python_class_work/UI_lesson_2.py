from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://erp.lemfix.com")
driver.maximize_window()

page_title = driver.title
if page_title =="柠檬ERP":
    print("这个页面的标题:{}".format(page_title))
else:
    print("这个用例不通过!")

driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()
page_name = driver.find_element_by_xpath("//p").text
driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()

# time.sleep(2)
if page_name == "测试用广":
    print("这个登录用户是:{}".format(page_name))
else:
    print("这个用例不通过!")

