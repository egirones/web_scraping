#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 17:06:13 2017

@author: egirones
"""

import scrapy
from scrapy.loader import ItemLoader
from feed.items import FeedItem
#from scrapy.crawler import CrawlerProcess

class feedSpider(scrapy.Spider):
    name = 'feed'
    allowed_domains = ['http://www.project-syndicate.org/']
    start_urls = ['http://www.project-syndicate.org/innovation-technology']
    
    def parse(self, response):
        website_title = response.xpath('//title/text()').extract()
        links = response.xpath('//article[contains(@class, "innovation-technology")]')
        for link in links:
            l = ItemLoader(item=FeedItem(),selector=link)
            l.add_value('website', website_title)
            l.add_xpath('title', './h2/a/text()')
            l.add_xpath('author','./p/a/text()')
            l.add_xpath('url', './a/@href')
            yield l.load_item()
        
#        all_items = []
#        website = response.xpath('//titl/text()').extract()
#        for news in response.xpath('//article[contains(@class, "innovation-technology")]'):
#            item = FeedItem()
#            item['website'] = website
#            item['author'] = news.xpath('p/a/text()').extract()
#            item['title'] = news.xpath('h2/a/text()').extract()
#            item['url'] = news.xpath('a/@href').extract()
#            all_items.append(item)
#        return(all_items)


#################################
        
        
#            item = FeedItem()
#            item['website'] = website
#            item['author'] = news.xpath('span/text()').extract()
#            item['title'] = news.xpath('h3/text()').extract()
#            item['url'] = news.xpath('@href').extract()
#            all_items.append(item)
#        return(all_items)
            
 #       for news in response.xpath('//div[contains(@class, "innovation-technology")]/a'):
 #           l = ItemLoader(item=FeedItem)
 #           l.add_value('author', 'span/text()')
 #           return l.load_item()
        
            #loader.add_xpath('website', website)
           # loader.add_xpath('author', 'span/text()')
            
#        all_items = []
#        website = 'Project Syndicate'
#        for news in response.xpath('//div[contains(@class, "innovation-technology")]/a'):
#            item = FeedItem()
#            item['website'] = website
#            item['author'] = news.xpath('span/text()').extract()
#            item['title'] = news.xpath('h3/text()').extract()
#            item['url'] = news.xpath('@href').extract()
#        for news in response.xpath('//article[contains(@class, "innovation-technology")]'):
#            item = FeedItem()
#            item['website'] = "holi"
#            item['author'] = news.xpath('p/a/text()').extract()
#            item['title'] = news.xpath('h2/a/text()').extract()
#            item['url'] = news.xpath('a/@href').extract()
#            all_items.append(item)
#        return(all_items)
        
        
      
#process = CrawlerProcess()
#process.crawl(feedSpider)
#process.start()