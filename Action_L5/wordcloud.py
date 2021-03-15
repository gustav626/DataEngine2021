'''
from nltk.book import *
'''
import pandas as pd
from nltk.tokenize import word_tokenize

# 数据加载
data = pd.read_csv('./Market_Basket_Optimisation.csv',encoding='gb18030',header=None)
print(data)
print(data.shape)
#store data into transactions
transactions=[]
#dict d[‘key’] = ‘value’
item_count={}
for i in range(data.shape[0]):
	temp=[]
	for j in range(data.shape[1]):
		item=str(data.values[i,j])
		if item != 'nan':
			temp.append(item)
			if item not in item_count:
				item_count[item]=1
			else:
				item_count[item]+=1
	transactions.append(temp)
#print(transactions)
#print(item_count)

from wordcloud import WordCloud
#'hello'，'have'，'can'，'might'
def remove_stop_words(f):
	stop_words=['tasty','special']
	for stop_word in stop_words:
		f=f.replace(stop_word,'')
	return f

def create_word_cloud(f):
	f = remove_stop_words(f)
	cut_text = word_tokenize(f)
	cut_text = " ".join(cut_text)
	wc = WordCloud(
		max_words=100,
		width=1280,
		height=1080,
    )
	wordcloud = wc.generate(cut_text)
	wordcloud.to_file("wordcloud.jpg")

#generate word cloud
all_word=''.join('%s' %item for item in transactions)
#print(all_word)
create_word_cloud(all_word)

#show Top10 goods
print(sorted(item_count.items(),key=lambda x:x[1], reverse=True)[:10])