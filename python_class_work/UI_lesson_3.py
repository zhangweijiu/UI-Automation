import time

def open_url(driver, url):
    driver.get(url)
    driver.maximize_window()

def login_func(driver, username, password):
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
    driver.find_element_by_id("btnSubmit").click()

def search_func(driver, url, username, password,key):
    open_url(driver, url)
    login_func(driver, username, password)

    driver.find_element_by_xpath("//span[text()='零售出库']").click() # 点击“零售出库”按键
    time.sleep(2)

    id_li = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id") # 获取iframe的id
    id_frame = id_li + "-frame"
    driver.switch_to.frame(id_frame) #切换到子html页面
    # driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_frame)))
    driver.find_element_by_id(id_frame).send_keys(key) # 在“查询单号”搜索框中键入要查询的内容
    driver.find_element_by_id("searchBtn").click() # 点击“查询”按键
    time.sleep(1)
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']//div").text # 获取查询到的单号的值

    return num