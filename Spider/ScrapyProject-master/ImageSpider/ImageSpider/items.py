# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImagespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 既然我们要下载图片，肯定要得到图片的链接地址，
    # 我们需要定义一个Item类，用来存放图片链接
    imgurl = scrapy.Field()
    # imgname = scrapy.Field()
    pass
