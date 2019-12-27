BOT_NAME = 'XiamenHouse'
SPIDER_MODULES = ['XiamenHouse.spiders']
NEWSPIDER_MODULE = 'XiamenHouse.spiders'
# 有些网站反爬，加上这个相当于用一个伪装的网站来访问，任意选择一个即可。
USER_AGENT = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
# 这个一定要为False
ROBOTSTXT_OBEY = False
# 设置爬虫的间隔时间：6秒算长的，所以爬取的速度比较慢，怕被网站禁掉IP，并关掉COOKIES
# 反爬虫：设置不同的浏览器UA或者IP地址来回避网站的屏蔽
DOWNLOAD_DELAY = 6
COOKIES_ENABLED = False
# 关闭重定向
REDIRECT_ENABLED = True
# 链家没有重定向问题。之前爬其他网站留下的，可以保留。解决返回码是301的重定向问题：https://blog.csdn.net/xueba8/article/details/81841408
HTTPERROR_ALLOWED_CODES = [301]
# 数据库主机
MYSQL_HOST = 'localhost'
# 数据库名称
MYSQL_DBNAME = 'xiamenhouse'
# 数据库账户名称
MYSQL_USER = 'root'
# 数据库账户密码
MYSQL_PASSWD = 'root'
# 默认100即可
ITEM_PIPELINES = {
    'XiamenHouse.pipelines.XiamenhousePipeline': 100,
}
# 默认从xm.lianjia.com这个域名爬取
DEFAULT_REQUEST_HEADERS = {
    'Host': 'xm.lianjia.com'
}
