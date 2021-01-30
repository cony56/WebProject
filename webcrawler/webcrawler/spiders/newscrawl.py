import scrapy
from webcrawler.items import WebcrawlerItem
import sys
from scrapy.http import Request


URL = 'http://news.naver.com/main/list.nhn?mode=LS2D&sid2=258&sid1=101&mid=shm&date=20210127&page={}'
start_page = 1

def remove_space(descs:list) -> list:
        result = []
        for i in range(len(descs)):
            if len(descs[i].strip()) > 0:
                result.append(descs[i].strip())
        return result
def unique_href(href_list):
    new_list =[]
    prev = href_list[0]
    new_list.append(prev)
    for href in href_list[1:]:
        if href == prev:
            pass
        else:
            new_list.append(href)
            prev = href
    return new_list


class NewscrawlSpider(scrapy.Spider):
    name = 'newscrawl'
    allowed_domains = ['naver.com']
    start_urls = [URL.format(start_page)]
    
    def parse(self, response):
        titles = response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt/a/text()').extract()
        titles = remove_space(titles)
        # 공백 제거하기
        writers = response.css('.writing::text').extract()
        articles = response.css('.lede::text').extract()
        hrefs = response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt/a/@href').extract()
        hrefs = unique_href(hrefs)
        
        # 겹치는 거는 빼주기
        print("-----------------------------------------------------------------------------")
        print(len(titles), len(writers), len(articles), len(hrefs))
        items = []
        for idx in range(len(titles)):
            item = WebcrawlerItem()
            item['title'] = titles[idx]
            item['writer'] = writers[idx]
            item['article'] = articles[idx]
            item['href'] = hrefs[idx]
            item['slug'] = idx

            items.append(item)

        return items
    
    def start_requests(self):
        for i in range(5):
            #request에 대한 생성자를 반환시킴
            # request를 실행한 다음에 parse함수를 실행시키게 연동시키는게 callback의 기능임
            yield Request(url=URL.format(i+start_page),callback=self.parse)