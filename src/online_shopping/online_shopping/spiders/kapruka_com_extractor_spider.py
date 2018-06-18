import json
import scrapy


class KaprukaComExtractorSpider(scrapy.Spider):
    name = "kaprukacomextractor"

    def start_requests(self):
        file = open('../../links/final_links.txt', 'r')
        urls = file.read().split('\n')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Print what the spider is doing
        print(response.url)
        # Get all the <a> tags
        a_selectors = response.xpath('//script[@type="application/ld+json"]')
        # Loop on each tag
        for selector in a_selectors:
            # Extract the link text
            text = selector.xpath("text()").extract_first()
            # Return it thanks to a generator
            data = json.loads(text)
            yield data