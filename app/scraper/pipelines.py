# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from articles.models import Company


class ArticlePipeline:
    def process_item(self, item, spider):
        article = item['item']
        oid = item['oid']

        article['pub_company'] = Company.objects.get(oid=oid)
        article.save()
        return item
