
# Import scrapy and scrapy.crawler 
import os 
import pandas as pd

# Import logging => Library used for logs manipulation 
## More info => https://docs.python.org/3/library/logging.html
import logging

# Import scrapy and scrapy.crawler 
import scrapy
from scrapy.crawler import CrawlerProcess
import scrapy.utils.misc
import scrapy.core.scraper

from urllib.parse import unquote


class NewsSpider(scrapy.Spider):
    
    name = "bbcnews"

    def warn_on_generator_with_return_value_stub(spider, callable):
        pass

    scrapy.utils.misc.warn_on_generator_with_return_value = warn_on_generator_with_return_value_stub
    scrapy.core.scraper.warn_on_generator_with_return_value = warn_on_generator_with_return_value_stub
    df = pd.read_json('src/bbc_links.json')
    df=df[df['url'].isna()==False]

    google_bbc = ['https://www.bbc.com/news/world-europe-67356581',
              'https://www.bbc.com/news/live/world-middle-east-67364296',
              'https://www.bbc.com/news/world-africa-67257862',
              'https://www.bbc.com/news/live/world-middle-east-67364296',
              'https://www.bbc.com/news/world-middle-east-67390375',
              'https://www.bbc.com/news/live/world-middle-east-67339462',
              'https://www.bbc.com/news/world-middle-east-67355319',
              'https://www.bbc.com/news/world-middle-east-67327079',
              'https://www.bbc.com/news/world-middle-east-67372035',
              'https://www.bbc.com/news/world-middle-east-67372661',
              'https://www.bbc.com/news/world-europe-67356581',
              'https://www.bbc.com/news/world-us-canada-67354706',
              'https://www.bbc.com/news/world-67273969',
              'https://www.bbc.com/news/world-us-canada-67342868',
              'https://www.bbc.com/news/world-middle-east-67373293',
              'https://www.bbc.co.uk/news/uk-england-kent-67378052',
              'https://www.bbc.com/news/world-middle-east-67385617',
              'https://www.bbc.com/news/world-middle-east-67375667',
              'https://www.bbc.com/news/world-asia-67353188',
              'https://www.bbc.com/news/world-middle-east-67345430',
              'https://www.bbc.com/news/world-middle-east-67321241',
              'https://www.bbc.com/news/world-us-canada-67339982',
              'https://www.bbc.com/news/world-middle-east-67376148',
              'https://www.bbc.com/news/world-middle-east-67373461',
              'https://www.bbc.com/sport/africa/67228507',
              'https://www.bbc.com/news/world-europe-67368409',
              'https://www.bbc.com/news/uk-scotland-scotland-politics-67367577',
              'https://www.bbc.com/news/world-middle-east-67350709',
              'https://www.bbc.com/news/world-67349605',
              'https://www.bbc.com/news/uk-scotland-edinburgh-east-fife-67344032',
              'https://www.bbc.com/news/live/uk-67390343',
              'https://www.bbc.com/pidgin/articles/cv2zwjlp701o',
              'https://www.bbc.com/news/uk-67349474',
              'https://www.bbc.com/news/world-67374801',
              'https://www.bbc.com/news/uk-67367617',
              'https://www.bbc.com/news/uk-67366031',
              'https://www.bbc.com/news/world-us-canada-67336799',
              'https://www.bbc.com/news/uk-wales-politics-67357824',
              'https://www.bbc.com/news/uk-wales-politics-67343909',
              'https://www.bbc.com/pidgin/articles/c4n4z40eve2o',
              'https://www.bbc.com/news/uk-england-merseyside-67367560',
              'https://www.bbc.com/news/world-us-canada-67342387',
              'https://www.bbc.com/news/av/world-europe-67399096',
              'https://www.bbc.com/news/uk-england-leeds-67363678',
              'https://www.bbc.com/news/uk-politics-67364797',
              'https://www.bbc.com/news/world-middle-east-67391335',
              'https://www.bbc.com/news/uk-politics-67353019',
              'https://www.bbc.com/news/uk-england-manchester-67370101',
                           
             ]

    start_urls =  google_bbc + df['url'].tolist()

    def parse(self, response): 
    
            #article = response.xpath('/article[contains(@class, "ssrcss-pv1rh6-ArticleWrapper")][contains(@class, "e1nh2i2l6")]')
            #title = article.xpath('.//h1[contains(@class, "ssrcss-15xko80-StyledHeading")][contains(@class, "e10rt3ze0")]/text()').get()
            #bold_text = article.xpath('.//p/b[contains(@class,"ssrcss-hmf8ql-BoldText")][contains(@class, "e5tfeyi3")]/text()').get()
            #texts = article.xpath('.//p/[contains(@class="ssrcss-1q0x1qg-Paragraph")][contains(@class, "e1jhz7w10")]/text()').getall()
            article = response.xpath('//article[contains(@class, "ssrcss-pv1rh6-ArticleWrapper")][contains(@class, "e1nh2i2l5")]')
            date = response.css('time[data-testid="timestamp"]::attr(datetime)').get()
        
            if article:
                title = article.xpath('.//h1[contains(@class, "ssrcss-15xko80-StyledHeading")][contains(@class, "e10rt3ze0")]/text() | '
                      './/h1[contains(@class, "ssrcss-15xko80-StyledHeading")][contains(@class, "e10rt3ze0")]/span/text()').get()
                bold_text = article.xpath('.//p/b[contains(@class,"ssrcss-hmf8ql-BoldText")][contains(@class, "e5tfeyi3")]/text()').get()
                texts = article.xpath('.//p[contains(@class,"ssrcss-1q0x1qg-Paragraph")][contains(@class, "e1jhz7w10")]/text()').getall()


                yield {
                    'title': title,
                    'bold': bold_text,
                    'body': texts,
                    'date':date,
                    'link': response.url
                }
            else:
                self.logger.info(f"No article found on {response.url}")

        
filename = "bbc_news.json"

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
process.crawl(NewsSpider)
process.start()

