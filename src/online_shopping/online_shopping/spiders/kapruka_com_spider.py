import scrapy

i = 0


class KaprukaComSpider(scrapy.Spider):
    name = "kaprukacom"

    def start_requests(self):
        file = open('../../links/final_links.txt', 'r')
        urls = file.read().split('\n')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        global i
        i += 1
        page = response.url.split("/")[-2]
        filename = '../../data/pages/kapruka-%s-%s.html' % (page, i)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)