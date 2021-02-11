#Step1，数据加载
import pandas as pd
df=pd.read_csv('./car_complain.csv')
#print(df)
df.to_excel('./car_complain.xls', index=False)

#Step2，数据预处理
#拆分problem类型 => 多个字段
df=df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))
print(df)

#Step3，数据统计
#对数据进行探索：品牌投诉总数，车型投诉总数
#哪个品牌的平均车型投诉最多
#清洗
def f(x):
    x=x.replace('一汽大众','一汽-大众')
    return x
df['brand']=df['brand'].apply(f)
result=df.groupby(['brand'])['id'].agg(['count'])
result

tags = df.columns[7:]
tags
result2=df.groupby(['brand'])[tags].agg(['sum'])
result2
result2=result.merge(result2,left_index=True,right_index=True,how='left')
result2
#序号搞回来
result2.reset_index(inplace=True)
result2
result2.to_csv('./result2.csv')

#排序，按照count，大到小
result2=result2.sort_values('count',ascending=False)
result2

query=('O348','sum')
result2.sort_values(query,ascending=False)