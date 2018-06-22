import scrapy
from scrapy.loader import ItemLoader
from src.online_shopping.online_shopping.items import OnlineShoppingItem

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

        item = ItemLoader(item=OnlineShoppingItem(), response=response)
        item.add_xpath(field_name='name',
                       xpath='//div[@class="product-information"]/h2/text()')
        item.add_xpath(field_name='payment_method',
                       xpath='//div[@class="product-information"]/div[2]/text()[6]')
        item.add_value(field_name='vendor',
                       value=response.xpath('//div[@class="info-wrap"]/p[2]/text()').extract_first().split(': ')[
                           -1] if (response.xpath(
                           '//div[@class="info-wrap"]/p[2]/text()').extract_first() is not None) and (response.xpath(
                           '//div[@class="info-wrap"]/p[2]/text()').extract_first() is not ' ') else response.xpath(
                           '//div[@class="info-wrap"]/p[2]/a[@class="ex3"]/text()').extract_first())
        item.add_value(field_name='instock',
                       value=True if response.xpath(
                           '//div[@class="product-information"]/div[2]/text()[4]').extract_first() == " In Stock\n" else False)
        item.add_value(field_name='delivery_areas_src',
                       value=response.xpath('//div[@class="product-information"]/script/text()').extract_first().split(
                           "src=")[-1].split(" ")[0] if response.xpath(
                           '//div[@class="product-information"]/script/text()').extract_first() is not None else 'N/A')
        item.add_value(field_name='max_qty',
                       value=response.xpath(
                           '//div[@class="col-md-3"]/select[@class="form-control"]/option[last()]/text()').extract_first().split(
                           "\xa0\xa0")[0] if response.xpath(
                           '//div[@class="col-md-3"]/select[@class="form-control"]/option[last()]/text()').extract_first() is not None else 'N/A')
        item.add_value(field_name='similar_items',
                       value=response.xpath(
                           '//div[@class="box spaceIn"]/ul[@class="prod-list"]/li/a[2]/p/span[1]/text()').extract())

        yield item.load_item()
