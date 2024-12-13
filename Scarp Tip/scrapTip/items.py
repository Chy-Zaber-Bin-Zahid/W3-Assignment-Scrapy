import scrapy

class ProductItem(scrapy.Item):
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_image_url = scrapy.Field()
    product_link = scrapy.Field()
