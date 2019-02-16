# 提取http://lab.scrapyd.cn中的五条名言
# 相同作者的名言保存在一个文件中，采用追加的方式写入

import scrapy

# 定义一个spider类，继承Spider父类
class ListSpider(scrapy.Spider):

    # 定义蜘蛛名
    name = 'ListSpider'
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):

        # 提取页面中的所有的名言
        mingyanPage1 = response.css('div.quote')

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
            filename =  '%s-语录.txt' %(author)
            # 以追加的方式写入文件，文件名相同（即作者相同），会写在同一个文件
            with open(filename, "a+") as f:
                f.write(text)
                f.write('\n')
                f.write('标签: ' + tags)
                f.write('\n---------------\n')
                f.close()










