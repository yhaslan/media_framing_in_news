# Import scrapy and scrapy.crawler 
import os 
import logging

import scrapy
from scrapy.crawler import CrawlerProcess
import scrapy.utils.misc
import scrapy.core.scraper

class ALJSpider(scrapy.Spider):
    name = 'alj_spider'

    def warn_on_generator_with_return_value_stub(spider, callable):
        pass

    scrapy.utils.misc.warn_on_generator_with_return_value = warn_on_generator_with_return_value_stub
    scrapy.core.scraper.warn_on_generator_with_return_value = warn_on_generator_with_return_value_stub

    def start_requests(self):
        # Read the HTML content obtained from Selenium saved in the file
            with open('aljazeera_html_content.html', 'r', encoding='utf-8') as file:
                html_content = file.read()

            # Pass the fake response to the parse method
            yield scrapy.Request(url='https://example.com', callback=self.parse, meta={'html_content': html_content})

    def parse(self, response):
        html_content = response.meta.get('html_content')
        sel = scrapy.Selector(text=html_content)
        links = sel.css('a.u-clickable-card__link::attr(href)').getall()

        dates = sel.css('div.date-simple > span:not(.screen-reader-text)::text').getall()
        titles = sel.css('a.u-clickable-card__link > span::text').getall()

    

        # Loop through extracted data (titles and dates) if they have the same length
        if len(dates) == len(titles):
            for date, title, link in zip(dates, titles, links):
                yield {
                    'date': date,
                    'title': title,
                    'link': 'https://www.aljazeera.com'+ link
                }
        else:
            self.logger.warning("Length mismatch between dates, titles, and links")
    

filename = "aljazeera_links.json"

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
process.crawl(ALJSpider)
process.start()