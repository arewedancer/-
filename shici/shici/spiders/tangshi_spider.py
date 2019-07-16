import scrapy


class TangshiSpider(scrapy.Spider):
    name = "tangshi"
    start_urls = ['https://so.gushiwen.org/gushi/tangshi.aspx']

    def parse(self, response):
        for href in response.css('span a::attr(href)').getall():
            print href
            yield response.follow('https://so.gushiwen.org' + href, self.parse_content)

    def parse_content(self, response):
        yield {
            'content': response.xpath('//head/meta[@name="description"]').xpath('@content').get()
        }

