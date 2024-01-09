
# Import scrapy and scrapy.crawler 
import os 
import logging


import pandas as pd
import scrapy
from scrapy.crawler import CrawlerProcess
import scrapy.utils.misc
import scrapy.core.scraper

class ALJNewsSpider(scrapy.Spider):
    name = "aljnews"

    def warn_on_generator_with_return_value_stub(spider, callable):
        pass

    scrapy.utils.misc.warn_on_generator_with_return_value = warn_on_generator_with_return_value_stub
    scrapy.core.scraper.warn_on_generator_with_return_value = warn_on_generator_with_return_value_stub

    df = pd.read_json('src/aljazeera_links.json')
    df = df.drop_duplicates().reset_index(drop=True)
    df = df[df['link'].isna() == False]
    df = df[(df['date'] < pd.Timestamp('2024-01-01')) &
                      (df['date'] > pd.Timestamp('2023-10-06'))]
    urls = df['link'].tolist()
    start_urls = urls

    def parse(self, response):
        title = response.css('h1::text').get()
        subhead = response.css('header.article-header p.article__subhead::text, header.article-header p.article__subhead em::text, h2.gallery-header__subhead::text, p.article__subhead.u-inline::text').get()
        texts = response.css('div.wysiwyg.wysiwyg--all-content.css-ibbk12 p::text').getall()

        yield {
            'title': title,
            'body': texts,
            'subhead': subhead,
            'link': response.url
        }

    def closed(self, reason):
        self.driver.quit()  # Close the browser after scraping is done

filename = "alj_news.json"

if filename in os.listdir('src/'):
    os.remove('src/' + filename)

process = CrawlerProcess(settings={
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        'src/' + filename: {"format": "json"},
    }
})

process.crawl(ALJNewsSpider)
process.start()
