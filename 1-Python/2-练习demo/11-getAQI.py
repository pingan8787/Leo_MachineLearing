
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
from pyecharts import Page,Bar,Pie,Geo

'''
pyecharts : pip install pyecharts http://pyecharts.org/#/
可能还需要安装 pyecharts_snapshot
BeautifulSoup : pip install beautifulsoup4
生成图片的插件 ： pip install pyecharts-snapshot
'''

def getAirData():
    # 获取空气质量数据
    air_head = [] # 空气指标标题
    air_data = [] # 空气指数数据
    response = requests.get('http://www.pm25.in/rank').text # 获取页面
    soup = BeautifulSoup(response,'lxml') # 解析网页

    ths = soup.find('thead').find('tr').find_all('th') # 获取空气指标标题
    for th in ths :
        air_head.append(th.get_text().replace('\n','').replace(' ',''))

    trs = soup.find('tbody').find_all('tr') # 获取空气质量数据
    for tr in trs :
        tmp = []
        tds = tr.find_all('td')
        for td in tds :
            tmp.append(td.get_text())
        air_data.append(tmp)
    return DataFrame(air_data,columns = air_head) # 转化为DataFrame类型

def DrawAQIBar(air_data):
    # 绘制前十名城市和后十名城市的空气质量AQI柱状图
    page = Page()
    bar1 = Bar("前十名空气质量指数AQI")
    bar1.add(
        "AQI",
        air_data["城市"][:10],air_data["AQI"][:10],
        mark_line = ["average"],
        mark_point = ["max", "min"],
        is_label_show = True,
        yaxis_min = 0,
        yaxis_max = 250
    )
    page.add(bar1)
    bar2 = Bar("后十名空气质量指数AQI")
    bar2.add(
        "AQI",
        air_data["城市"][-10:],air_data["AQI"][-10:],
        mark_line = ["average"],
        mark_point = ["max", "min"],
        is_label_show = True,
        yaxis_min = 0,
        yaxis_max = 250
    )
    page.add(bar2)
    page.render()

def DrawAQIPie(air_data):
    # 绘制全国373个主要城市空气质量指数类别饼形图
    # 按照空气质量指数类别进行分组统计
    AQIRank = dict(air_data.groupby("空气质量指数类别")["空气质量指数类别"].count())
    pie = Pie('全国主要城市空气质量指数类别')
    pie.add(
        "空气质量指数类别",
        AQIRank.keys(),
        AQIRank.values(),
        is_label_show=True
    )
    pie.render()

def DrawAQIGeo(air_data) :
    # 绘制钱50名城市和后50名城市的pm2.5地理图
    geo = Geo(
        "全国主要城市PM2.5",
        title_color = "#fff",
        title_pos = "left",
        width = 800,height = 600,
        background_color="#404a59"
    )
    geo.add(
        "PM2.5",
        air_data["城市"][:50],
        air_data["PM2.5细颗粒物"][:50],
        visual_range=[0, 150],
        visual_text_color="#fff",
        symbol_size = 15,
        is_visualmap = True,
    )
    geo.add(
        "PM2.5",
        air_data["城市"][-50:],
        air_data["PM2.5细颗粒物"][-50:],
        visual_range=[0, 150],
        visual_text_color="#aaa",
        symbol_size = 15,
        is_visualmap = True,
        label_clor="#aaa"
    )
    geo.render()

if __name__ == "__main__":
    air_data = getAirData()
    # DrawAQIBar(air_data)
    # DrawAQIPie(air_data)
    DrawAQIGeo(air_data)

