# 通过WebDriver操作进行查找

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def main():
    options = Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.baidu.com")
    print(driver.page_source)
    driver.close()


if __name__ == '__main__':
    main()

