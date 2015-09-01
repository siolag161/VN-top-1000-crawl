# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Firm(scrapy.Item):
    """firm's general information"""
    firm_id = scrapy.Field()
    name = scrapy.Field()
    rank = scrapy.Field()
    tax_code = scrapy.Field()
    listing_status = scrapy.Field()
    headquarter = scrapy.Field()
    tel = scrapy.Field()
    fax = scrapy.Field()
    email = scrapy.Field()
    website = scrapy.Field()
    category = scrapy.Field()
    founded_date = scrapy.Field()
    company_type = scrapy.Field()
