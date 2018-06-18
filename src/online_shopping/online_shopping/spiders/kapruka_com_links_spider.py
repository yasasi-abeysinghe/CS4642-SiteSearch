import scrapy
from scrapy.linkextractors import LinkExtractor


class KaprukaComLinksSpider(scrapy.Spider):
    name = "kaprukacomlinks"
    allowed_domains = ["www.kapruka.com"]

    def start_requests(self):
        file = open('../../links/links.txt', 'r')
        urls = file.read().split('\n')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        extractor = LinkExtractor(allow_domains=['kapruka.com'])
        links = extractor.extract_links(response)
        file = open('../../links/links.txt', 'a')
        for link in links:
            file.write('\n' + link.url)