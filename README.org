* HttpProxyMiddleware

A middleware for scrapy. Used to change HTTP proxy from time to time.

Initial proxyes are stored in a file. During runtime, the middleware
will fetch new proxyes if it finds out lack of valid proxyes.

Related blog: [[http://www.kohn.com.cn/wordpress/?p=208]]


** fetch_free_proxyes.py
Used to fetch free proxyes from the Internet. Could be modified by
youself.

** Usage

*** settings.py

#+BEGIN_SRC python
  DOWNLOADER_MIDDLEWARES = {
      'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
      'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 351,
      # put this middleware after RetryMiddleware
      'crawler.middleware.HttpProxyMiddleware': 999,
  }

  DOWNLOAD_TIMEOUT = 10           # 10-15 second is an experienmental reasonable timeout
#+END_SRC

*** change proxy

Often, we wanna change to use a new proxy when our spider gets banned.
Just recognize your IP being banned and yield a new Request in your
Spider.parse method with:

#+BEGIN_SRC python
request.meta["change_proxy"] = True
#+END_SRC

Some proxy may return invalid HTML code. So if you get any exception
during parsing response, also yield a new request with:

#+BEGIN_SRC python
request.meta["change_proxy"] = True
#+END_SRC


*** spider.py

Your spider should specify an array of status code where your spider
may encouter during crawling. Any status code that is not 200 nor in
the array would be treated as a result of invalid proxy and the proxy
would be discarded. For example:

#+BEGIN_SRC python
website_possible_httpstatus_list = [404]
#+END_SRC

This line tolds the middleware that the website you're crawling would
possibly return a response whose status code is 404, and do not
discard the proxy that this request is using.


** Test

Update HttpProxyMiddleware.py path in
HttpProxyMiddlewareTest/settings.py.


#+BEGIN_SRC sh
cd HttpProxyMiddlewareTest
scrapy crawl test
#+END_SRC


The testing server is hosted on my VPS, so take it easy... DO NOT
waste too much of my data plan.

You may start your own testing server using IPBanTest which is powered
by Django.
