from scrapy.crawler import CrawlerProcess
from test_spyder.test_spyder.spiders.authors import AuthorsSpider
from test_spyder.test_spyder.spiders.quotes import QuotesSpider


def main():
    process = CrawlerProcess()
    process.crawl(AuthorsSpider)
    process.crawl(QuotesSpider)
    process.start()


if __name__ == '__main__':
    main()
