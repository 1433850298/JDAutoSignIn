import time
from selenium import webdriver
username = "yourusername"
password = "yourpassword"

driver=webdriver.Chrome()
driver.get('http://vip.jd.com')
time.sleep(1)


driver.find_element_by_link_text('账户登录').click()
driver.find_element_by_id('loginname').click()
driver.find_element_by_id('loginname').send_keys(username)
driver.find_element_by_id('nloginpwd').click()
driver.find_element_by_id('nloginpwd').send_keys(password)
driver.find_element_by_id('loginsubmit').click()
time.sleep(1)
driver.find_element_by_id('signIn').click()

driver.close()
