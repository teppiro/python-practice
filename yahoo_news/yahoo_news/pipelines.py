# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ValidationPipeline:
    """
    Itemを検証するPipeline
    """
    def process_item(self, item, spider):
        if not item['title']:
            raise DropItem('Missing title')
        return item