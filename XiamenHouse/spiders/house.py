# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.http import Request
from XiamenHouse.items import PageItem


# 标记为测试代码的可以不用看，test01.py文件和housetest.py也是测试文件，可以忽略
class HouseSpider(scrapy.Spider):
    # 定义该Spider的名字
    name = 'house'
    # 定义该Spider允许爬取的域名
    allowed_domains = ['xm.lianjia.com']
    # -----------测试：建议不要用房天下来爬取，因为不加params根本无法爬取数据，而且params不好寻找规律。安居客打开需要输入验证码，所以这里选择链家。
    # OK False
    # start_urls = ['https://xm.esf.fang.com/house-a0354/d2100/?_rfss=f6&rfss=1-01adc8a5a023aa3867-f6']
    # 报错：NG True  解决：刷新网页，然后重新copy链接，设置False就OK了
    # ------------------测试代码------------------
    # 定义该Spider爬取的url
    start_urls = []
    # dict表示字典，以key-value来保存
    # 这里是逐个爬取每个区的数据，为了一层一层的往下爬数据，用价格区间做划分，打开网页找到每个价格区间对应的最大页面数，然后用for循环赋值，比较笨的方法
    # 可以观察下链家的url，100万以下是p1  pg2表示第二页 每个区用拼音拼写即可
    price_dict = dict(
        # 100万以下：思明区25页  湖里区26  海沧区23  集美28  翔安12  同安3
        p1="p1",
        # 100-200万：思明区5     湖里区8   海沧区11  集美11  翔安14  同安8
        p2="p2",
        # 200-300万:思明区28     湖里区25  海沧区23  集美45  翔安29  同安9
        p3="p3",
        # 300-400万:思明区49     湖里区25  海沧区28  集美36  翔安14  同安5
        p4="p4",
        # 400-500万:思明区39     湖里区21  海沧区18  集美29  翔安3   同安3
        p5="p5",
        # 500-800万:思明区75     湖里区39  海沧区14  集美17  翔安2   同安2
        p6="p6",
        # 800万以上:思明区55     湖里区28  海沧区7   集美7   翔安2   同安1
        p7="p7"
    )

    # ---------------------思明区的url：不可删除---------------------
    # for price in list(price_dict.keys()):
    #     # https://xm.lianjia.com/ershoufang/siming/pg2p1/
    #     if price == "p1":
    #         for page in range(1, 25 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/siming/pg{}".format(page) + "p1/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p2":
    #         for page in range(1, 5 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/siming/pg{}".format(page) + "p2/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p3":
    #         for page in range(1, 28 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/siming/pg{}".format(page) + "p3/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p4":
    #         for page in range(1, 49 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/siming/pg{}".format(page) + "p4/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p5":
    #         for page in range(1, 39 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/siming/pg{}".format(page) + "p5/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p6":
    #         for page in range(1, 75 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/siming/pg{}".format(page) + "p6/"
    #             # print(url)
    #             start_urls.append(url)
    #     else:
    #         for page in range(1, 55 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/siming/pg{}".format(page) + "p7/"
    #             # print(url)
    #             start_urls.append(url)
    # ---------------------思明区的url：不可删除---------------------

    # ---------------------湖里区的url：不可删除---------------------
    # for price in list(price_dict.keys()):
    #     # https://xm.lianjia.com/ershoufang/huli/pg3p7/
    #     if price == "p1":
    #         for page in range(1, 26 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/huli/pg{}".format(page) + "p1/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p2":
    #         for page in range(1, 8 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/huli/pg{}".format(page) + "p2/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p3":
    #         for page in range(1, 25 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/huli/pg{}".format(page) + "p3/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p4":
    #         for page in range(1, 25 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/huli/pg{}".format(page) + "p4/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p5":
    #         for page in range(1, 21 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/huli/pg{}".format(page) + "p5/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p6":
    #         for page in range(1, 39 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/huli/pg{}".format(page) + "p6/"
    #             # print(url)
    #             start_urls.append(url)
    #     else:
    #         for page in range(1, 28 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/huli/pg{}".format(page) + "p7/"
    #             # print(url)
    #             start_urls.append(url)
    # ---------------------湖里区的url：不可删除---------------------

    # ---------------------海沧区的url：不可删除---------------------
    # for price in list(price_dict.keys()):
    #     # https://xm.lianjia.com/ershoufang/haicang/pg3p1/
    #     if price == "p1":
    #         for page in range(1, 23 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/haicang/pg{}".format(page) + "p1/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p2":
    #         for page in range(1, 11 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/haicang/pg{}".format(page) + "p2/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p3":
    #         for page in range(1, 23 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/haicang/pg{}".format(page) + "p3/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p4":
    #         for page in range(1, 28 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/haicang/pg{}".format(page) + "p4/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p5":
    #         for page in range(1, 18 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/haicang/pg{}".format(page) + "p5/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p6":
    #         for page in range(1, 14 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/haicang/pg{}".format(page) + "p6/"
    #             # print(url)
    #             start_urls.append(url)
    #     else:
    #         for page in range(1, 7 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/haicang/pg{}".format(page) + "p7/"
    #             # print(url)
    #             start_urls.append(url)
    # ---------------------海沧区的url：不可删除---------------------

    # ---------------------集美区的url：不可删除---------------------
    # for price in list(price_dict.keys()):
    #     # https://xm.lianjia.com/ershoufang/jimei/pg3p1/
    #     if price == "p1":
    #         for page in range(1, 28 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/jimei/pg{}".format(page) + "p1/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p2":
    #         for page in range(1, 11 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/jimei/pg{}".format(page) + "p2/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p3":
    #         for page in range(1, 45 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/jimei/pg{}".format(page) + "p3/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p4":
    #         for page in range(1, 36 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/jimei/pg{}".format(page) + "p4/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p5":
    #         for page in range(1, 29 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/jimei/pg{}".format(page) + "p5/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p6":
    #         for page in range(1, 17 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/jimei/pg{}".format(page) + "p6/"
    #             # print(url)
    #             start_urls.append(url)
    #     else:
    #         for page in range(1, 7 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/jimei/pg{}".format(page) + "p7/"
    #             # print(url)
    #             start_urls.append(url)
    # ---------------------集美区的url：不可删除---------------------
    # ---------------------翔安区的url：不可删除---------------------
    # for price in list(price_dict.keys()):
    #     # https://xm.lianjia.com/ershoufang/xiangan/pg3p1/
    #     if price == "p1":
    #         for page in range(1, 12 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/xiangan/pg{}".format(page) + "p1/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p2":
    #         for page in range(1, 14 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/xiangan/pg{}".format(page) + "p2/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p3":
    #         for page in range(1, 29 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/xiangan/pg{}".format(page) + "p3/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p4":
    #         for page in range(1, 14 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/xiangan/pg{}".format(page) + "p4/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p5":
    #         for page in range(1, 3 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/xiangan/pg{}".format(page) + "p5/"
    #             # print(url)
    #             start_urls.append(url)
    #     elif price == "p6":
    #         for page in range(1, 2 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/xiangan/pg{}".format(page) + "p6/"
    #             # print(url)
    #             start_urls.append(url)
    #     else:
    #         for page in range(1, 2 + 1):
    #             url = "https://xm.lianjia.com/ershoufang/xiangan/pg{}".format(page) + "p7/"
    #             print(url)
    #             start_urls.append(url)
    # ---------------------翔安区的url：不可删除---------------------
    # ---------------------同安区的url：不可删除---------------------
    for price in list(price_dict.keys()):
        # https://xm.lianjia.com/ershoufang/tongan/pg2p1/
        if price == "p1":
            for page in range(1, 3 + 1):
                url = "https://xm.lianjia.com/ershoufang/tongan/pg{}".format(page) + "p1/"
                # print(url)
                start_urls.append(url)
        elif price == "p2":
            for page in range(1, 8 + 1):
                url = "https://xm.lianjia.com/ershoufang/tongan/pg{}".format(page) + "p2/"
                # print(url)
                start_urls.append(url)
        elif price == "p3":
            for page in range(1, 9 + 1):
                url = "https://xm.lianjia.com/ershoufang/tongan/pg{}".format(page) + "p3/"
                # print(url)
                start_urls.append(url)
        elif price == "p4":
            for page in range(1, 5 + 1):
                url = "https://xm.lianjia.com/ershoufang/tongan/pg{}".format(page) + "p4/"
                # print(url)
                start_urls.append(url)
        elif price == "p5":
            for page in range(1, 3 + 1):
                url = "https://xm.lianjia.com/ershoufang/tongan/pg{}".format(page) + "p5/"
                # print(url)
                start_urls.append(url)
        elif price == "p6":
            for page in range(1, 2 + 1):
                url = "https://xm.lianjia.com/ershoufang/tongan/pg{}".format(page) + "p6/"
                # print(url)
                start_urls.append(url)
        else:
            for page in range(1, 1 + 1):
                url = "https://xm.lianjia.com/ershoufang/tongan/pg{}".format(page) + "p7/"
                # print(url)
                start_urls.append(url)

    # ---------------------同安区的url：不可删除---------------------

    # 拿到每一个详情页的url
    def parse(self, response):
        parturllist = response.xpath('//*[@class="sellListContent"]/li/a/@href').extract()
        # print("parturllist", len(parturllist))
        # print("response.url", response.url)
        for house in parturllist:
            # print("house:", house)
            yield Request(house, callback=self.parse1)

    # 对详细页的内容进行爬取解析
    def parse1(self, response):
        # 数据信息参考这个网页：https://xm.lianjia.com/ershoufang/105103438571.html
        # 小区名称
        housename = response.xpath('/html/body/div[5]/div[2]/div[5]/div[1]/a[1]/text()').extract()
        if housename:
            print("housename is ok")
        else:
            housename = ['暂无数据']
        # 户型：两室一厅
        room = response.xpath('//*[@class="houseInfo"]/*[@class="room"]/*[@class="mainInfo"]/text()').extract()
        if room:
            print("room is ok")
        else:
            room = ['暂无数据']
        # 房屋朝向：南北
        dtype = response.xpath('//*[@class="houseInfo"]/*[@class="type"]/*[@class="mainInfo"]/text()').extract()
        if dtype:
            print("dtype is ok")
        else:
            dtype = ['暂无数据']
        # 房屋面积：多少平
        area = response.xpath('//*[@class="houseInfo"]/*[@class="area"]/*[@class="mainInfo"]/text()').extract()
        if area:
            print("area is ok")
        else:
            area = ['暂无数据']
        # 装修:包含装修情况和户型结构 举例：平层 简装
        # fixtures = response.xpath('//*[@class="houseInfo"]/*[@class="type"]/*[@class="subInfo"]/text()').extract()
        # 修建时间：1996建 建筑类型：板楼
        # buildyears = str(response.xpath('//*[@class="houseInfo"]/*[@class="area"]/*[@class="subInfo"]/text()').extract()).find("/")
        # indexnum = str(
        #     response.xpath('//*[@class="houseInfo"]/*[@class="area"]/*[@class="subInfo"]/text()').extract()).find("/")
        # buildyears = list(
        #     str(response.xpath('//*[@class="houseInfo"]/*[@class="area"]/*[@class="subInfo"]/text()').extract())[
        #     2:indexnum])

        # 修建年代
        buildyears = response.xpath('/html/body/div[5]/div[2]/div[4]/div[3]/div[2]/text()').extract()
        buildyears = list(re.findall(r"\d+", str(buildyears)))
        if buildyears:
            print("buildyears is ok")
        else:
            buildyears = ['暂无数据']
        # 建筑类型:板楼
        architecturaltype = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[6]/text()').extract()
        if architecturaltype:
            print("architecturaltype is ok")
        else:
            architecturaltype = ['暂无数据']
        # 有无配备电梯
        elevator = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[11]/text()').extract()
        if elevator:
            print("elevator is ok")
        else:
            elevator = ['暂无数据']
        # 交易权属：商品房
        houseuse = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[2]/span[2]/text()').extract()
        if houseuse:
            print("houseuse is ok")
        else:
            houseuse = ['暂无数据']
        # 代码分割线----------------
        # 房屋总价 单位：万
        price = response.xpath('/html/body/div[5]/div[2]/div[3]/span[1]/text()').extract()
        if price:
            print("price is ok")
        else:
            price = ['暂无数据']
        #  price = str(price) + '万'
        # 房屋单价  单位：元/平米
        unitPrice = response.xpath('/html/body/div[5]/div[2]/div[3]/div[1]/div[1]/span/text()').extract()
        if unitPrice:
            print("unitPrice is ok")
        else:
            unitPrice = ['暂无数据']
        # 所在楼层
        floor = response.xpath('/html/body/div[5]/div[2]/div[4]/div[1]/div[2]/text()').extract()
        if floor:
            print("floor is ok")
        else:
            floor = ['暂无数据']
        # 房屋用途：普通住宅
        buildingType = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[4]/span[2]/text()').extract()
        if buildingType:
            print("buildingType is ok")
        else:
            buildingType = ['暂无数据']
        # 房屋年限：满五年
        fusamoto = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[5]/span[2]/text()').extract()
        if fusamoto:
            print("fusamoto is ok")
        else:
            fusamoto = ['暂无数据']
        # 产权期限：70年
        property = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[12]/text()').extract()
        if property:
            print("property is ok")
        else:
            property = ['暂无数据']
        # 所在的区域：区
        placequ = response.xpath('//*[@class="areaName"]/*[@class="info"]/a[1]/text()').extract()
        if placequ:
            print("placequ is ok")
        else:
            placequ = ['暂无数据']
        # 所在区域：路
        placeroad = response.xpath('//*[@class="areaName"]/*[@class="info"]/a[2]/text()').extract()
        if placeroad:
            print("placeroad is ok")
        else:
            placeroad = ['暂无数据']
        # 户型结构：平层
        huxingstructure = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[4]/text()').extract()
        if huxingstructure:
            print("huxingstructure is ok")
        else:
            huxingstructure = ['暂无数据']
        # 装修情况：简装
        fixturessituation = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[9]/text()').extract()
        if fixturessituation:
            print("fixturessituation is ok")
        else:
            fixturessituation = ['暂无数据']
        # 建筑结构：砖混结构
        buildstructure = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[8]/text()').extract()
        if buildstructure:
            print("buildstructure is ok")
        else:
            buildstructure = ['暂无数据']
        # 梯户结构：一梯两户
        ladderstructure = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[10]/text()').extract()
        if ladderstructure:
            print("ladderstructure is ok")
        else:
            ladderstructure = ['暂无数据']
        # 套内面积：暂无数据
        inarea = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[5]/text()').extract()
        if inarea:
            print("inarea is ok")
        else:
            inarea = ['暂无数据']
        # 挂牌时间:2019-11-27
        listingtime = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[1]/span[2]/text()').extract()
        if listingtime:
            print("listingtime is ok")
        else:
            listingtime = ['暂无数据']
        # 上次交易：2005-01-06
        lasttransaction = response.xpath(
            '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[3]/span[2]/text()').extract()
        if lasttransaction:
            print("lasttransaction is ok")
        else:
            lasttransaction = ['暂无数据']
        # 抵押信息：无抵押
        mortgageinformation = response.xpath(
            '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[7]/span[2]/text()').extract()
        mortgageinformation = ''.join(mortgageinformation).replace('\n', '').strip().split('---------')
        if mortgageinformation:
            print("mortgageinformation is ok")
        else:
            mortgageinformation = ['暂无数据']
        # 产权所属：非公有
        roppertyownership = response.xpath(
            '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[6]/span[2]/text()').extract()
        if roppertyownership:
            print("roppertyownership is ok")
        else:
            roppertyownership = ['暂无数据']
        # 房本备件：已上传房本照片
        housingspareparts = response.xpath(
            '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[8]/span[2]/text()').extract()
        if housingspareparts:
            print("housingspareparts is ok")
        else:
            housingspareparts = ['暂无数据']
        # 房源编码：00418320
        housingsourcecode = response.xpath(
            '//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[9]/span[2]/text()').extract()
        if housingsourcecode:
            print("housingsourcecode is ok")
        else:
            housingsourcecode = ['暂无数据']
        item = PageItem()
        item['housename'] = housename
        item['room'] = room
        item['dtype'] = dtype
        item['area'] = area
        # item['fixtures'] = fixtures
        item['buildyears'] = buildyears
        item['architecturaltype'] = architecturaltype
        item['elevator'] = elevator
        item['houseuse'] = houseuse
        item['price'] = price
        item['unitPrice'] = unitPrice
        item['floor'] = floor
        item['buildingType'] = buildingType
        item['fusamoto'] = fusamoto
        item['property'] = property
        item['placequ'] = placequ
        item['placeroad'] = placeroad
        item['huxingstructure'] = huxingstructure
        item['fixturessituation'] = fixturessituation
        item['buildstructure'] = buildstructure
        item['ladderstructure'] = ladderstructure
        item['inarea'] = inarea
        item['listingtime'] = listingtime
        item['lasttransaction'] = lasttransaction
        item['mortgageinformation'] = mortgageinformation
        item['roppertyownership'] = roppertyownership
        item['housingspareparts'] = housingspareparts
        item['housingsourcecode'] = housingsourcecode
        # yield将item的数据发送到pipelines进行保存，不懂这个流程可以看下scrapy框架的流程
        yield item

        # -----------------------------------测试代码-----------------------------------
        # pagenum = response.xpath('//*[@id="content"]/div[1]/div[8]/div[2]/div/@page-data').extract()
        # print("每个url对应的最大页面数", pagenum)
        # d = pagenum[0]
        # maxpage = d[13]
        # print(type(d))
        # print(d)
        # print("每个url对应的最大页面数", maxpage)
        # print(dict['totalPage'])
        # item = PageItem()  # 实例化
        # item["pagemax"] = maxpage
        # yield item
        # -----------------------------------测试代码-----------------------------------
