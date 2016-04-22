# HttpProxyMiddlware
A middleware for scrapy. Used to change HTTP proxy from time to time.

Initial proxyes are stored in a file. During runtime, the middleware
will fetch new proxyes if it finds out lack of valid proxyes.

## fetch_free_proxyes.py
Used to fetch free proxyes from the Internet. Could be modified by
youself.

## Usage

### settings.py
```
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 3,
    # put this middleware behind retrymiddleware
    'crawler.middleware.HttpProxyMiddleware': 4,
}
```

### change proxy

Often, we wanna change to use a new proxy when our spider gets
banned.  Just recognize your IP being banned and yield a new Request
in your Spider.parse method with:

    request.meta["change_proxy"]=True


Some proxy may return invalid HTML code. So if you get any exception
during parsing response, also yield a new request with:

    request.meta["change_proxy"] = True


### spider.py

Your spider should specify an array of status code where your spider
may encouter during crawling. Any status code that is not 200 nor in
the array would be treated as a result of invalid proxy and the proxy
would be discarded. For example:

    website_possible_httpstatus_list = [404]

This line tolds the middleware that the website you're crawling would
possibly return a response whose status code is 404, and do not
discard the proxy that this request is using.
