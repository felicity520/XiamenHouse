import scrapy
from scrapy import Field


class PageItem(scrapy.Item):
    # 27
    # 小区名称
    housename = Field()
    # 户型：两室一厅
    room = Field()
    # 房屋朝向：南北
    dtype = Field()
    # 房屋面积：多少平
    area = Field()
    # 装修:包含装修情况和户型结构 举例：平层 简装
    # fixtures = Field()
    # 修建时间：1996建 建筑类型：板楼
    # buildyears = Field()
    # 修建年代
    buildyears = Field()
    # 建筑类型：板楼
    architecturaltype = Field()
    # 有无电梯
    elevator = Field()
    # 交易权属：商品房
    houseuse = Field()
    # 房屋总价
    price = Field()
    # 房屋单价
    unitPrice = Field()
    # 所在楼层
    floor = Field()
    # 房屋用途：普通住宅
    buildingType = Field()
    # 房屋年限：满五年
    fusamoto = Field()
    # 产权期限：70年
    property = Field()
    # 所在区域的区
    placequ = Field()
    # 所在区域的路
    placeroad = Field()
    # 户型结构
    huxingstructure = Field()
    # 装修情况
    fixturessituation = Field()
    # 建筑结构
    buildstructure = Field()
    # 梯户结构：一梯两户
    ladderstructure = Field()
    # 套内面积：暂无数据
    inarea = Field()
    # 挂牌时间:2019-11-27
    listingtime = Field()
    # 上次交易：2005-01-06
    lasttransaction = Field()
    # 抵押信息：无抵押
    mortgageinformation = Field()
    # 产权所属：非公有
    roppertyownership = Field()
    # 房本备件：已上传房本照片
    housingspareparts = Field()
    # 房源编码：00418320
    housingsourcecode = Field()
