import scrapy
from tutorial.spiders.dbutil import DBHelper
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BitCoinSpider(scrapy.Spider):
    name = "bitcoin"
    # start_urls = [
    #     'https://finance.yahoo.com/news/bitcoin-ethereum-ripple-bitcoin-cash-190600722.html'
    # ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print ("Start Driver ...")
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('no-sandbox')
        options.add_argument('disable-gpu')
        options.add_argument('disable-dev-shm-usage')
        options.add_argument('window-size=1200x600')
        self.driver = webdriver.Chrome('E:/chromedriver.exe',chrome_options=options)
        self.dbutil = DBHelper()

    def start_requests(self):
        urls = [
            'https://www.coindesk.com/category/markets-news'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parseWeb(self):
        page = self.driver.page_source
        soup = BeautifulSoup(page, 'html.parser')
        selects = soup.find_all('a',{"class": "stream-article"},href=True)
        for select in selects:
            item = {
                'title': select.get_text(),
                'href': select['href'],
                'pubtime': select.select('div.meta > div > time')[0].get_text(),
                'brand': select.select('div.meta > div')[0].get_text()
            }
            self.dbutil.insert(item)

    def parse(self, response):
        self._get_page(response.url)
        # Do something...
        while(True):
            clk = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="load-more-stories"]/button'))) 
            if clk == None:
                break
            clk.click()
            self.parseWeb()
        
       



#YDC-Stream > ul > li:nth-child(4) > div > div > div.Ov\28 h\29.Pend\28 44px\29.Pstart\28 25px\29 > div.Fz\28 12px\29.Fw\28 b\29.Tt\28 c\29.D\28 ib\29.Mb\28 6px\29.C\28 \24 c-fuji-blue-1-a\29.Mend\28 9px\29.Mt\28 -2px\29
        #self._close_driver()

    def _close_driver(self):
        print ("Closing Driver ...")
        self.driver.close()
        self.driver.quit()

    def _get_page(self, url):
        print ("Getting Page ...")
        self.driver.get(url)



    # def parse(self, response):
    #     x = DBHelper();
    #     for quote in response.css('li.js-stream-content Pos(r)'):
    #         print(quote)
    #         # item = {
    #         #     'title': quote.css('div > div > div.Ov\28 h\29.Pend\28 44px\29.Pstart\28 25px\29 > h3 ::text').get(),
    #         #     'url': quote.css('div > div > div.Ov\28 h\29.Pend\28 44px\29.Pstart\28 25px\29 > h3 > a :: href').get()
    #         # } 
    #         #x.insert(item)