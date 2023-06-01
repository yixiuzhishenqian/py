from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 设置浏览器配置实例
option = webdriver.EdgeOptions()
option.add_experimental_option('detach', True)
# 创建webdriver实例
# edge
driver = webdriver.Edge(options=option)
# 设置浏览器最大化
driver.maximize_window()
# 打开一个浏览器
driver.get('https://www.bilibili.com')
sleep(3)
# driver.quit()
# 获取页面元素
search_input = driver.find_element(By.CLASS_NAME, "nav-search-input")
# 设置内容
search_input.send_keys("雾山五行")
# 获取搜索按钮
search_btn = driver.find_element(By.CSS_SELECTOR, ".nav-search-btn")
# 点击按钮
search_btn.click()
# 切换页面
# 获取所有页面
handlers = driver.window_handles
driver.switch_to.window(handlers[-1])
sleep(5)
# 获取立即观看
picture = driver.find_element(By.CSS_SELECTOR, '[title="【雾山五行】不是吧，这唢呐怎么卡着点燃起来了"]')
picture.click()