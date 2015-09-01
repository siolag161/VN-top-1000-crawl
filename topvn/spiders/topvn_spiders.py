# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy.selector import HtmlXPathSelector

from topvn.items import Firm

firm_attrs = ["rank", "tax_code", "listing_status", "headquarter",
              "tel", "fax", "email", "website", "category",
              "founded_date", "company_type",]

class TopFirmSpider(CrawlSpider):
    name = "topvn"
    allowed_domains = ["v1000.vn"]
    start_urls = (
        'http://www.v1000.vn/Charts/',
    )
    rules = (Rule(LinkExtractor(
         allow=( r"Charts/*", r"Thong-tin-doanh-nghiep/.*.html" ),
                 restrict_xpaths=('//*[@id="dataTables-example"]',)
                 ),
                callback="parse_results", follow= True),)

    def parse_results(self, response):
        url = response.url
        hxs = HtmlXPathSelector(response)

        trs = hxs.select('//*[@id="content"]/div[1]/div/table/tbody/tr')
        firm = Firm()
        firm["name"] = hxs.select('//*[@id="content"]/div[1]/p/text()').extract()[0].strip()
        for attr_id, tr in enumerate(trs):
            attr = tr.select("./td[1]/text()").extract()[0].strip()
            val = tr.select("./td[2]/text()").extract()[0].strip()
            if attr_id == 0: # ranking info
                val = self.extract_ranking(val)
            #setattr(firm, firm_attrs[attr_id], val)
            firm[firm_attrs[attr_id]] = val
        yield firm

    rank_pattern = re.compile("\\d+")
    def extract_ranking(self, txt):
        rank = self.rank_pattern.search(txt)
        return rank.group(0) if rank else "N/A"
