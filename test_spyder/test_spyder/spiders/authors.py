import scrapy
from scrapy.crawler import CrawlerProcess


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'authors.json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            author_link = quote.xpath(".//a[starts-with(@href, '/author/')]/@href").get()
            yield response.follow(author_link, callback=self.parse_author)

        next_link = response.css('li.next a::attr(href)').get()
        if next_link:
            yield response.follow(next_link, callback=self.parse)

    def parse_author(self, response):
        yield {
            "fullname": response.css('h3.author-title::text').get(),
            "born_date": response.css('span.author-born-date::text').get(),
            "born_location": response.css('span.author-born-location::text').get(),
            "description": response.css('div.author-description::text').get().strip()
        }


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(AuthorsSpider)
    process.start()