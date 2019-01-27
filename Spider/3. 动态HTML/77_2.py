# 通过WebDriver操作进行查找
# 无头浏览器，支持无浏览器操作
# 操作Chrome打开百度，并搜索大熊猫，截图搜索结果

from selenium import webdriver
import time

def main():

    # 创建浏览器实例
    driver = webdriver.Chrome()
    url = 'http://www.baidu.com'
    driver.get(url)

    # 打印出wrapper中的文字内容
    text = driver.find_element_by_id('wrapper').text
    print(text)

    # 打印出HTML页面的标题
    print(driver.title)

    # 得到页面的快照，得到百度首页的的截图
    driver.save_screenshot('77_2.png')

    # id='kw'是百度的输入框
    driver.find_element_by_id('kw').send_keys(u'大熊猫')

    # id='su'是百度搜索的按钮，百度一下，click模拟点击
    driver.find_element_by_id('su').click()

    # 搜索需要时间，等待一下再截图
    time.sleep(5)
    driver.save_screenshot('大熊猫搜索结果.png')

    # 清空输入框
    driver.find_element_by_id('kw').clear()

    # 在搜索一个航母
    driver.find_element_by_id('kw').send_keys(u'航母')
    time.sleep(5)
    driver.save_screenshot('航母.png')

    # 关闭浏览器
    driver.close()

if __name__ == '__main__':
    main()




