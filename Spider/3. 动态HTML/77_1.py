# 通过WebDriver操作进行查找
# 无头浏览器，支持无浏览器操作

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def main():
    # 设置无界面浏览器
    options = Options()
    options.add_argument('-headless')

    # 创建一个实例无界面浏览器实例
    driver = webdriver.Firefox(options=options)
    driver.get('http://www.baidu.com')
    print("Title: {0}".format(driver.title))

    # 关闭浏览器
    driver.close()

if __name__ == '__main__':
    main()