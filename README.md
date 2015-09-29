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

### when to change proxy
Often, we wanna change to use a new proxy when our spider gets
banned. Just edit the process_response function as the example.
