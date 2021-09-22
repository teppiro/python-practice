from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from yahoo_news.items import Headline

class NewsCrawlSpider(CrawlSpider):
    name = 'news_crawl'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['https://news.yahoo.co.jp/']

    # リンクをたどるためのルールのリスト。
    rules = (
      # トピックスのページへのリンクをたどり、レスポンスをparse_topics()メソッドで処理する。
      Rule(LinkExtractor(allow=r'/pickup/\d+$'), callback='parse_topics'),
    )

    def parse_topics(self, response):
        """
        トピックスのページからタイトルと本文を抜き出す
        """
        item = Headline()
        item['title'] = response.css('p.sc-faswKr.bMRUDC::text').get() #タイトル
        item['body'] = response.css('p.sc-inlrYM.highLightSearchTarget::text').get() #本文
        yield item #Itemをyieldして、データを抽出する。
