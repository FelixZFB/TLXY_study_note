# -*- coding: utf-8 -*-
# 运行方式：进入ImageSpider目录（scrapy.cfg所在目录)输入：
# scrapy crawl ImgSpider111

import scrapy
from ImageSpider.items import ImagespiderItem


class ImgspiderSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'ImgSpider111'
    # 设置过滤爬取的域名,不在此允许范围内的域名就会被过滤
    # 对于start_urls里的起始爬取页面，它是不会过滤的，它的作用是过滤首页之后的页面
    allowed_domains = ['https://www.mzitu.com']
    # 开始爬取的网站
    start_urls = []
    # 生成一个网站列表，爬取第1页到第10页
    for i in range(300, 376):
        url = "https://www.mzitu.com/zipai/comment-page-" + str(i) + "/#comments"
        start_urls.append(url)

    def parse(self, response):
        # item是items.py中ImagespiderItem()的一个实例
        # 用来存放获取的图片连接地址
        item = ImagespiderItem()

        # 采用extract()，提取的所有满足规则的连接，
        # 注意imgurls是一个集合也就是多张图片的连接地址，提取的结果是一个列表
        # css选择器，选择class属性为lazy标签中属性为data-original的值
        # 将获取的图片地址列表传递给item['imgurl']
        # item['imgurl']又传递给pipelines.py，地址循环后下载每一张图片
        item['imgurl'] = response.css('.lazy::attr(data-original)').extract()
        # 抓取文章的标题作为图集文件夹的名称，每一个网址放在同一个文件夹下
        yield item

