from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# 这个位置会报错，但是由于是显式等待，所以会等到最后的10秒钟才会报错
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'btn-search')))
print(input, button)
