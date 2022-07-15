import scrapy


class BeastSpider(scrapy.Spider):
    name = 'wiki_beasts'
    start_urls = ['https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83']

    def __init__(self):
        self.results = {}

    def parse(self, response):
        latters_in_page = len(response.xpath('//*[@id="mw-pages"]/div/div/div').getall())
        for i in range(latters_in_page):
            key = response.xpath(f'//*[@id="mw-pages"]/div/div/div[{i+1}]/h3/text()').get()
            if key[0] in self.results:
                self.results[key[0]] += len(response.xpath(f'//*[@id="mw-pages"]/div/div/div[{i+1}]/ul/li').getall())
            else:
                self.results[key[0]] = len(response.xpath(f'//*[@id="mw-pages"]/div/div/div[{i+1}]/ul/li').getall())

        next_page = 'https://ru.wikipedia.org/'+response.xpath('//*[@id="mw-pages"]/a[2]/@href').get()
        request = scrapy.Request(url=next_page)
        yield request
        yield self.results

