from selenium import webdriver

'''
driver = webdriver.Firefox()   # Firefox浏览器

driver = webdriver.Chrome()    # Chrome浏览器

driver = webdriver.Ie()        # Internet Explorer浏览器

driver = webdriver.Edge()      # Edge浏览器

driver = webdriver.Opera()     # Opera浏览器

driver = webdriver.PhantomJS()   # PhantomJS
'''

driver = webdriver.Opera ()
driver.get ('https://www.baidu.com')
print (driver.title)
driver.quit ()
