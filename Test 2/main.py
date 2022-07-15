from wiki_beast.wiki_beast.spiders.beast_spider import BeastSpider
from scrapy.crawler import CrawlerProcess

items = []

class ItemCollectorPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        items.append(item)
        

process = CrawlerProcess({
    'USER_AGENT': 'scrapy',
    'LOG_LEVEL': 'INFO',
    'ITEM_PIPELINES': { '__main__.ItemCollectorPipeline': 1000 }
})
process.crawl(BeastSpider)
process.start()

print("results is ")
print(items[-1])
