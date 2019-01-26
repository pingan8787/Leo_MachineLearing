#-*- coding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib import pyplot

# @配置项
saveFileName = 'house_data.csv' # 保存的文件名
filename = 'G:/www/python/pacong/demo_house'+saveFileName # 保存文件的路径
pageNum = 100  # 总共读取的页数


# @伪装浏览器访问  
def inBorwer():   
    header = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')    
    #@伪装浏览器    
    opener = urllib.request.build_opener()    
    opener.addheaders = [header]    
    #将伪装浏览器设为全局，这样在后续对网页的访问就可以直接使用urlopen  
    urllib.request.install_opener(opener)

# @获取网页内容
def getPage(url,num):   
    try:        
        #获取网页的内容，并使用BeautifulSoup解析以便后面的信息提取          
        page = urllib.request.urlopen(url).read()        
        soup = BeautifulSoup(page, 'lxml')        
        print('--------第%d页抓取成功--------'%num)        
        return soup    
    except urllib.request.URLError as e:        
        if hasattr(e,'code'):            
            print('错误原因：',e.code)        
        if hasattr(e,'reason'):            
            print('错误原因：',e.reason)
            

# @提取网页中的房子信息，并把信息以DataFrame的形式返回
def getInfo(page):   
    item = {}    
    item['house_name'] = [i.get_text().strip().split('|')[0] for i in page.select('div[class="houseInfo"]')]    #  房名
    item['house_type'] = [i.get_text().strip().split('|')[1] for i in page.select('div[class="houseInfo"]')]    #户型
    item['house_area'] = [i.get_text().strip().split('|')[2] for i in page.select('div[class="houseInfo"]')]    #面积
    item['house_interest'] = [i.get_text().strip().split('/')[0] for i in page.select('div[class="followInfo"]')]    #关注人数
    item['house_see'] = [i.get_text().strip().split('/')[1] for i in page.select('div[class="followInfo"]')]    #带看人数
    item['house_issuedate'] = [i.get_text().strip().split('/')[2] for i in page.select('div[class="followInfo"]')]    #发布时间
    item['house_price'] = [i.get_text().strip() for i in page.select('div[class="totalPrice"] span')]    #房价
    item['house_unit_price'] = [i.get_text().strip() for i in page.select('div[class="unitPrice"] span')]    #单位价格
    return pd.DataFrame(item)

# @主函数 
def main():    
    inBorwer()    
    house_data = []    
    #二手房网页总共只有100页，这里可以使用一个for循环对网址进行更新    
    for pg in range(1,pageNum+1):        
        lianjia_url = 'http://xm.lianjia.com/ershoufang/pg' + str(pg) +'/'        
        page = getPage(lianjia_url,pg)        
        if len(page) > 0:            
            house_info = getInfo(page)            
            #把每一页提取到的信息都存在一个list里面              
            house_data.append(house_info)    
            #对list里的DataFrame进行纵向拼接    
    data = pd.concat(house_data, ignore_index = True)    
    #将信息保存到CSV文件中    
    data.to_csv(filename, encoding = 'gbk', index = False)    
    print('------写入完毕------')

if __name__ == '__main__':    
    main()