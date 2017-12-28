# written by Taylor Huang 
import time
from selenium import webdriver
from datetime import date

username = "yourusername"
password = "yourpassword"


driver=webdriver.Chrome()
driver.get('http://vip.jd.com')


driver.find_element_by_link_text('账户登录').click()
driver.find_element_by_id('loginname').click()
driver.find_element_by_id('loginname').send_keys(username)
driver.find_element_by_id('nloginpwd').click()
driver.find_element_by_id('nloginpwd').send_keys(password)
driver.find_element_by_id('loginsubmit').click()
time.sleep(1)

try:
    driver.find_element_by_id('signIn').click()  #签到领京豆
    print("签到成功！")
except:
    print("签到失败，可能是重复签到了，请检查.")  # 若签到失败，打印错误信息

time.sleep(1)

if date.today().day == 5:
    driver.find_element_by_class_name('gift').click()  #每月5号领取礼包
    print('每月5号领取礼包！')


driver.get("http://datawallet.jd.com/profile.html")
driver.find_element_by_class_name('btn-sign').click()  # 签到领流量
print("领取流量成功！")
print('签到结束！')
driver.quit()  #签到成功，关闭浏览器并安静退出
