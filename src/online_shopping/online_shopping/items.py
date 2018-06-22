# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class OnlineShoppingItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    vendor = scrapy.Field(output_processor=TakeFirst())
    instock = scrapy.Field(output_processor=TakeFirst())
    payment_method = scrapy.Field(output_processor=TakeFirst())
    delivery_areas_src = scrapy.Field(output_processor=TakeFirst())
    delivery_areas = scrapy.Field()
    max_qty = scrapy.Field(output_processor=TakeFirst())
    similar_items = scrapy.Field()
    pass
