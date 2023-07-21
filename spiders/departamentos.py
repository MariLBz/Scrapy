import scrapy

class NachosSpider(scrapy.Spider):
    name = "departamentos"
    allowed_domains = ["listado.mercadolibre.com.ar"]
    start_urls = ["https://inmuebles.mercadolibre.com.ar/departamentos/venta/cordoba/"]

    def parse(self, response):
        all_links =  response.xpath('//div[@class="andes-carousel-snapped__wrapper"]/div[1]/a/@href').getall()
      	all_prices = response.xpath('//div[@class="ui-search-price ui-search-price--size-medium shops__price"]/div/span/span[3]/text()').getall()
        dolar = response.xpath('//div[@class="ui-search-price ui-search-price--size-medium shops__price"]/div/span/span[2]/text()').getall()
        all_sizes = response.xpath('//ul[@class="ui-search-card-attributes ui-search-item__group__element shops__items-group-details"]/li[1]/text()').getall()
        
        for i in range(len(all_links)):
            link = all_links[i]
            price = dolar[i]+all_prices[i]
            size = all_sizes[i][0:-9]
            
            yield{
                'link' : link,
                'price': price,
                'size' : size          
                  }
