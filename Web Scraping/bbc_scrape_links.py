import os

import logging

import pandas as pd
import logging

# Import scrapy and scrapy.crawler 
import scrapy
from scrapy.crawler import CrawlerProcess
import scrapy.utils.misc
import scrapy.core.scraper



class BBCSpider(scrapy.Spider):
    
    name = "bbc"

    def warn_on_generator_with_return_value_stub(spider, callable):
        pass

    scrapy.utils.misc.warn_on_generator_with_return_value = warn_on_generator_with_return_value_stub
    scrapy.core.scraper.warn_on_generator_with_return_value = warn_on_generator_with_return_value_stub
    #def start_requests(self):
   
    all_urls = []
    for i in range(1,43):
         new_url= f'https://www.bbc.com/news/topics/c2vdnvdg6xxt?page={i}'
         all_urls.append(new_url)


    start_urls = all_urls
         

    def parse(self, response):
        latest = response.xpath('//ol[contains(@class, "ssrcss-jv9lse-Stack")][contains(@class, "e1y4nx260")]/li')
        for news in latest:
            link = news.css('a.ssrcss-9haqql-LinkPostLink.ej9ium92::attr(href)').get()
            date = news.css('span.ssrcss-dyweam-Timestamp.ej9ium93::text').get()
            if link is not None:
                full_link = 'https://www.bbc.com'+ link
            else:
                 full_link = link

            yield {
                'url': full_link,
                'date': date if date else None,  # Strip whitespace if date exists
            }
          

            #news_page = news.xpath('./a[@class="ssrcss-9haqql-LinkPostLink ej9ium92"]').attrib["href"]
            #article = news_page('/article[@class="ssrcss-pv1rh6-ArticleWrapper e1nh2i2l6"]')
            #title = article.xpath('.//h1[@class="ssrcss-15xko80-StyledHeading e10rt3ze0"]/text()').get()
            #bold_text = article.xpath('.//p/b[@class="ssrcss-hmf8ql-BoldText e5tfeyi3"]/text()').get()
            #texts = article.xpath('.//p/[@class="ssrcss-1q0x1qg-Paragraph e1jhz7w10"]/text()').getall()

        #next_page = response.xpath('//a[contains(@class, "ssrcss-1hnkt5q-StyledLink e1f8wbog0") and contains(text(),"Next")]/@href').get()


        
        
filename = "bbc_links.json"

# If file already exists, delete it before crawling (because Scrapy will 
# concatenate the last and new results otherwise)
if filename in os.listdir('src/'):
        os.remove('src/' + filename)


process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        'src/' + filename : {"format": "json"},
    }
})

# Start the crawling using the spider you defined above
process.crawl(BBCSpider)
process.start()

