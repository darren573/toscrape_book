# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Field, Item


class ToscrapeBookItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BookItem(Item):
    name = Field()  # 书名
    price = Field()  # 价格
    review_rating = Field()  # 评价等级 1-5星
    review_num = Field()  # 评价数量
    upc = Field()  # 产品编码
    stock = Field()  # 库存量
