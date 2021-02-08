# -*- coding: utf-8 -*-
'''
67948 Yu Junhao

Action1：汽车投诉信息采集：
数据源：http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml
投诉编号，投诉品牌，投诉车系，投诉车型，问题简述，典型问题，投诉时间，投诉状态
'''
import requests 
from bs4 import BeautifulSoup as bs
import pandas as pd

page_total=int(input('输入需要翻页的次数:'))
# 请求URL
url1 = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
#添加请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
	}
# 创建DataFrame
df = pd.DataFrame(columns = ['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
for page in range(0,page_total):
    url=url1+str(page+1)+'.shtml'
    html=requests.get(url,headers=headers,timeout=10)
    content = html.text
    # 通过content创建BeautifulSoup对象
    soup = bs(content, 'html.parser', from_encoding='utf-8')
    # 找到完整的投诉信息框
    temp = soup.find('div',class_="tslb_b")
    
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        print(tr.type)
        if (len(tr.find_all('td'))):#判断list是否为空，防溢出
            id=tr.find_all('td')[0].get_text()
            brand=tr.find_all('td')[1].get_text()
            car_model=tr.find_all('td')[2].get_text()
            type=tr.find_all('td')[3].get_text()
            desc=tr.find_all('td')[4].get_text()
            problem=tr.find_all('td')[5].get_text()
            datetime=tr.find_all('td')[6].get_text()
            status=tr.find_all('td')[7].get_text()
            #追加一行
            df=df.append(pd.Series(dict(zip(df.columns, [id,brand,car_model,type,desc,problem,datetime,status]))), ignore_index=True)
            
print(df)
df.to_excel('CompainCollection.xls')