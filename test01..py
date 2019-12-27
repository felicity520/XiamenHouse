# print(''.join([/, p]))

# a = '20190607'
# A = list(start_urls)  # 转化
# start_urls.insert(start_urls.rindex('p', beg=0, end=len(start_urls)), 'pg')  # 注意不用重新赋值
# a = ''.join(A)  # 转化回来
# print(a)


# 有一个字符串
# str_1 = '月圆星/疏夜,/n'
# str_1 = 'https://xm.lianjia.com/ershoufang/jimei/p1/'
# 把字符串转为 list
# str_list = list(str_1)
# 字符数， 可以利用这个在某个位置插入字符
# count = len(str_list)
# 找到 斜杠的位置
# for index, nums in enumerate(str_list):
#     if nums == '/p':
#         print("循环内", index)
#         break
# nPos = str_list.index('/')
# print(nPos)
# 在斜杠位置之前 插入要插入的字符
# str_list.insert(dex - 1, '佳人何处在!')
# 将 list 转为 str
# print("外面", index)
# str_list.insert(index - 1, '佳人何处在!')
# str_2 = "".join(str_list)
# print(str_2)
# print(type(str_2))

#
# a = [3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 7, 8, 8, 3]
# for index, nums in enumerate(a):
#     if nums == 3:
#         print(index)
# start_urls = []
# price_dict = dict(
#     # 100万以下：25页
#     p1="p1",
#     # 100-200万：5
#     p2="p1",
#     # 200-300万:28
#     p3="p3",
#     # 300-400万:49
#     p4="p3",
#     # 400-500万:39
#     p5="p4",
#     # 500-800万:75
#     p6="p6",
#     # 800万以上:55
#     p7="p7"
# )
#
# for price in list(price_dict.keys()):
#     # https://xm.lianjia.com/ershoufang/siming/pg2p1/
#     if price == "p1":
#         for page in range(1, 25 + 1):
#             url = "https://xm.lianjia.com/ershoufang/siming/pg{}".format(page) + "p1/"
#             print(url)
#             start_urls.append(url)

# import re
#
# mortgageinformation = ['\n                                有抵押 100万元 工商银行 客户偿还\n                              ']
# # mortgageinformation = '\n                                有抵押 100万元 工商银行 客户偿还\n                              '
# print(mortgageinformation)
# print(''.join(mortgageinformation))
# print(''.join(mortgageinformation).replace('\n', '').strip())
# print(''.join(mortgageinformation).replace('\n', '').strip().split('这里传任何字符串中没有的分割单位都可以，但是不能为空'))
#
# str1 = 'helloworld'
# print(str1.split('这里传任何字符串中没有的分割单位都可以，但是不能为空'))
#
# # num = re.sub(r'\S', "", str(mortgageinformation))
# # print(num)
# #
# buildyears = ['1996年建/板楼']
# buildyears = list(re.findall(r"\d+", str(buildyears)))
# print(buildyears)

#
# phone = "2004-959-559 # \n    这是一个国外电话\n号码"
# num = re.sub(r'/n', "", phone)
# print("电话号码是 : ", num)


# 湖里---------------------------
start_urls = []
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
