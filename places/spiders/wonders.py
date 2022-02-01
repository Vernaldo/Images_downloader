import scrapy


class WondersSpider(scrapy.Spider):
    name = 'wonders'
    #allowed_domains = ['x.com']
    start_urls = ['https://en.wikipedia.org/wiki/Africa']

    def parse(self, response):
        raw_image_urls = response.css(' .thumbimage ::attr(src)').getall()
        clean_image_urls = []
        for img_url in raw_image_urls:
            clean_image_urls.append(response.urljoin(img_url))

        yield {
        'image_urls' : clean_image_urls
        }        
