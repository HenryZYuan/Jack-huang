# -*- coding: utf-8 -*-
from huaban.items import HuabanItem
import scrapy

class HuabanSpider(scrapy.Spider):
    name = 'meipic'
    allowed_domains = ['meisupic.com']
    baseURL = 'http://www.meisupic.com/topic.php'
    start_urls = [baseURL]

    def parse(self, response):
        node_list = response.xpath("//div[@class='plist_list']/div/a/@href").extract()
        if len(node_list) == 0:
            return
        for url in node_list:
            new_url = self.baseURL[:-9] + url
            yield scrapy.Request(new_url, callback = self.parse2)

    def parse2(self, response):
        node_list = response.xpath("//div[@id='searchCon2']/ul")
        if len(node_list) == 0:
            return
        item = HuabanItem()
        item["image_url"] = node_list.xpath("./li/a/img/@data-original").extract()
        yield item
