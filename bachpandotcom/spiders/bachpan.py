import scrapy
from string import ascii_lowercase
import re

lower_pattern = re.compile("^[a-z]+$")


def next(url):
    l = url.split('=')
    l[-1] = str(int(l[-1]) + 1)
    return '='.join(l)


class BachpanSpider(scrapy.Spider):
    name = "bachpan"

    def start_requests(self):
        urls = [
            'https://bachpan.com/indian-boy-names-{}.aspx?page=1'.format(c) for c in ascii_lowercase]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        response.css('td.c1 a::text')
        data = response.css('td.c1 a::text').getall()
        data = list(map(lambda x: x.lower(),  data))
        data = list(filter(lambda x: lower_pattern.match(x), data))
        if data:
            yield {'data': data}
            next_page = next(response.url)
            print("next_page")
            print(next_page)
            # self.log("next_page %s", next_page)
            yield scrapy.Request(next_page, callback=self.parse)
