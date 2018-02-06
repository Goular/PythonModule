from selenium import webdriver
import time

# 添加key和提交button
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(2)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
# 提交按钮
button.click()