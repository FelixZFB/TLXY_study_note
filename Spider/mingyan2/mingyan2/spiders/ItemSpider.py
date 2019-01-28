# 提取http://lab.scrapyd.cn中的五条名言
# 分别按编号+作者的方式保存为5个文件

import scrapy

# 定义一个mingyan类，继承Spider父类
class ItemSpider(scrapy.Spider):

    # 定义蜘蛛名
    name = 'ItemSpider'
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):

        # 提取页面中的所有的名言
        mingyanPage1 = response.css('div.quote')

        number1 = 0

        for mingyan in mingyanPage1:
            # 提取css中text标签对应的文字内容，名言的正文
            text = mingyan.css('.text::text').extract_first()
            # 提取作者
            author = mingyan.css('.author::text').extract_first()
            # 提取标签
            tags = mingyan.css('.tags .tag::text').extract()
            # 数组转换为字符串
            tags = ', '.join(tags)
            # 将爬去的内容存入文件，文件名为：编号. 作者-语录.txt
            number1 += 1
            filename =  '%s. %s-语录.txt' %(number1, author)
            # 以写的方式打开文件并写入内容
            with open(filename, "w") as f:
                f.write(text)
                f.write('\n')
                f.write('标签: ' + tags)
                f.close()










