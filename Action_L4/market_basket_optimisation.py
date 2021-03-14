import pandas as pd
#from mlxtend.frequent_patterns import apriori
#from mlxtend.frequent_patterns import association_rules
#import sys
#import io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
# 数据加载
pd.set_option('max_columns',None)
dataset = pd.read_csv('./Market_Basket_Optimisation.csv',encoding='gb18030',header=None)
print(dataset)
print(dataset.shape)

transactions=[]
#按照行进行遍历
for i in range(0,dataset.shape[0]):
	#记录一行transaction
	temp=[]
	#按照列进行遍历
	for j in range(0,dataset.shape[1]):
		if str(dataset.values[i,j])!='nan':
			temp.append(dataset.values[i,j])
	#print(temp)
	transactions.append(temp)
print(transactions)

from efficient_apriori import apriori
itemsets, rules = apriori(transactions, min_support=0.02,  min_confidence=0.2)
print('频繁项集：', itemsets)
print('关联规则：', rules)
