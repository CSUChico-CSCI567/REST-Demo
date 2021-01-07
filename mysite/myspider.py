import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector


import sys, os
sys.path.append('.')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.conf import settings

from myapp import models



class FoodSpider(scrapy.Spider):
    name = 'foodspider'
    start_urls = ['https://www.foodnetwork.com/recipes/recipes-a-z']

    def parse(self, response):
        section = response.css("section.o-SiteIndex").get()
        recipe_list = Selector(text=section).css('li.m-PromoList__a-ListItem').getall()
        for recipe in recipe_list:
            link = Selector(text=recipe).css('a::attr(href)').get()
            yield scrapy.Request("http:"+link, callback=self.parse_recipe)
            # print(link)
    
    def parse_recipe(self, response):
        title = response.css('title::text').get()
        title = title.split("|")
        # print(title[0])
        section = response.css("div.recipeLead").get()
        image = "http:" + Selector(text=section).css('img.m-MediaBlock__a-Image::attr(src)').get()
        # print(image)
        url = response.url
        #Look for duplicate
        search = models.FoodModel.objects.filter(title=title[0])
        if len(search) == 0:
            # print("NONE")
            food = models.FoodModel()
            food.title=title[0]
            food.photo_url = image
            food.url = url
            food.save()
            # print(food)
        else:
            print(search)

        # print(food)
        # print(url)

            

        # for title in response.css('.post-header>h2'):
        #     yield {'title': title.css('a ::text').get()}

        # for next_page in response.css('a.next-posts-link'):
        #     yield response.follow(next_page, self.parse)

process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
})


process.crawl(FoodSpider)
process.start() # the script will block here until the crawling is finished