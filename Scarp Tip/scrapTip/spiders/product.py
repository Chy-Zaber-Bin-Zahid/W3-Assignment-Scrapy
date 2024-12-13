import scrapy
from scrapTip.items import ProductItem

class ProductSpider(scrapy.Spider):
    name = 'product'
    start_urls = ['https://www.scrapingcourse.com/ecommerce/']

    def parse(self, response):
        for product in response.css("li.product"):
            item = ProductItem()
            item['product_name'] = product.css("h2.product-name::text").get()
            item['product_price'] = product.css("span.product-price bdi::text").get()
            item['product_image_url'] = product.css("img::attr(src)").get()
            item['product_link'] = product.css("a.woocommerce-LoopProduct-link::attr(href)").get()
            yield item  # This sends the item to the pipeline
