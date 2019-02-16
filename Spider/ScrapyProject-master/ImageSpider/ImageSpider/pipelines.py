# -*- coding: utf-8 -*-
"""
功能：本项目主要演示Scrapy下载图片；
运行环境：win7 64 + python3.6 + scrapy1.4 +  mongodb3.4 + pymongo-3.6.0
运行方式：进入ImageSpider目录（scrapy.cfg所在目录)输入：

scrapy crawl ImgSpider

项目详情：http://www.scrapyd.cn/example/174.html；
创建时间：2018年2月28日12:47:46
创建者：scrapy中文网（http://www.scrapyd.cn）；
"""
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class ImagespiderPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        # item['imgurl']是网址列表，从spider主程序传递过来
        for image_url in item['imgurl']:
            # meta中的数据是从spider主程序传递过来
            # 然后meta传递给下面的方法file_path
            yield Request(image_url)
            # yield Request(image_url, meta={'name': item['imgname']})

'''
    def file_path(self, request, response=None, info=None):
        # 提取url前面名称作为图片名。
        image_guid = request.url.split('/')[-1]
        # 接收上面meta传递过来的图片名称
        name = request.meta['name']
        # 过滤windows字符串，不经过这么一个步骤，你会发现有乱码或无法下载
        name = re.sub(r'[?\\*|“<>:/]', '', name)
        # format函数，分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
        filename = u'{0}/{1}'.format(name, image_guid)
        return filename
'''