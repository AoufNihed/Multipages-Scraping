1- Create a virtula env:
python -m venv env

2-active virtual env :
env\Scripts\activate

3- install scrapy :
pip install scrapy

4- start scrapy project:
scrapy startproject 

5- install spider:
scrapy genspider  multipage multipage

6- return what we need from website:

product_name=texts = response.css('a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal > span.a-size-base-plus.a-color-base.a-text-normal::text').getall()

prices = response.css('a.a-link-normal.s-no-hover.s-underline-text.s-underline-link-text.s-link-style.a-text-normal > span.a-price > span.a-offscreen::text').getall()


7-create items:
from scrapy.item import Item, Field

8-csv save project 
scrapy crawl multipage -o multipage.csv
