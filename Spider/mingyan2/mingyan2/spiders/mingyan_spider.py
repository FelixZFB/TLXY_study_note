import scrapy

# 定义一个mingyan类，继承Spider父类
class mingyan(scrapy.Spider):

    # 定义蜘蛛名
    name = 'mingyan2'

    # 此方法通过下面链接爬取页面
    def start_requests(self):
        urls = [
            'http://lab.scrapyd.cn/page/1/',
            'http://lab.scrapyd.cn/page/2/',
            'http://lab.scrapyd.cn/page/3/',
        ]

        # 爬取到的页面直接调用下面定义的parse方法处理
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        '''
        start_requests已经爬取到页面，那如何提取我们想要的内容呢？那就可以在这个方法里面定义。
        这里的话，并木有定义，只是简单的把页面做了一个保存，并没有涉及提取我们想要的数据，后面会慢慢说到
        也就是用xpath、正则、或是css进行相应提取，这个例子就是让你看看scrapy运行的流程：
        1、定义链接；
        2、通过链接爬取（下载）页面；
        3、定义规则，然后提取数据；
        就是这么个流程，似不似很简单呀？
        '''

        # 根据url请求得到页面，提取里面的页码，如：/page/1/，提取到倒数第二个元素的就是：1
        page = response.url.split('/')[-2]

        # 拼接文件名称，如果是第一页，最终文件名便是：mingyan-1.html
        filename = 'mingyan-%s.html' % page

        # 保存爬取到的网页内容
        # wb以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
        with open(filename, 'wb') as f:
            # 将下载页面中的body标签下的内容写入
            f.write(response.body)










