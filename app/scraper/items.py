# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    subtitle = scrapy.Field()
    contents = scrapy.Field()
    pub_date = scrapy.Field()
    oid = scrapy.Field()

