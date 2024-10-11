import scrapy
from scrapy.item import Item, Field

# Define the Scrapy item for product details
class MultipageItem(Item):
    name = Field()
    price = Field()

class MultipageSpider(scrapy.Spider):
    name = "multipage"
    start_urls = ["https://www.amazon.fr/s?k=arduino&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3UEYFAH3A73M3&sprefix=arduino+%2Caps%2C183&ref=nb_sb_noss_2"]
    page_name = 2  # Start from page 2 for pagination

    def parse(self, response):
        # Scrape the individual product details 
        products = response.css('div.a-section.a-spacing-small.puis-padding-left-small.puis-padding-right-small')

        for product in products:
            item = MultipageItem()

            # Extract product name and price
            item['name'] = product.css('a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal > span.a-size-base-plus.a-color-base.a-text-normal::text').get()
            item['price'] = product.css('a.a-link-normal.s-no-hover.s-underline-text.s-underline-link-text.s-link-style.a-text-normal > span.a-price > span.a-offscreen::text').get()

            yield item

        # Create the next page URL
        next_page = f'https://www.amazon.fr/s?k=arduino&page={MultipageSpider.page_name}&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3UEYFAH3A73M3&qid=1728189163&sprefix=arduino+%2Caps%2C183&ref=sr_pg_{MultipageSpider.page_name}'
        
        # Limit pagination to a set number of pages
        if MultipageSpider.page_name <= 7:
            MultipageSpider.page_name += 1
            # Use the correct callback name
            yield response.follow(next_page, callback=self.parse)
