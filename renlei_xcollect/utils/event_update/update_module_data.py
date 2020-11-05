# -*- coding: utf-8 -*-

from uqer import Client, DataAPI
from jqdatasdk import *
from scp import SCPClient
from paramiko import SSHClient
import psycopg2
import csv
import hashlib
import datetime
import json
import time
import os
import datetime
import threading
import time

from local_settings import *
from utils.auto.autoupdate import auto_update

ef_headers = ['title', 'abstract', 'media_source', 'url', 'publish_time', 'section_tags', 'event_tags', 'party_name',
              'assets_ids', 'sentiment', 'attention', 'market_type']

live_ef_headers = ['title', 'abstract', 'media_source', 'url', 'publish_time', 'section_tags', 'event_tags',
                   'party_name',
                   'assets_ids', 'sentiment', 'attention', 'market_type', 'event_status']

clean_ef_headers = ['hash_id', 'abstract', 'event_tags', 'party_name']

bad_description_strings = ["首页新闻军事政务财经汽车文化娱乐游戏守艺中华国防军事军事APP头条APP注册登录宏观海外证券产经房产酒业银行保险基金科技数码当前位置：",
                           "首页新闻军事政务财经汽车文化娱乐健康解梦游戏佛教守艺中华国防军事军事APP头条APP注册登录中华网设为书签Ctrl+D将本页面保存为书签，全面了解最新资讯，方便快捷。军事APP国内/国际/社会/专题/经济/滚动/政务/冬奥/公益当前位置：",
                           "中工网首页时政国际社会军事工会维权人物评论理论论坛博客网视播客图画财经企业就业旅游教育文化读书娱乐体育绿色城建社区RSS聚焦首页聚焦就业新闻大众创业万众创新声音观察创业沙龙职场·健康创见·思享热点专题高清图库",
                           "来源：智通财经网智通财经网更多文章>>广告：新股资讯尽在掌握广告：理财小贴士",
                           "中工网首页时政评论国际军事社会财经企业工会维权就业论坛博客理论人物网视图画体育汽车文化书画教育读书娱乐旅游绿色城建社区打工权益保障首页",
                           "中工网首页时政国际社会军事工会维权人物评论理论论坛博客网视播客图画财经企业就业旅游教育文化读书娱乐体育绿色城建社区 RSS热点聚焦工会要闻企业风采劳模人物法治社会经济民生调查监督工评正议职工沙龙维权帮扶集体协商视频新闻文体杂谈影像胶东首页",
                           "图片中工网首页　中工新闻首页",
                           "网站首页时政国际财经台湾军事观点领导人事理论法治社会产经教育科普体育文化书画房产汽车旅游健康视频登录注册退出登录人民网通行证",
                           "，也可关注微信公众号tel_world﻿运营商财经网八卦",
                           "人民网>>湖南频道>>",
                           "选择类别房地产综合规定房产地产权属管理房地产开发房地产企业房地产交易与市场土地使用与管理房地产信贷房地产税收房地产财会房地产评估住房公积金住房保障华侨房地产涉港澳台房地产涉外房地产历史遗留问题住房制度改革房屋住宅建设宗教房地产军队房地产搬迁拆迁安置房屋买卖拍卖房屋抵押物业管理城市规划其他相关新闻资讯",
                           "首页信用房地产房协专区新闻资讯数据研究行业测评政策法规采购平台直播间新闻资讯新闻资讯数据报告政策法规测评榜单全部类型其他年报半年报季报月报周报日报选择颁布时间",
                           "地方首页 >> 地方资讯 >> 正文",
                           "中工网首页时政国际社会军事工会维权人物评论理论论坛博客网视播客图画财经企业就业旅游教育文化读书娱乐体育绿色城建社区RSS学法365首页劳动维权职工社保维权故事安全生产学法365法治传真法治观察法律文库权益保护热点专题",
                           "中工网首页时政评论国际军事社会财经企业工会维权就业论坛博客理论人物网视图画体育汽车文化书画教育读书娱乐旅游绿色城建社区打工要闻纵览",
                           "实名认证的分析师均已通过人脸识别认证，身份信息真实可靠证书编号",
                           "更多资讯可登录运营商财经网（telworld.com.cn），也可关注微信公众号tel_world",
                           "首页新闻军事政务财经汽车文化娱乐健康解梦游戏佛教守艺中华国防军事军事APP头条APP注册登录中华网设为书签",
                           "热点栏目自选股数据中心行情中心资金流向模拟交易客户端　　",
                           "炒股就看金麒麟分析师研报，权威，专业，及时，全面，助您挖掘潜力主题机会！　　",
                           "首页｜要闻｜人民日报系说雄安｜政策｜解读｜聚焦京津冀｜直播访谈｜新雄安人｜文化｜生态｜雄图｜智库｜English要闻",
                           "Ctrl+D将本页面保存为书签",
                           "视频加载中，请稍候...自动播放play",
                           "&nbsp",
                           "中工网首页时政国际社会军事工会维权人物评论理论论坛博客网视播客图画财经企业就业旅游教育文化读书娱乐体育绿色城建社区RSS大众创业首页聚焦就业新闻大众创业万众创新声音观察创业沙龙职场·健康创见·思享热点专题高清图库",
                           "证券时报网证券时报网更多文章>>更多广告：证券之星APP下载广告：理财小贴士",
                           "中国健康营养食品首席顾问新闻热线:010-88564110商务合作:010-88564110电子邮箱:foodchina01@126.com要闻新零售品牌营养部委智库农产品当前位置>首页>",
                           "受损股民可至新浪股民维权平台登记该公司维权：http://wq.finance.sina.com.cn/　　微博关注@新浪证券、微信关注新浪券商基金、百度搜索新浪股民维权、访问新浪财经客户端、新浪财经首页都能找到我们！　　"
                           "来源：评论(0)收藏(0)微博微信用微信扫描二维码分享至好友和朋友圈QQ空间扫一扫用微信扫描二维码分享至好友和朋友圈",
                           "智通财经网智通财经网更多文章>>广告：新股资讯尽在掌握广告：",
                           "【链得得播报】链得得（微信号：ChainDD）",
                           "亮评论(0)收藏(0)微博微信用微信扫描二维码分享至好友和朋友圈QQ空间扫一扫用微信扫描二维码分享至好友和朋友圈",
                           "，全面了解最新资讯，方便快捷。军事APP国内/国际/社会/专题/经济/滚动/政务/冬奥/公益当前位置",
                           "四川新闻网巴中",
                           "投稿、反馈：gongsi@staff.hexun.com　　",
                           "青海新闻网·大美青海客户端讯",
                           "中研普华_中研网资讯报告头条资讯数据分析视点财经研究院规划院商学院百咖峰会当前位置：中研网 > 资讯 > 行业经济",
                           "金融界首页>房产频道>房地产动态>正文",
                           "您当前的位置：浙江网闻联播 >",
                           "首页>全百点>正文全百点实名认证的分析师均已通过人脸识别认证，身份信息真实可靠证书编号",
                           "评论(0)收藏(0)微博微信用微信扫描二维码分享至好友和朋友圈QQ空间扫一扫用微信扫描二维码分享至好友和朋友圈",
                           "首页新闻军事文史政务财经汽车文化娱乐健康解梦趣闻",
                           "首页新闻军事文史政务财经汽车文化娱乐健康解梦",
                           "游戏佛教古诗词守艺中华国防军事军事APP头条APP注册登录中华网设为书签  ：新闻>",
                           "首页时政国际工会维权财经人物网评就业理论视频军事图库民生体育汽车文化企业书画城建职教打工娱乐社区旅行公益绿色",
                           "首页新闻军事文史政务财经汽车文化娱乐健康解梦游戏佛教古诗词守艺中华国防军事军事APP头条APP注册登录中华网设为书签  ：新闻",
                           "中电网设为首页网站地图加入收藏 首页新闻新品文库方案视频下载商城开发板数据中心在线座谈培训工具博客论坛百科GEC活动主题月万花筒设计技术 嵌入式系统线性PMIC专用IC存储器接口数据采集时钟/计时逻辑配件传感器，变送器隔离器电源射频/IF和RFIDMCU|FPGA|嵌入式|模拟设计|RF|电源管理|传感器|测试测量|LED|DSP|存储器|AC/DC转换器|DC/DC转换器|放大器|铁电存储|应用开发智能能源电表与能源监视能量存储风能太阳能汽车电子安全性和底盘传动/混合动力系统其它汽车电子驾驶员信息娱乐车身电子通信&电信无线基础设施通信电源视频通信测试和测量光纤网络网络通信计算机与多媒体个人设备移动产品桌面服务器/高性能计算终端消费及便携电子产品家用电器消费类音频消费类视频产品个人电子产品其它医疗保健个人健康诊断/监视/治疗成像远程医疗家庭医疗保健工业控制工业自动化工业网络自动处理控制其它工业产品测试和测量构建技术零售自动化设备LED和通用照明汽车后灯照明标识电机驱动与控制AC感应电动机带刷DC电机永磁同步电机步进电机其它应用安全防卫入侵与访问控制带刷DC电机视频监视智能电网电表气表/水表网络基础设施家庭自动化通信系统空间/防务增强型产品便携式系统视频/视觉数码相机数字显示器工业设备视觉便携式系统投影系统视频会议视频通信医用视频成像视频产品视频安全与监视电源管理AC/DC转换器数字电源转换器智能城市电子化政府识别/验证无线基站手持设备工业以太网物联网VR/无人机|智能医疗|5G技术|智能汽车|智能家居|自动化与马达控制|人工智能|智能能源|智能电源|智能可穿戴|智能手机|智能照明 首页 > 新闻 >",
                           'vary=newDate();vargy=y.getYear();vardName=newArray("星期天","星期一","星期二","星期三","星期四","星期五","星期六");varmName=newArray("01","02","03","04","05","06","07","08","09","10","11","12");{document.write("2020年",mName[y.getMonth()],"月",y.getDate(),"日&nbsp;","",dName[y.getDay()]);}']

bad_party_name_list = ["荆楚网", "职业教育", "豪华", "51talk", "新东方在线", "浪潮", "木林森", "推特", "经济日报",
                       "同花顺", "人人网", "人民网", "新华网", "金融界", "财华社", "万润科技", "微博", "视觉中国",
                       "36氪", "可视化", "东方网", "十二年", "新疆生产建设兵团", "qq", "穿山甲", "全景视觉", "决策者", "长江口", "身临其境", "注意力", "纽约时报"]

commodity_list = ["原油", "天然气", "焦炭", "石墨烯", "燃料流", "沥青", "天然橡胶", "纸浆", "白糖", "棉花", "橡胶", "棉", "糙米", "菜籽油", "汽油", "聚乙烯",
                  "鸡蛋", "粳米", "棕榈油", "豆粕", "豆油", "小麦", "大豆", "玉米", "棕榈油", "天胶", "燃油", "塑料", "强麦",
                  "白银", "黄金", "铁矿石", "不锈钢", "热轧卷板", "线材", "螺纹钢", "镍", "锡", "铅", "锌", "铝", "铜"]



# 保存数据成csv文件---
def save_as_csv(filename, header, rows):
    with open(filename, 'w', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(header)
        f_csv.writerows(rows)


# 生成事件因子唯一ID
def hash_sha3_256_ef(title, event_status, time, section_tags, event_tag, assets_ids):
    x = hashlib.sha256()
    x.update(title.encode())
    x.update(str(event_status).encode())
    x.update(time.encode())
    x.update(section_tags.encode())
    x.update(event_tag.encode())
    x.update(assets_ids.encode())
    return x.hexdigest()


# 更新事件因子到数据库---
def update_live_event_factor_to_db(file_name):
    with open(file_name, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        birth_header = next(csv_reader)
        for row in csv_reader:
            insert_live_event_factor(row)


# 将List转换成PG数据库格式--
def list2pgarr(alist):
    pg_list = '{}'
    if len(alist) == 1:
        pg_list = single2pgarr(alist)
    elif len(alist) > 1:
        pg_list = lst2pgarr(alist)
    return pg_list


def lst2pgarr(alist):
    return '{' + ','.join(alist) + '}'


def single2pgarr(alist):
    return '{' + alist[0] + '}'


# 将 taiji 事件标签转换成 xtech 事件标签----
def find_lack_event_tags(event_factor):
    with open(RESOURCE_PATH + "/xtech_event_tags.csv", 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        birth_header = next(csv_reader)
        event_tags = []
        print("taiji event tag: ", str(event_factor[7]))
        if len(str(event_factor[7])) != 0:
            for tag_row in csv_reader:
                if len(str(tag_row[4])) != 0 and str(tag_row[4]) != "" and str(tag_row[4]) != " ":
                    if str(event_factor[7]) == str(tag_row[4]):
                        event_tags.append(str(tag_row[4]))
                        print("xtech 4th-level event tag found: ", str(event_factor[7]))

        if len(event_tags) == 0:
            print("taiji event tag is empty: ", str(event_factor[7]))
            with open(RESOURCE_PATH + "/xtech_event_tags.csv", 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                birth_header = next(csv_reader)
                if len(event_tags) == 0:
                    for tag_row in csv_reader:
                        if len(str(tag_row[3])) != 0 and str(tag_row[3]) != "" and str(tag_row[3]) != " ":
                            if str(event_factor[7]) == str(tag_row[3]):
                                event_tags.append(str(tag_row[3]))
                                print("xtech 3th-level event tag found: ", str(event_factor[7]))

        if len(event_tags) == 0:
            with open(RESOURCE_PATH + "/xtech_event_tags.csv", 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                birth_header = next(csv_reader)
                if len(event_tags) == 0:
                    for tag_row in csv_reader:
                        if len(str(tag_row[2])) != 0 and str(tag_row[2]) != "" and str(tag_row[2]) != " ":
                            if str(event_factor[7]) == str(tag_row[2]):
                                event_tags.append(str(tag_row[2]))
                                print("xtech 2th-level event tag found: ", str(event_factor[7]))

        if len(event_tags) == 0 and len(event_factor[7]) != 0:
            xtech_tag = ""
            with open(RESOURCE_PATH + "/xtech_event_tags_converter.csv", 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                birth_header = next(csv_reader)
                for tag_row in csv_reader:
                    if str(tag_row[1]) == str(event_factor[7]):
                        xtech_tag = str(tag_row[0])
                        print("taiji xtech event tag converter found: ", str(tag_row[0]), str(event_factor[7]))
                if len(xtech_tag) == 0:
                    print("taiji event tag not found: ", event_factor[7])
                    save_unknown_taiji_tag(event_factor[7])
            event_factor[7] = xtech_tag
    return event_factor


# 保存未识别太极标签-----
def save_unknown_taiji_tag(tag):
    with open(RESOURCE_PATH + "/taiji_tags_not_found.txt", "a", encoding='utf-8') as file:
        file.write(str(tag) + "\n")


# 从标题和摘要中搜索是否含有事件标签----
def find_event_tags(event_factor):
    event_tags = []
    if len(str(event_factor[7])) == 0:
        with open(RESOURCE_PATH + "/xtech_event_tags.csv", 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            birth_header = next(csv_reader)
            for tag_row in csv_reader:
                if len(str(tag_row[4])) != 0 and str(tag_row[4]) != "" and str(tag_row[4]) != " ":
                    if str(event_factor[1]).find(str(tag_row[4])) != -1 or str(event_factor[2]).find(
                            str(tag_row[4])) != -1:
                        event_tags.append(str(tag_row[4]))

        if len(event_tags) == 0:
            with open(RESOURCE_PATH + "/xtech_event_tags.csv", 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                birth_header = next(csv_reader)
                for tag_row in csv_reader:
                    if len(str(tag_row[3])) != 0:
                        if str(event_factor[2]).find(str(tag_row[3])) != -1:
                            event_tags.append(str(tag_row[3]))

        if len(event_tags) != 0:
            event_tags = list(set(event_tags))

            if "GDP" in event_tags and len(event_tags) > 1:
                event_tags.remove("GDP")
            if "供给侧" in event_tags and len(event_tags) > 1:
                event_tags.remove("供给侧")
            if "春节" in event_tags and len(event_tags) > 1:
                event_tags.remove("春节")
            if "疫情" in event_tags and len(event_tags) > 1:
                event_tags.remove("疫情")
            if "库存变动" in event_tags and len(event_tags) > 1:
                event_tags.remove("库存变动")

            separator = ','
            event_tag = separator.join(event_tags)
            event_factor[7] = event_tag
            print("xtech event tag found in title & description:", event_factor[1], event_tag)
    return event_factor


# 从标题和摘要中搜索是否含有事件标签关键字----
def find_event_tags_keyword(event_factor):
    if len(str(event_factor[7])) == 0:
        with open(RESOURCE_PATH + "/xtech_event_keywords.csv", 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            birth_header = next(csv_reader)
            for tag_row in csv_reader:
                keyword_list = str(tag_row[1]).split(",")
                for keyword in keyword_list:
                    if str(event_factor[1]).find(str(keyword)) != -1 or str(event_factor[2]).find(str(keyword)) != -1:
                        event_tag = (str(tag_row[0]))
                        print("xtech event tag keyword found:", event_factor[1], event_tag, keyword)
                        event_factor[7] = event_tag
    return event_factor


# 将中文标的转换成回测系统可识别id----
def find_assets_ids(event_factor):
    title = event_factor[1]
    descri = event_factor[2]
    cleaned_party_list = []
    new_party_list = []
    commodity_found = []
    assets_ids_list = []

    if len(str(event_factor[8])) != 0:
        event_factor[8] = event_factor[8].replace("，", ",")
        event_factor[8] = event_factor[8].replace(" ", "")
        party_list = str(event_factor[8]).split(",")
        party_list = party_list[:5]  # todo:为什么取的是前五

        for party_name in party_list:
            # 判断party_name 是否合法，如果不合法那就跳过
            if party_name in bad_party_name_list:  # 如果此name在这个列表中存在就跳过此次循环
                print("bad party name found & removed:", party_name)
                continue
            # 循环遍历某一类型的所有股票，
            # 如果找到相同的，那就将完整的股票代码添加到assets_ids_list列表中
            # 将name添加到cleaned_party_list列表中 todo:添加的意义是什么？
            elif party_name.isdigit():
                print("digital party name found:", party_name)
                code_not_found = True
                # 查找是否和A股中的某一支代码相同
                with open(RESOURCE_PATH + "/xtech_astocks_sum.csv", 'r', encoding='utf-8') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    birth_header = next(csv_reader)
                    for ais_row in csv_reader:
                        code = str(ais_row[1]).split(".")[0]
                        if str(party_name) == code:
                            code_not_found = False
                            print("astocks assets id code found:", party_name, str(ais_row[2]), ais_row[4])
                            assets_ids_list.append(str(ais_row[1]))
                            cleaned_party_list.append(str(ais_row[2]))
                            break
                # 上面如果没找到，执行和上面一样的逻辑
                if code_not_found:
                    with open(RESOURCE_PATH + "/xtech_hstocks_sum.csv", 'r', encoding='utf-8') as csvfile:
                        csv_reader = csv.reader(csvfile)
                        birth_header = next(csv_reader)
                        for ais_row in csv_reader:
                            code = str(ais_row[1]).split(".")[0]
                            if str(party_name) == code:
                                print("hstocks assets id code found:", party_name, str(ais_row[2]), ais_row[4])
                                assets_ids_list.append(str(ais_row[1]))
                                cleaned_party_list.append(str(ais_row[2]))
                                break

            elif ".sh" in party_name:
                code = party_name.split(".")[0] + ".XSHG"
                print("astocks assets id code found:", party_name, code)
                assets_ids_list.append(code)
            elif ".sz" in party_name:
                code = party_name.split(".")[0] + ".XSHE"
                print("astocks assets id code found: ", party_name, code)
                assets_ids_list.append(code)
            elif ".hk" in party_name:
                code = party_name.split(".")[0] + ".XHKG"
                print("hstocks assets id code found: ", party_name, code)
                assets_ids_list.append(code)
            else:
                cleaned_party_list.append(party_name)

        ustocks_assets_id_found = False
        for party_name in cleaned_party_list:
            with open(RESOURCE_PATH + "/xtech_ustocks_sum.csv", 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                birth_header = next(csv_reader)
                for ais_row in csv_reader:
                    if party_name == str(ais_row[2]) or party_name == str(ais_row[3]) or party_name == str(
                            ais_row[4]) or party_name == str(ais_row[6]):
                        print("ustocks assets id found:", party_name, str(ais_row[2]), ais_row[4])
                        assets_ids_list.append(str(ais_row[1]))
                        new_party_list.append(str(ais_row[2]))
                        ustocks_assets_id_found = True
                        break

        if ustocks_assets_id_found:
            event_factor[12] = 3

        hstocks_assets_id_found = False
        for party_name in cleaned_party_list:
            with open(RESOURCE_PATH + "/xtech_hstocks_sum.csv", 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                birth_header = next(csv_reader)
                for ais_row in csv_reader:
                    if party_name == str(ais_row[2]) or party_name == str(ais_row[3]) or party_name == str(
                            ais_row[4]) or party_name == str(ais_row[6]):
                        print("hstocks assets id found:", party_name, str(ais_row[2]), ais_row[4])
                        assets_ids_list.append(str(ais_row[1]))
                        new_party_list.append(str(ais_row[2]))
                        hstocks_assets_id_found = True
                        break

        if hstocks_assets_id_found:
            event_factor[12] = 2

        astocks_assets_id_found = False
        for party_name in cleaned_party_list:
            with open(RESOURCE_PATH + "/xtech_astocks_sum.csv", 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                birth_header = next(csv_reader)
                for ais_row in csv_reader:
                    if party_name == str(ais_row[2]) or party_name == str(ais_row[3]) or party_name == str(
                            ais_row[4]) or party_name == str(ais_row[6]):
                        print("astocks assets id found:", party_name, str(ais_row[2]), ais_row[4])
                        assets_ids_list.append(str(ais_row[1]))
                        new_party_list.append(str(ais_row[2]))
                        astocks_assets_id_found = True
                        break

        for party_name in cleaned_party_list:
            with open(RESOURCE_PATH + "/xtech_index_sum_brief.csv", 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                birth_header = next(csv_reader)
                for iis_row in csv_reader:
                    if party_name == str(iis_row[6]):
                        print("index id found:", party_name, iis_row[5], iis_row[6])
                        assets_ids_list.append(str(iis_row[1]))
                        new_party_list.append(str(iis_row[2]))
                        astocks_assets_id_found = True
                        break

        if astocks_assets_id_found:
            event_factor[12] = 1

    if "概念" in title or "概念" in descri:
        print("Finding astocks concept id")
        with open(RESOURCE_PATH + "/xtech_astocks_concept.csv", 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            birth_header = next(csv_reader)
            theme_num = 0
            for c_row in csv_reader:
                if theme_num > 2:
                    print("theme id exceed: ", title)
                    break
                if str(c_row[2]) in title or str(c_row[2]) in descri:
                    print("theme id found:", str(c_row[2]))
                    assets_ids_list.append(str(c_row[0]))
                    new_party_list.append(str(c_row[2]))
                    theme_num = theme_num + 1

    for com in commodity_list:
        if str(event_factor[1]).find(str(com)) != -1:
            commodity_found.append(com)
            print("commodity assets_id found:", str(com))

    if len(commodity_found) != 0:
        for i in commodity_found:
            new_party_list.append(i)
    new_party_list = list(set(new_party_list))
    event_factor[8] = ','.join(new_party_list)

    if len(assets_ids_list) != 0:
        assets_ids_list = list(set(assets_ids_list))
        assets_id = ','.join(assets_ids_list)
        event_factor[9] = assets_id
        print("assets id found:", event_factor[1], assets_id)
    return event_factor


# 从标题和摘要中搜索是否含有行业标签----
def find_section_tags(event_factor):
    section_tags = []

    if len(str(event_factor[6])) == 0:
        event_factor[6] == str(event_factor[6]).replace("，", ",")
        with open(RESOURCE_PATH + "/xtech_section_tags.csv", 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            birth_header = next(csv_reader)
            for tag_row in csv_reader:
                if len(str(tag_row[4])) != 0:
                    if str(event_factor[2]).find(str(tag_row[4])) != -1:
                        print("4th level section tag found:", event_factor[1], tag_row[4])
                        section_tags.append(str(tag_row[4]))

        if len(section_tags) == 0:
            with open(RESOURCE_PATH + "/xtech_section_tags.csv", 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                birth_header = next(csv_reader)
                for tag_row in csv_reader:
                    if len(str(tag_row[3])) != 0:
                        if str(event_factor[2]).find(str(tag_row[3])) != -1:
                            print("3th level section tag found:", event_factor[1], tag_row[4])
                            section_tags.append(str(tag_row[3]))

        if len(section_tags) == 0:
            with open(RESOURCE_PATH + "/xtech_section_tags.csv", 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                birth_header = next(csv_reader)
                for tag_row in csv_reader:
                    if len(str(tag_row[2])) != 0:
                        if str(event_factor[2]).find(str(tag_row[2])) != -1:
                            print("2th level section tag found:", event_factor[1], tag_row[4])
                            section_tags.append(str(tag_row[2]))

        if len(section_tags) == 0:
            with open(RESOURCE_PATH + "/xtech_section_keywords.csv", 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                birth_header = next(csv_reader)
                for tag_row in csv_reader:
                    keyword_list = str(tag_row[1]).split(",")
                    for keyword in keyword_list:
                        if str(event_factor[1]).find(str(keyword)) != -1 or str(event_factor[2]).find(
                                str(keyword)) != -1:
                            section_tags.append(str(tag_row[0]))
                            print("section tag keyword found:", event_factor[1], str(tag_row[0]), keyword)

    if len(section_tags) != 0:
        section_tags = list(set(section_tags))
        new_section_tags = []

        for tag in section_tags:
            bad_section_tag_not_found = True
            with open(RESOURCE_PATH + "/xtech_section_tags_converter.csv", 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                birth_header = next(csv_reader)
                for tag_row in csv_reader:
                    if str(tag_row[1]) == str(tag):
                        new_section_tags.append(str(tag_row[0]))
                        bad_section_tag_not_found = False
                        print("taiji xtech section tag converter found: ", str(tag_row[0]), str(tag_row[1]))
                        break
            if bad_section_tag_not_found:
                new_section_tags.append(tag)

        separator = ','
        section_tag = separator.join(new_section_tags)
        event_factor[6] = section_tag
        print("xtech section tag found: ", event_factor[1], section_tag)

    return event_factor


# 从标题和摘要中搜索是否含有行业标签关键字---
def find_section_tags_keyword(event_factor):
    return event_factor


# 从标题和摘要中搜索是否含有行业标签关键字----
def find_assets_section_tag(event_factor):
    if len(str(event_factor[6])) == 0 and len(str(event_factor[9])) != 0:
        assets_list = str(event_factor[9]).split(",")
        first_assets = assets_list[0]
        print("find assets section tag: ", first_assets)
        with open(RESOURCE_PATH + "/xtech_astocks_sum.csv", 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            birth_header = next(csv_reader)
            for tag_row in csv_reader:
                if first_assets == str(tag_row[1]):
                    print("assets section tag found:", event_factor[1], tag_row[13])
                    event_factor[6] = tag_row[13]

    if len(str(event_factor[6])) == 0 and len(str(event_factor[9])) != 0:
        assets_list = str(event_factor[9]).split(",")
        first_assets = assets_list[0]
        with open(RESOURCE_PATH + "/xtech_hstocks_sum.csv", 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            birth_header = next(csv_reader)
            for tag_row in csv_reader:
                if first_assets == str(tag_row[1]):
                    print("assets section tag found:", event_factor[1], tag_row[13])
                    event_factor[6] = tag_row[13]

    if len(str(event_factor[6])) == 0 and len(str(event_factor[9])) != 0:
        assets_list = str(event_factor[9]).split(",")
        first_assets = assets_list[0]
        with open(RESOURCE_PATH + "/xtech_ustocks_sum.csv", 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            birth_header = next(csv_reader)
            for tag_row in csv_reader:
                if first_assets == str(tag_row[1]):
                    print("assets section tag keyword found:", event_factor[1], tag_row[13])
                    event_factor[6] = tag_row[13]

    return event_factor


# 清理事件因子标题和描述---
def clean_event(row):
    title = str(row[1])
    descri = str(row[2])
    event_tag = str(row[7])
    event_tag_list = event_tag.split(",")
    new_event_tag_list = []
    party_name = str(row[8])
    assets_ids_list = str(row[9]).split(",")
    new_assets_ids_list = []

    party_name_list = party_name.split(",")

    if len(title) > 80:
        title = title[0:80] + "..."

    for bad_str in bad_description_strings:
        if bad_str in descri:
            descri = descri.replace(bad_str, " ")

    for eventtag in event_tag_list:
        if len(str(eventtag)) != 0 and str(eventtag) != "" and str(eventtag) != " ":
            new_event_tag_list.append(eventtag)

    for assets_id in assets_ids_list:
        if len(str(assets_id)) != 0 and str(assets_id) != "" and str(assets_id) != " ":
            new_assets_ids_list.append(assets_id)

    new_event_tag_list = list(set(new_event_tag_list))
    row[1] = title
    row[2] = descri
    row[7] = ",".join(new_event_tag_list)
    row[8] = ",".join(party_name_list)
    row[9] = ",".join(new_assets_ids_list)

    print("event cleaned:", row[1], row[7], row[8], row[9])

    return row


# 获取事件发生后1天涨跌幅
def gat_day1_change_from_db(assets_id, event_time):
    day1_return = 0

    time_before = event_time + 1 * 86400
    time_after = event_time - 1 * 86400
    try:
        table_name = ""
        if assets_id.startswith('0') or assets_id.startswith('1') or assets_id.startswith('2'):
            table_name = "astocks_daily_factors_02"
        elif assets_id.startswith('3') or assets_id.startswith('4') or assets_id.startswith('5'):
            table_name = "astocks_daily_factors_35"
        elif assets_id.startswith('6') or assets_id.startswith('7') or assets_id.startswith(
                '8') or assets_id.startswith('9'):
            table_name = "astocks_daily_factors_69"
        elif assets_id[0].isalpha():
            table_name = "astocks_daily_factors_az"

        conn = psycopg2.connect(database=REMOTE_DATABASE, user=REMOTE_USER, password=REMOTE_PASSWORD,
                                host=REMOTE_HOST,
                                port=REMOTE_PORT)
        # 获得游标对象
        cursor = conn.cursor()

        sql = "select * from " + table_name + " where assets_id = '%s' and datetime > %d and datetime < %d order by datetime;" % (
        assets_id, time_after, time_before)

        cursor.execute(sql)
        results = cursor.fetchall()

        conn.close()
        day1_return = results[0][5]
        print("get day1return success", day1_return)
    except:
        print("failed to get day1 return")
    return day1_return


# 获取事件发生1天涨跌幅
def get_assets_day1_change_from_uqer(assets_id, occurred_timestamp):
    s_time = time.localtime(occurred_timestamp - 10 * 86400)
    e_time = time.localtime(occurred_timestamp + 86400)

    start_date = time.strftime("%Y-%m-%d", s_time)
    end_date = time.strftime("%Y-%m-%d", e_time)

    day1_change = 0.0
    if assets_id.endswith(".XSHE") or assets_id.endswith(".XSHG"):
        astocks = DataAPI.MktEqudGet(secID=assets_id, ticker=u"", tradeDate=u"", beginDate=start_date, endDate=end_date,
                                     isOpen="", field=u"", pandas="1")
        if str(astocks['chgPct'][0]) != 'NaN' and str(astocks['chgPct'][0]) != 'nan':
            day1_change = astocks['chgPct'][0]
    elif assets_id.endswith(".XHKG"):
        hstocks = DataAPI.MktHKEqudGet(secID=assets_id, ticker=u"", tradeDate=u"", beginDate=start_date,
                                       endDate=end_date, field=u"", pandas="1")
        if str(hstocks['chgPct'][0]) != 'NaN' and str(hstocks['chgPct'][0]) != 'nan':
            day1_change = hstocks['chgPct'][0]
    elif assets_id.endswith(".OTER") or assets_id.endswith(".ZICN"):
        aindex = DataAPI.MktInstEqudGet(industrySymbol=u"", secID=assets_id, indexSymbol=u"", tradeDate=u"",
                                        industryID=u"", beginDate=start_date, endDate=end_date, field=u"", pandas="1")
        if str(aindex['chgPct'][0]) != 'NaN' and str(aindex['chgPct'][0]) != 'nan':
            day1_change = aindex['chgPct'][0]
    return day1_change


def find_event_factor_ext_info(assets_ids_list, section_tags_list, occurred_timestamp):
    for section_tag in section_tags_list:
        with open(RESOURCE_PATH + "/xtech_index_sum_brief.csv", 'r', encoding='utf-8') as csvfile6:
            csv_reader6 = csv.reader(csvfile6)
            birth_header = next(csv_reader6)
            for cis_row in csv_reader6:
                if section_tag == str(cis_row[6]):
                    assets_ids_list.append(cis_row[1])
                    break
    assets_ids_list = list(set(assets_ids_list))
    assets_ids_list = [x for x in assets_ids_list if x != '']

    ext_infos = []
    for assets_id in assets_ids_list:
        print("finding ext_info: ", assets_id)
        with open(RESOURCE_PATH + "/xtech_astocks_sum.csv", 'r', encoding='utf-8') as csvfile1, \
                open(RESOURCE_PATH + "/xtech_index_sum_brief.csv", 'r', encoding='utf-8') as csvfile2, \
                open(RESOURCE_PATH + "/xtech_hstocks_sum.csv", 'r', encoding='utf-8') as csvfile3, \
                open(RESOURCE_PATH + "/xtech_ustocks_sum.csv", 'r', encoding='utf-8') as csvfile4, \
                open(RESOURCE_PATH + "/xtech_astocks_concept.csv", 'r', encoding='utf-8') as csvfile5:
            csv_reader1 = csv.reader(csvfile1)
            birth_header = next(csv_reader1)
            csv_reader2 = csv.reader(csvfile2)
            birth_header = next(csv_reader2)
            csv_reader3 = csv.reader(csvfile3)
            birth_header = next(csv_reader3)
            csv_reader4 = csv.reader(csvfile4)
            birth_header = next(csv_reader4)
            csv_reader5 = csv.reader(csvfile5)
            birth_header = next(csv_reader5)

            print("finding ext_info astocks day1change")
            for ais_row in csv_reader1:
                if assets_id == str(ais_row[1]):
                    day1_return = get_assets_day1_change_from_uqer(assets_id, occurred_timestamp)
                    print("astocks id found: ", str(ais_row[2]), str(ais_row[1]))
                    ext_info = "1|" + str(ais_row[2]) + "|" + str(ais_row[1]) + "|" + str(day1_return)
                    ext_infos.append(ext_info)
                    break
            print("finding ext_info aindex day1change")
            for iis_row in csv_reader2:
                if assets_id == str(iis_row[1]):
                    day1_return = get_assets_day1_change_from_uqer(assets_id, occurred_timestamp)
                    print("aindex id found :", iis_row[2], iis_row[1])
                    ext_info = "2|" + str(iis_row[6]) + "|" + str(iis_row[1]) + "|" + str(day1_return)
                    ext_infos.append(ext_info)
                    break
            print("finding ext_info hstocks day1change")
            for his_row in csv_reader3:
                if assets_id == str(his_row[1]):
                    day1_return = get_assets_day1_change_from_uqer(assets_id, occurred_timestamp)
                    print("hstocks id found: ", str(his_row[2]), str(his_row[1]))
                    ext_info = "1|" + str(his_row[2]) + "|" + str(his_row[1]) + "|" + str(day1_return)
                    ext_infos.append(ext_info)
                    break
            print("finding ext_info ustocks day1change")
            for uis_row in csv_reader4:
                if assets_id == str(uis_row[1]):
                    # day1_return = gat_day1_change_from_db(assets_id, time)
                    print("ustocks id found: ", str(uis_row[2]), str(uis_row[1]))
                    ext_info = "1|" + str(uis_row[2]) + "|" + str(uis_row[1]) + "|0.0"
                    ext_infos.append(ext_info)
                    break
            print("finding ext_info concept day1change")
            for tis_row in csv_reader5:
                if assets_id == str(tis_row[0]):
                    day1_return = gat_day1_change_from_db(assets_id, occurred_timestamp)
                    print("concept id found: ", str(tis_row[2]), str(tis_row[0]))
                    ext_info = "2|" + str(tis_row[2]) + "|" + str(tis_row[0]) + "|" + str(day1_return)
                    ext_infos.append(ext_info)
                    break

    return assets_ids_list, ext_infos


# 插入标的信息到数据库---
def insert_live_event_factor(row):
    section_tags_list = row[5].split(",")
    event_tag_list = row[6].split(",")
    party_names_list = row[7].split(",")
    assets_ids_list = row[8].split(",")
    occurred_timestamp = int(datetime.datetime.strptime(str(row[4]), "%Y-%m-%d %H:%M:%S").timestamp()) + 28800

    try:
        assets_ids_list, ext_info_list = find_event_factor_ext_info(assets_ids_list, section_tags_list,
                                                                    occurred_timestamp)
        assets_ids_pg_list = list2pgarr(assets_ids_list)
        section_tags_pg_list = list2pgarr(section_tags_list)
        ext_info_pg_list = list2pgarr(ext_info_list)
        event_tags_pg_list = list2pgarr(event_tag_list)
        party_names_pg_list = list2pgarr(party_names_list)

        conn = psycopg2.connect(database=REMOTE_DATABASE, user=REMOTE_USER, password=REMOTE_PASSWORD,
                                host=REMOTE_HOST,
                                port=REMOTE_PORT
                                )
        # 获得游标对象
        cursor = conn.cursor()

        hash_id = hash_sha3_256_ef(row[0], row[12], row[4], row[5], row[6], row[8])
        print("before insert xtech_event_factors into db: ", hash_id, row[12], row[0], row[1], row[9], row[10], row[11],
              row[2], row[3],
              section_tags_pg_list, event_tags_pg_list, party_names_pg_list, assets_ids_pg_list,
              ext_info_pg_list, occurred_timestamp)

        sql = "insert into xtech_event_factors (hash_id, event_status, title, description, sentiment, " \
              "attention, market_type, media_source, source_url, section_tags, event_tags, " \
              "party_names, assets_ids, ext_info, occurred_at) \
              VALUES ('%s', %s, '%s', '%s', %s, %s, %s, '%s', '%s', %r, %r, %r, %r, %r, %s)" % \
              (hash_id, row[12], row[0], row[1], row[9], row[10], row[11], row[2], row[3],
               section_tags_pg_list, event_tags_pg_list, party_names_pg_list, assets_ids_pg_list,
               ext_info_pg_list, occurred_timestamp)

        cursor.execute(sql)
        print("updated successfully: ", section_tags_pg_list, event_tags_pg_list, party_names_pg_list,
              assets_ids_pg_list, ext_info_pg_list)
        # 事物提交
        conn.commit()
        # 关闭数据库连接
        conn.close()
    except psycopg2.Error as e:
        print("Error database ", e)
    except (SyntaxError, KeyError, RuntimeError, IndexError, AttributeError, ValueError)as e:
        print("Error format", e)
    except:
        print("Error unknown ")


# 进度条
def progress(filename, size, sent):
    print("%s\'s progress: %.2f%%   \r" % (filename, float(sent) / float(size) * 100))


# 服务器下载taiji文件----
def download_latest_event(remote_file, local_path):
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect('175.25.50.117', 12672, 'root', 'root1234', banner_timeout=3600)

    # SCPCLient takes a paramiko transport as an argument
    scp = SCPClient(ssh.get_transport(), progress=progress)

    remote_path = '/root/event_driven/' + remote_file
    scp.get(remote_path, local_path)  # 从服务器中获取文件

    scp.close()


# 服务器下载市场机会文件并转换成事件因子----
def update_last_save_market_opp_event_to_db():
    # local_file = "/Users/cheney/cheney/code/eventar/xcollect/resource2/mo_last_save.csv"
    local_file = RESOURCE_PATH2 + "/mo_last_save.csv"
    download_latest_event("output_data/market_opportunity/last_save.csv", local_file)
    converted_file = RESOURCE_PATH2 + "/mo_ef.csv"
    convert_market_opp_to_event_factor(local_file, converted_file)
    # update_live_event_factor_to_db(converted_file)


# 将市场机会文件转换成事件因子---
def convert_market_opp_to_event_factor(src, dst):
    with open(src, 'r', encoding='utf-8') as csvfile:
        csv.field_size_limit(500 * 1024 * 1024)
        csv_reader = csv.reader(csvfile)
        birth_header = next(csv_reader)
        ef_list = []

        for row in csv_reader:
            try:
                party_names = []
                party_names_json_str = str(row[24])
                party_names_json_str = party_names_json_str.replace("\'", "\"")
                party_names_json = json.loads(party_names_json_str)

                for party_name_json in party_names_json:
                    party_names.append(party_name_json['name'])

                party_name = ",".join(party_names)
                if len(row[28]) == 0:
                    row[28] = row[26]
                # id, title, description, media_source, url, publish_time, section_tag, event_tag, party_name, assets_ids, sentiment_score, attention_score, market_type,event_status
                new_row = [row[2], row[26], row[28], row[34], row[25], row[21], row[35], row[29], party_name, "",
                           row[32], row[33], row[31], row[30]]

                new_row = find_lack_event_tags(new_row)
                # new_row = find_event_tags(new_row)
                # new_row = find_event_tags_keyword(new_row)
                new_row = find_assets_ids(new_row)
                new_row = find_section_tags(new_row)
                new_row = find_section_tags_keyword(new_row)
                new_row = find_assets_section_tag(new_row)
                new_row = clean_event(new_row)

                if new_row is not None:
                    # title, description, media_source, url, publish_time, section_tag, event_tag, party_name, assets_id, sentiment_score, attention_score, market_type, event_status
                    new_ef = (
                    new_row[1], new_row[2], new_row[3], new_row[4], new_row[5], new_row[6], new_row[7], new_row[8],
                    new_row[9], new_row[10], new_row[11], new_row[12], new_row[13])
                    ef_list.append(new_ef)

            except IndexError:
                print("Except IndexError 数据格式错误: ")
        save_as_csv(dst, live_ef_headers, ef_list)


# 服务器下载近期风口文件并转换成事件因子----
def update_last_save_hot_plate_event_to_db():
    local_file = RESOURCE_PATH2 + "/hp_last_save.csv"
    download_latest_event("output_data/hot_plates/last_save.csv", local_file)
    converted_file = RESOURCE_PATH2 + "/hp_ef.csv"
    convert_hot_plate_to_event_factor(local_file, converted_file)
    # update_live_event_factor_to_db(converted_file)


# 将市场机会文件转换成事件因子---
def convert_hot_plate_to_event_factor(src, dst):
    with open(src, 'r', encoding='utf-8') as csvfile:
        csv.field_size_limit(500 * 1024 * 1024)
        csv_reader = csv.reader(csvfile)
        birth_header = next(csv_reader)
        ef_list = []

        for row in csv_reader:
            try:
                # id, title, description, media_source, url, publish_time, section_tag, event_tag, party_name, assets_ids, sentiment_score, attention_score, market_type,event_status
                new_row = [row[0], row[4], row[4], "交叉科技", "", row[2], row[3], "", row[1], "", 1, row[5], 1, 13]

                new_row = find_lack_event_tags(new_row)
                new_row = find_event_tags(new_row)
                new_row = find_event_tags_keyword(new_row)
                new_row = find_assets_ids(new_row)
                new_row = find_section_tags(new_row)
                new_row = find_section_tags_keyword(new_row)
                new_row = find_assets_section_tag(new_row)
                new_row = clean_event(new_row)

                if new_row is not None:
                    # title, description, media_source, url, publish_time, section_tag, event_tag, party_name, assets_id, sentiment_score, attention_score, market_type, event_status
                    new_ef = (
                    new_row[1], new_row[2], new_row[3], new_row[4], new_row[5], new_row[6], new_row[7], new_row[8],
                    new_row[9], new_row[10], new_row[11], new_row[12], new_row[13])
                    ef_list.append(new_ef)

            except IndexError:
                print("Except IndexError 数据格式错误: ")
        save_as_csv(dst, live_ef_headers, ef_list)


# 服务器下载近期风口文件并转换成事件因子----
def update_last_save_robot_news_event_to_db():
    local_file = RESOURCE_PATH2 + "/rb_last_save.csv"
    download_latest_event("output_data/robot_news/robot_news_taged.csv", local_file)
    converted_file = RESOURCE_PATH2 + "/rb_ef.csv"
    convert_robot_to_event_factor(local_file, converted_file)
    # update_live_event_factor_to_db(converted_file)


# 将市场机会文件转换成事件因子----
def convert_robot_to_event_factor(src, dst):
    with open(src, 'r', encoding='utf-8') as csvfile:
        csv.field_size_limit(500 * 1024 * 1024)
        csv_reader = csv.reader(csvfile)
        birth_header = next(csv_reader)
        ef_list = []

        for row in csv_reader:
            try:

                if len(str(row[2])) == 0:
                    row[2] = row[1]
                status = row[9]
                attention = 2
                if status == 34 or status == 17:
                    attention = 3

                # Unnamed: 0,title,description,media_source,url,publish_time,market_type,sentiment,attention,data_status,section_tags,event_tags,party_name,section_tag,risk,event_tag
                # id, title, description, media_source, url, publish_time, section_tag, event_tag, party_name, assets_ids, sentiment_score, attention_score, market_type,event_status
                new_row = [row[0], row[1], row[2], row[3], row[4], row[5], row[10], row[11], row[12], "", row[7],
                           attention, row[6], 34]
                new_row = find_lack_event_tags(new_row)
                new_row = find_assets_ids(new_row)
                new_row = find_section_tags(new_row)
                new_row = find_section_tags_keyword(new_row)
                new_row = find_assets_section_tag(new_row)
                new_row = clean_event(new_row)

                if new_row is not None:
                    # title, description, media_source, url, publish_time, section_tag, event_tag, party_name, assets_id, sentiment_score, attention_score, market_type, event_status
                    new_ef = (
                    new_row[1], new_row[2], new_row[3], new_row[4], new_row[5], new_row[6], new_row[7], new_row[8],
                    new_row[9], new_row[10], new_row[11], new_row[12], new_row[13])
                    ef_list.append(new_ef)

            except IndexError:
                print("Except IndexError 数据格式错误: ")
        save_as_csv(dst, live_ef_headers, ef_list)


# 服务器下载近期风口文件并转换成事件因子---
def update_last_save_easy_money_news_event_to_db():
    local_file = RESOURCE_PATH2 + "/em_last_save.csv"
    download_latest_event("output_data/eastmoney_live/xy_last_save.csv", local_file)
    converted_file = RESOURCE_PATH2 + "/em_ef.csv"
    convert_easy_money_to_event_factor(local_file, converted_file)
    update_live_event_factor_to_db(converted_file)


# 将市场机会文件转换成事件因子----
def convert_easy_money_to_event_factor(src, dst):
    with open(src, 'r', encoding='utf-8') as csvfile:
        csv.field_size_limit(500 * 1024 * 1024)
        csv_reader = csv.reader(csvfile)
        birth_header = next(csv_reader)
        ef_list = []

        # ,title,description,media_source,url,publish_time,market_type,sentiment,attention,data_status,section_tags,event_tags,party_name,section_tag

        for row in csv_reader:
            try:
                # id, title, description, media_source, url, publish_time, section_tag, event_tag, party_name, assets_ids, sentiment_score, attention_score, market_type,event_status
                new_row = [row[0], row[1], row[2], row[3], row[4], row[5], row[13], row[11], row[12], "", row[7],
                           row[8], row[6], row[9]]

                new_row = find_lack_event_tags(new_row)
                new_row = find_event_tags(new_row)
                new_row = find_event_tags_keyword(new_row)
                new_row = find_assets_ids(new_row)
                new_row = find_section_tags(new_row)
                new_row = find_section_tags_keyword(new_row)
                new_row = find_assets_section_tag(new_row)
                new_row = clean_event(new_row)

                if new_row is not None:
                    # title, description, media_source, url, publish_time, section_tag, event_tag, party_name, assets_id, sentiment_score, attention_score, market_type, event_status
                    new_ef = (
                    new_row[1], new_row[2], new_row[3], new_row[4], new_row[5], new_row[6], new_row[7], new_row[8],
                    new_row[9], new_row[10], new_row[11], new_row[12], new_row[13])
                    ef_list.append(new_ef)

            except IndexError:
                print("Except IndexError 数据格式错误: ")
        save_as_csv(dst, live_ef_headers, ef_list)


# 服务器下载近期风口文件并转换成事件因子---
def update_last_save_limitup_news_event_to_db():
    # local_file = "/Users/cheney/cheney/code/eventar/xcollect/resource2/lu_live_new.csv"
    local_file = RESOURCE_PATH2 + "/lu_last_save.csv"
    download_latest_event("output_data/limit_up_pool/last_save.csv", local_file)
    converted_file = RESOURCE_PATH2 + "/lu_ef.csv"
    convert_limitup_to_event_factor(local_file, converted_file)
    # update_live_event_factor_to_db(converted_file)


# 下载并转化实时大涨事件
# 将市场机会文件转换成事件因子--
def convert_limitup_to_event_factor(src, dst):
    with open(src, 'r', encoding='utf-8') as csvfile:
        csv.field_size_limit(500 * 1024 * 1024)
        csv_reader = csv.reader(csvfile)
        birth_header = next(csv_reader)
        ef_list = []

        for row in csv_reader:
            try:
                description = row[6] + row[7] + row[8]
                if len(description) == 0:
                    description = row[1]
                new_row = [row[0], row[1], description, "交叉科技", "", row[2], "", row[5], row[3], "", 1, 2, 1, 5]
                new_row = find_assets_ids(new_row)
                new_row = find_assets_section_tag(new_row)
                new_row = clean_event(new_row)

                if new_row is not None:
                    # title, description, media_source, url, publish_time, section_tag, event_tag, party_name, assets_id, sentiment_score, attention_score, market_type, event_status
                    new_ef = (
                    new_row[1], new_row[2], new_row[3], new_row[4], new_row[5], new_row[6], new_row[7], new_row[8],
                    new_row[9], new_row[10], new_row[11], new_row[12], new_row[13])
                    ef_list.append(new_ef)

            except IndexError:
                print("Except IndexError 数据格式错误: ")
        save_as_csv(dst, live_ef_headers, ef_list)


# 服务器下载近期风口文件并转换成事件因子----
def update_last_save_post_event_to_db():
    # local_file = "/Users/cheney/cheney/code/eventar/xcollect/resource2/lu_live_new.csv"
    local_file = RESOURCE_PATH2 + "/post_last_save.csv"
    # download_latest_event("output_data/xuangubao_posts/last_save.csv", local_file)
    download_latest_event("output_data/xuangubao_posts/live_news.csv", local_file)
    converted_file = RESOURCE_PATH2 + "/post_ef.csv"
    convert_post_to_event_factor(local_file, converted_file)
    update_live_event_factor_to_db(converted_file)


# 将市场机会文件转换成事件因子----
def convert_post_to_event_factor(src, dst):
    with open(src, 'r', encoding='utf-8') as csvfile:
        csv.field_size_limit(500 * 1024 * 1024)
        csv_reader = csv.reader(csvfile)
        birth_header = next(csv_reader)
        ef_list = []

        # ,title,description,media_source,url,publish_time,market_type,sentiment,attention,data_status,section_tags,event_tags,party_name
        for row in csv_reader:
            try:
                # id, title, description, media_source, url, publish_time, section_tag, event_tag, party_name, assets_ids, sentiment_score, attention_score, market_type,event_status
                new_row = [row[0], row[1], row[2], row[3], row[4], row[5], row[10], row[11], row[12], "", 1, row[7], 2,
                           row[9]]
                new_row = find_assets_ids(new_row)
                new_row = find_section_tags(new_row)
                new_row = find_assets_section_tag(new_row)
                new_row = clean_event(new_row)

                if new_row is not None:
                    # title, description, media_source, url, publish_time, section_tag, event_tag, party_name, assets_id, sentiment_score, attention_score, market_type, event_status
                    new_ef = (
                    new_row[1], new_row[2], new_row[3], new_row[4], new_row[5], new_row[6], new_row[7], new_row[8],
                    new_row[9], new_row[10], new_row[11], new_row[12], new_row[13])
                    ef_list.append(new_ef)

            except IndexError:
                print("Except IndexError 数据格式错误: ")
        save_as_csv(dst, live_ef_headers, ef_list)


# 每日3点实时更新最新数据
def hourly_update():
    now_time = datetime.datetime.now()

    print("begin to update event: ", now_time)

    client = Client(token=UQ_TOKEN)
    update_last_save_limitup_news_event_to_db()  # 下载并转化实时大涨事件
    update_last_save_market_opp_event_to_db()  # 下载并转化最新机会
    update_last_save_easy_money_news_event_to_db()  # 下载并转化事件快讯
    update_last_save_hot_plate_event_to_db()  # 下载并转化近期风口
    update_last_save_robot_news_event_to_db()  # 下载并转化风险预警
    update_last_save_post_event_to_db()  # 下载并转化

    print("daily update event success: ", now_time)

    auto_update(hourly_update, day=1, appoint_hour='03')
    # 如果需要循环调用，就要添加以下方法
    # timer = threading.Timer(3600, hourly_update)
    # timer.start()
#

if __name__ == '__main__':
    auth('18846444159', 'aA1192338674')
    client = Client(token=UQ_TOKEN)

    # update_last_save_limitup_news_event_to_db()
    # update_last_save_market_opp_event_to_db()
    update_last_save_easy_money_news_event_to_db()
    # update_last_save_hot_plate_event_to_db()
    # update_last_save_robot_news_event_to_db()
    # update_last_save_post_event_to_db()
    # converted_file = RESOURCE_PATH2 + "/post_ef.csv"
    # update_live_event_factor_to_db(converted_file)
