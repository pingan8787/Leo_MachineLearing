import pandas as pd
import os
import get_house
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# @配置项
saveFileName = 'house_data.csv' # 读取的文件名
filename = 'G:/www/python/pacong/demo_house'+saveFileName # 读取文件的路径

# @检查文件是否存在，不存在则运行爬虫程序获得数据
def check_file(filename):    
    if os.path.exists(filename):        
        print('------数据文件已存在------')        
        house_data = pd.read_csv(filename, encoding = 'gbk', sep = ',')        
        return house_data    
    else:        
        print('------文件不存在，运行爬虫程序对信息进行爬取------')        
        get_house.main()        
        house_data = pd.read_csv(filename, encoding = 'gbk', sep= ',')            
        return house_data

# @查看数据集的基本信息
def data_info(data_set):    
    print('-----数据集基本信息-----')    
    data_set.info()    
    print('-----预览数据-----\n',data_set.head())

# @将字符串转换成数字
def data_adj(area_data, str):    
    if str in area_data :        
        return float(area_data[0 : area_data.find(str)])    
    else :        
        return None

# @主函数
def main():    
    #查看数据文件是否存在
    house_data = check_file(filename)
    #查看数据基本信息    
    data_info(house_data)
    #将数据从字符串提取出来    
    house_data['area_adj'] = house_data['house_area'].apply(data_adj,str = '平米')    
    house_data['interest_adj'] =  house_data['house_interest'].apply(data_adj,str = '人')  
    #画图时显示中文和负号    
    plt.rcParams['font.sans-serif'] = ['SimHei']    
    plt.rcParams['axes.unicode_minus'] = False

    # @户型和关注人数分布
    fig, ax1 = plt.subplots(1,1)    
    type_interest_group = house_data['interest_adj'].groupby(house_data['house_type']).agg([('户型', 'count'), ('关注人数', 'sum')])    
    #取户型>50的数据进行可视化
    ti_sort = type_interest_group[type_interest_group['户型'] > 50].sort_values(by='户型')    
    ti_sort.plot(kind='barh', alpha=0.7, grid=True, ax=ax1)    
    plt.title('二手房户型和关注人数分布')    
    plt.ylabel('户型') 
    plt.show() 
# ![二手房户型和关注人数分布](http://upload-images.jianshu.io/upload_images/4043796-c0dd3dd1c64444e5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
# 由上图可以知道，广州二手房户型都集中在3室2厅、2室1厅和2室2厅，而且它们的关注人数也是最多的。其中可以看到2室1厅虽然数量比3室2厅少，但是关注人数却比3室2厅多。

    # @二手房面积分析
    # @面积分布    
    fig,ax2 = plt.subplots(1,1)    
    area_level = [0, 50, 100, 150, 200, 250, 300, 500]    
    label_level = ['小于50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350']    
    area_cut = pd.cut(house_data['area_adj'], area_level, labels=label_level)        
    area_cut.value_counts().plot(kind='bar', rot=30, alpha=0.4, grid=True, fontsize='small', ax=ax2)    
    plt.title('二手房面积分布')    
    plt.xlabel('面积')    
    plt.legend(['数量'])    
    plt.show() 

# ![二手房面积分布](http://upload-images.jianshu.io/upload_images/4043796-1bcf27f753f15ff9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
# 从二手房的面积分布可以知道，广州二手房面积在50平米-100平米的占比最大。

    # @聚类分析
    # @对二手房价格、关注人数、面积进行Kmeans聚类
    print('-----开始聚类分析-----')    
    # 缺失值处理:直接将缺失值去掉    
    cluster_data = house_data[['interest_adj','area_adj','house_price']].dropna()    
    #将簇数设为3    
    K_model = KMeans(n_clusters=3)    
    alg = K_model.fit(cluster_data)    
    print('------聚类中心------')    
    center = pd.DataFrame(alg.cluster_centers_, columns=['关注人数','面积','房价'])    
    cluster_data['label'] = alg.labels_
    print(center)
   
if __name__ == '__main__':
main()