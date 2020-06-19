import logging
from datetime import datetime
from urllib import parse

import scrapy
from pytz import timezone
from scrapy.utils.log import configure_logging

from scraper.items import ArticleItem


class ArticleSpider(scrapy.Spider):
    name = 'Article'
    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='log.txt',
        format='%(levelname)s: %(message)s',
        level=logging.ERROR
    )

    now = datetime.now(tz=timezone('Asia/Seoul'))
    allowed_domains = ["news.naver.com"]
    oid_list = ['032', '005', '020']
    start_urls = [f'https://news.naver.com/main/list.nhn?mode=LPOD&listType=paper&oid={oid}' for oid in oid_list]

    def parse(self, response):
        last_page = response.xpath('//*[@id="main_content"]/div[2]/div[3]/div/ul/li[last()]/a/@href').extract()[0][-1]
        last_page = int(last_page)
        for i in range(1, last_page + 1):
            url = response.url + f'&page={i}' + f'&date={self.now.strftime("%Y%m%d")}'
            yield scrapy.Request(url, callback=self.parse_page_articles_url)

    def parse_page_articles_url(self, response):
        article_urls = response.xpath(
            '//div[@class="list_body newsflash_body"]//ul[@class="type13 firstlist"]/li//a/@href').extract()
        for url in article_urls:
            yield scrapy.Request(url, callback=self.parse_articles, meta={
                'handle_httpstatus_list': [302],
            })

    def parse_articles(self, response):
        if response.status == 200:
            item = ArticleItem()
            query = parse.parse_qs(parse.urlparse(response.url).query)
            contents = response.xpath('//div[@id="articleBodyContents"]/text()').extract()
            if contents:
                contents = ''.join(contents).strip()
            else:
                contents = None
            oid = query['oid'][0]
            aid = query['aid'][0]
            title = response.css('h3#articleTitle::text').get().strip()
            subtitle = response.css('strong.media_end_summary').get()
            pub_date = self.now.strftime("%Y%m%d")

            item['title'] = title
            item['subtitle'] = subtitle
            item['contents'] = contents
            item['aid'] = aid
            item['pub_date'] = pub_date

            yield {'item': item, 'pub_date': pub_date}

