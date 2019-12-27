# -*- coding: utf-8 -*
import requests
from lxml import etree

# 请求头和目标网址
headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
}

url = 'http://esf.xm.fang.com/house-a0354/d2100/'

# 第二种写法的 xpath
# 获取所有 li标签
# xpath_items = '//ul[@class="note-list"]/li'
xpath_items = '//div[@class="main945 floatl"]'
# 对每个 li标签再提取
# xpath_comment_num = '/a/@href'
xpath_comment_num = './div[@class="page_a1"]/span[2]/a/@href'

# 获取和解析网页
r = requests.get(url, headers=headers)
print("items:" + str(r))
r.encoding = r.apparent_encoding
print("r:" + str(r))
dom = etree.HTML(r.text)
print("dom:" + str(dom))

# 获取所有的文章标签
items = dom.xpath(xpath_items)
print("items:" + str(items))

# items:<Response [200]>
# r:<Response [200]>
# dom:<Element html at 0x37b6e08>
# items:[]

# 分别对每一个文章标签进行操作 将每篇文章的链接 标题 评论数 点赞数放到一个字典里
data = []
for article in items:
    t = {}
    t['link'] = article.xpath(xpath_comment_num)
    # t['title'] = article.xpath(xpath_title)[0]
    # comment_num对应的标签里有两个文本标签 用 join方法将两个文本拼接起来
    # strip()方法去除换行和空格
    # t['comment_num'] = ''.join(article.xpath(xpath_comment_num)).strip()
    # t['heart_num'] = article.xpath(xpath_heart_num)[0].strip()
    data.append(t)
    print(t)

# # 打印结果
# for t in data:
#     print(t)
