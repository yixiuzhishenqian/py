from selenium import webdriver
from time import sleep

# 创建WebDriver对象
# 如果把驱动放置到了 系统环境变量目录中，可不带参数创建
# driver = webdriver.Chrome()
driver = webdriver.Edge()
# 如果没有放置到系统环境变量目录中，需要通过参数指定
# driver= webdriver.Chrome(executable_path="./chromedriver.exe")
url = 'https://www.baidu.com'
# 使用浏览器打开指定页面
driver.get(url)
sleep(3)
# 关闭浏览器
sleep(3)
driver.quit()
