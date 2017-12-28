# written by Taylor Huang 
import time
from selenium import webdriver
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
    time.sleep(1)
    driver.find_element_by_class_name('gift').click()  #领取礼包
    driver.get("http://datawallet.jd.com/profile.html")
    driver.find_element_by_class_name('btn-sign').click()  # 签到领流量
    print("领取流量成功！")
    driver.quit()  #若签到成功，关闭浏览器并安静退出
except:
    print("签到失败，请检查.")  #若签到失败，打印错误信息
    driver.close()  #关闭浏览器，但保留命令行，提示用户检查错误的原因
