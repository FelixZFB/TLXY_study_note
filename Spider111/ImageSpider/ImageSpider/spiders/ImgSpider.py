# - 爬虫项目文件夹命名后，里面的py文件
    # - 会自动创建以项目文件夹名称相关的类，名称的首字母会大写，
    # - 之后的字母会自动变成小写
# - 爬虫主py文件，要换一个名称，不要和项目文件名相同
    # - 爬虫主py文件中的爬虫name和爬虫py文件命名一致


import scrapy

from ImageSpider.items import ImagespiderItem

class ImgspiderSpider(scrapy.Spider):
    name = 'ImgSpider'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = [
        'http://lab.scrapyd.cn/archives/55.html',
        'http://lab.scrapyd.cn/archives/57.html',
    ]

    def parse(self, response):
        # 实例化item
        item = ImagespiderItem()
        # 获取所有的图片链接地址，是一个列表，放在item['imgurl']中
        # item['imgurl']就相当于是scrapy.Field()
        item['imgurl'] = response.css('.post img::attr(src)').extract()
        # 抓取文章的标题作为图集的名称
        item['imgname'] = response.css(".post-title a::text").extract_first()
        yield item



