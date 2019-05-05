from scrapy.spiders import Spider
from scrapyspider.items import DoubanMovieItem

class DoubanMovieTop250Spider(Spider):
    name = 'douban_movie_top250'
    start_urls = ['https://movie.douban.com/top250']
    
    def parse(self, response):
        item = DoubanMovieItem()

    def start_requests(self):
        return [scrapy.FormRequest("http://www.example.com/login",
                               formdata={'user': 'john', 'pass': 'secret'},
                               callback=self.logged_in)]

    def logged_in(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        pass    