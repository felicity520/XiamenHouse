import csv  # 导入csv模块，这个模块python自带就有
# 导入访问MySQL的模块:pymysql只是python的一个库，用来连接mysql
import time

import pymysql

from XiamenHouse import settings


class XiamenhousePipeline(object):
    # 定义构造器，初始化要写入的文件
    def __init__(self):
        # 连接数据库。可以查看settings的设置
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
        # 删除表格（第一次运行还没哟创建表格不可以进行删除，手动注释掉，代码里没有做判断）
        # self.cursor.execute("drop table house1")
        # 创建表格（第一次运行加上创建表格这段，因为要将数据存到表格）
        # self.cursor.execute(
        #     "create table house1(housename VARCHAR(255) DEFAULT NULL,room VARCHAR(255) DEFAULT NULL,dtype VARCHAR(255) DEFAULT NULL,area VARCHAR(255) DEFAULT NULL,buildyears VARCHAR(255) DEFAULT NULL,architecturaltype VARCHAR(255) DEFAULT NULL,elevator VARCHAR(255) DEFAULT NULL, houseuse VARCHAR(255) DEFAULT NULL, price VARCHAR(255) DEFAULT NULL, unitPrice VARCHAR(255) DEFAULT NULL, floor VARCHAR(255) DEFAULT NULL, buildingType VARCHAR(255) DEFAULT NULL, fusamoto VARCHAR(255) DEFAULT NULL, property VARCHAR(255) DEFAULT NULL, placequ VARCHAR(255) DEFAULT NULL,placeroad VARCHAR(255) DEFAULT NULL, huxingstructure VARCHAR(255) DEFAULT NULL, fixturessituation VARCHAR(255) DEFAULT NULL, buildstructure VARCHAR(255) DEFAULT NULL, ladderstructure VARCHAR(255) DEFAULT NULL, inarea VARCHAR(255) DEFAULT NULL,listingtime VARCHAR(255) DEFAULT NULL,lasttransaction VARCHAR(255) DEFAULT NULL, mortgageinformation VARCHAR(255) DEFAULT NULL, roppertyownership VARCHAR(255) DEFAULT NULL, housingspareparts VARCHAR(255) DEFAULT NULL, housingsourcecode VARCHAR(255) DEFAULT NULL)")

    # process_item是固定写法，固定函数
    def process_item(self, item, spider):
        print(type(item))
        print("名称:", item['housename'])
        print("户型:", item['room'])
        print("类型:", item['dtype'])
        print("大小:", item['area'])
        # print("装修:", item['fixtures'])
        print("年代:", item['buildyears'])
        print("建筑类型:", item['architecturaltype'])
        print("电梯:", item['elevator'])
        print("用途:", item['houseuse'])
        print("总价:", item['price'])
        print("单价:", item['unitPrice'])
        print("楼层:", item['floor'])
        print("类型:", item['buildingType'])
        print("房本:", item['fusamoto'])
        print("产权:", item['property'])
        print("所区:", item['placequ'])
        print("所路:", item['placeroad'])
        print("户型结构:", item['huxingstructure'])
        print("装修情况:", item['fixturessituation'])
        print("建筑结构:", item['buildstructure'])
        print("梯户结构:", item['ladderstructure'])
        print("套内面积:", item['inarea'])
        print("挂牌时间:", item['listingtime'])
        print("上次交易:", item['lasttransaction'])
        print("抵押信息:", item['mortgageinformation'])
        print("产权所属:", item['roppertyownership'])
        print("房本备件:", item['housingspareparts'])
        print("房源编码:", item['housingsourcecode'])

        # -------------------------------测试代码:将数据保存到excel的代码（可以了解下）------------------------------------------
        # 这里的item["room"]用item["housename"]都是一样的。因为一条户型信息对应一条小区名称信息。信息是对应的
        # for i in range(0, len(item["housename"])):
        #     data = (item["housename"][i].strip(), item["room"][i].strip(), item["dtype"][i].strip(),
        #             item["area"][i].strip(),
        #             # item["fixtures"][i].strip(),
        #             # item["buildyears"][i].strip(),
        #             item["architecturaltype"][i].strip(),
        #             item["elevator"][i].strip(),
        #             item["houseuse"][i].strip(),
        #             item["price"][i].strip(),
        #             item["unitPrice"][i].strip(),
        #             item["floor"][i].strip(),
        #             item["buildingType"][i].strip(),
        #             item["fusamoto"][i].strip(),
        #             item["property"][i].strip(),
        #             item["placequ"][i].strip(),
        #             item["placeroad"][i].strip(),
        #             item["huxingstructure"][i].strip(),
        #             item["fixturessituation"][i].strip(),
        #             item["buildstructure"][i].strip(),
        #             item["ladderstructure"][i].strip(),
        #             item["inarea"][i].strip(),
        #             item["listingtime"][i].strip(),
        #             item["lasttransaction"][i].strip(),
        #             item["mortgageinformation"][i].strip(),
        #             item["roppertyownership"][i].strip(),
        #             item["housingspareparts"][i].strip(),
        #             item["housingsourcecode"][i]
        #             )  # .strip()方法是将获取到的信息中的空格空白去除，可以试试没有strip后保存的结果
        #     with open('D:\python\PyProject\XiamenHouseMaster\data.csv', 'a', encoding='utf-8',
        #               newline='') as csvfile:  # 'D:\Python_DATA\dat.csv'为保存文件的地址，采用追加逐条写入
        #         writer = csv.writer(csvfile)
        #         writer.writerow(data)
        # ----------------------------------------------测试代码----------------------------------------------

        # 在其中执行数据的增删查改，通过cursor编写sql语句
        # 提交sql语句:注意此处提交的参数是connect而不是cursor
        # 将数据插入到house1这个表格中，%s表示字符串
        self.cursor.execute(
            "insert into house1(housename,room,dtype,area,buildyears,architecturaltype,elevator,houseuse,price,unitPrice,floor,buildingType,fusamoto,property,placequ,placeroad,huxingstructure,fixturessituation,buildstructure,ladderstructure,inarea,listingtime,lasttransaction,mortgageinformation,roppertyownership,housingspareparts,housingsourcecode) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                item['housename'], item['room'], item['dtype'], item['area'], item['buildyears'],
                item['architecturaltype'],
                item['elevator'], item['houseuse'], item['price'], item['unitPrice'],
                item['floor'], item['buildingType'], item['fusamoto'], item['property'],
                item['placequ'], item['placeroad'], item['huxingstructure'], item['fixturessituation'],
                item['buildstructure'], item['ladderstructure'], item['inarea'], item['listingtime'],
                item['lasttransaction'], item['mortgageinformation'], item['roppertyownership'],
                item['housingspareparts'], item['housingsourcecode']))
        self.connect.commit()
        return item

    # 重写close_spider回调方法，用于关闭数据库资源
    def close_spider(self, spider):
        print('----------关闭数据库资源-----------')
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.connect.close()

        # -------------测试代码：写入excel的代码
        # print("Pipeline页面数:", item['pagemax'])
        # data = (item["pagemax"][0].strip())  # .strip()方法是将获取到的信息中的空格空白去除，可以试试没有strip后保存的结果
        # with open('D:\Software\python\PyProject\XiamenHouseMaster\data.csv', 'a', encoding='utf-8',
        #           newline='') as csvfile:  # 'D:\Python_DATA\dat.csv'为保存文件的地址，采用追加逐条写入
        #     writer = csv.writer(csvfile)
        #     writer.writerow(data)
        # -------------测试代码-----------------
