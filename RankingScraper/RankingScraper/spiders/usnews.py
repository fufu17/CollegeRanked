# -*- coding: utf-8 -*-
import scrapy


class UsnewsSpider(scrapy.Spider):
    name = 'usnews'
    allowed_domains = ['https://www.usnews.com/best-colleges/rankings/national-universities']
    start_urls = ['https://www.usnews.com/best-colleges/rankings/national-universities']

    def parse(self, response):
        for infoDiv in response.css("div.shadow-dark.block-flush"):
            uniName = infoDiv.css("h3.heading-large.block-tighter a::text").extract_first()
            uniRank = infoDiv.css("div.text-strong div::text").extract_first().split()[0]
            if uniRank is None:
                uniRank = infoDiv.css("div.block-normal.text-strong").extract_first()
            yield {
                "name": uniName,
                "rank": uniRank,
            }
        next_page = response.css("link[rel='next']::attr(href)").extract_first()
        if "page=21" not in next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)