import scrapy

class RokomariSpider(scrapy.Spider):
    name = "rokomari_spider"
    start_urls = ['http://localhost:8080/rokomari_pages']
    
    # def parse(self, response):
        
    #     #all links
    #     LINK = ".body a ::attr(href)"
    #     for page in response.css(LINK):
    #         self.i +=1
    #         print(self.i)
    #         print(page)
    #         yield scrapy.Request(
    #             response.urljoin(page.css("::text").extract_first()),
    #             callback=self.parse_product
    #             )    
     
    def parse(self, response):
        hxs = scrapy.Selector(response)
        # extract all links from page
        all_links = hxs.xpath('*//a/@href').extract()
        # iterate over links
        for link in all_links:
            yield scrapy.Request(response.urljoin(link), callback=self.print_this_link)
 
    def print_this_link(self, link):
        print ("Link --> {this_link}" + str(link))

    def parse_product(self, response):        
            
            BOOK_SELECTOR = '.details-book-main-info__header h1::text'
            book = response.css(BOOK_SELECTOR).extract_first()
            
            yield { "product_name":book}
        
            LINK = "a ::attr(href)"
            
            for page in response.css(LINK):
                         
                yield scrapy.Request(
                       response.urljoin(page.css("::text").extract_first()),
                       callback=self.parse_product
                )    

            



# class BrickSetPipeline(object):
#     def process_item(self, item, spider):
#        print("Hello how are you?");        