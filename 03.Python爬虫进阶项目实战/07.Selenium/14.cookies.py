from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name': 'goular', 'domain': 'http://www.zhihu.com', 'value': 'Germany'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
