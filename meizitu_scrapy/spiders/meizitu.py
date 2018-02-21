import scrapy
from scrapy import Request
from meizitu_scrapy.items import MeizituScrapyItem

class Meizitu(scrapy.Spider):
    name = "meizitu"

    def start_requests(self):
        n = 1
        for i in range(n):
            i +=1
            url = 'http://www.meizitu.com/a/pure_' + str(i) + '.html'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        item = MeizituScrapyItem()
        names = response.xpath('//ul[@class="wp-list clearfix"]/li/div/h3/a//text()').extract()
        page_urls = response.xpath('//ul[@class="wp-list clearfix"]/li/div/h3/a/@href').extract()
        for name in names:
            item['name'] = name
            yield item
        for page_url in page_urls:
            item['page_url'] = page_url
            yield item
            print(page_url)
            yield Request(page_url, callback=self.get_img_url)

    def get_img_url(self,response):
        # item = MeizituScrapyItem()
        img_urls = response.xpath('//*[@id="picture"]/p/img/@src').extract()
        for img_url in img_urls:
            print(img_url)
            yield Request(img_url,callback=self.down_pic)
            # item['img_url'] = img_url
        # yield item

    def down_pic(self,response):

        pass