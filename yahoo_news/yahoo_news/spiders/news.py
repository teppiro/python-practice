from yahoo_news.items import Headline
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['https://news.yahoo.co.jp/']

    def parse(self, response):
        """
        トップページのトピックス一覧から個々のトピックスへのリンクを抜き出してたどる。
        """
        for url in response.css('div.sc-gjAXCV.esBJml a::attr("href")').re(r'/pickup/\d+$'):
            yield response.follow(url, self.parse_topics)

    def parse_topics(self, response):
        """
        トピックスのページからタイトルと本文を抜き出す
        """
        item = Headline()
        item['title'] = response.css('p.sc-faswKr.bMRUDC::text').get() #タイトル
        item['body'] = response.css('p.sc-inlrYM.highLightSearchTarget::text').get() #本文
        yield item #Itemをyieldして、データを抽出する。
