# 面向对象-设计模式
# 1. 请求拿到整体网站数据
# 2. 抽取们想要的数据 图片标题和图片链接
# 3. 请求下载图片，建立图片文件名
# 4. 保存图片

import requests
from lxml import etree

class Spider(object):


    # 请求链接，提取图片标题和图片链接
    def start_request(self):
        # 1. 请求拿到整体网站的数据
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2854.400',
        }
        url = 'https://www.mzitu.com/zipai/'
        res = requests.get(url=url, headers=headers)
        html = etree.HTML(res.text)
        # 2. 抽取我们要的数据 图片标题和图片链接
        # 图片标题，就是img lazy alt属性的值
        alt_list = html.xpath("//img[@class='lazy']/@alt")
        # 图片链接，就是img lazy data-original属性的值
        src_list = html.xpath("//img[@class='lazy']/@data-original")

        for alt, src in zip(alt_list, src_list):
            self.down_jpg(alt, src)

    # 定义一个下载图片的方法
    def down_jpg(self, alt, src):
        # 3. 请求下载图片，建立图片文件名
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2854.400',
        }
        content = requests.get(src, headers=headers).content #获得图片的二进制数据
        print(id(content))
        file_name = '图片-' + '.jpg'
        print("正在保存图片: " + file_name)
        # 4. 保存图片,图片二进制数据写入图片
        with open(file_name, 'wb') as f:
            f.write(content)


spider = Spider()
spider.start_request()



