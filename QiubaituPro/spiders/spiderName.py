import scrapy

from QiubaituPro.items import QiubaituproItem
class SpidernameSpider(scrapy.Spider):
    name = 'spiderName'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        all_data = []
        for div in div_list:
            # author = div.xpath('./div/a[2]/h2/text()')[0].extract()
            author = div.xpath('./div/a[2]/h2/text()').extract_frist()
            content = div.xpath('./a/div/span//text()').extract()
            content = ''.join(content)

            item = QiubaituproItem()
            item['author'] = author
            item['content'] = content
            yield item #将item提交给管道





    # def parse(self, response):
    #     div_list=response.xpath('//*[@id="content"]/div/div[2]/div')
    #     all_data=[]
    #     for div in div_list:
    #         author = div.xpath('./div/a[2]/h2/text()')[0].extract()
    #         content = div.xpath('./a/div/span//text()').extract()
    #         content = ''.join(content)
    #         dic={
    #             'author':author,
    #             'content':content,
    #         }
    #         all_data.append(dic)
    #     return all_data
    # #保存指令scrapy crawl xxx -o FilePath

