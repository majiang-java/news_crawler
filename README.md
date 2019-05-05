# Overview

这个是一个基于scrapy框架的爬虫程序，scrapy天然分装好的多线程。
而且有非常多的分装好的中间件可以方便使用，比如seesion池，代理， 并且方便使用redis扩展分布式

# topic

1.  限制ip用requests代理，买代理，或者网上免费代理
2.  伪装成浏览器requests切换user agent
3.  先登录，保存cookiesrequests用session先post拿到cookies，再爬
4.  URL参数太多，一般使用分治法处理网站，先收集种子再逐步爬取

#how to play

scrapy crawl neteast
