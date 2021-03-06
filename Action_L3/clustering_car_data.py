from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt

#从csv读取数据
data = pd.read_csv(r"car_data.csv", encoding="GBK")
tran_x = data[["人均GDP","城镇人口比重","交通工具消费价格指数","百户拥有汽车量"]]
#print(tran_x)
#格式化地区数据
#le = LabelEncoder()
#tran_x["地区"] = le.fit_transform(tran_x["地区"])
#print(tran_x)
#格式化整体数据【0-1】
min_max_scaler = preprocessing.MinMaxScaler()
tran_x = min_max_scaler.fit_transform(tran_x)
# print(tran_x)
#pd.DataFrame(tran_x).to_csv("temp", encoding="GBK")
#手肘法
sse = []
for k in range(2,10):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(tran_x)
    sse.append(kmeans.inertia_)
x = range(2,10)
plt.xlabel('k')
plt.ylabel('SSE')
plt.plot(x,sse,'o-')
plt.show()
#轮廓系数
sc_scores = []
for k in range(2,10):
    kmeans = KMeans(n_clusters=k)
    kmeans_model = kmeans.fit(tran_x)
    sc_score = silhouette_score(tran_x,kmeans_model.labels_,metric='euclidean')
    sc_scores.append(sc_score)
k=[2,3,4,5,6,7,8,9]
plt.xlabel('k')
plt.ylabel('SCS')
plt.plot(k,sc_scores,'*-')
plt.show()
#通过手肘和轮廓系数确定K为3
kmeans = KMeans(n_clusters=4)
kmeans.fit(tran_x)
preidct_y = kmeans.predict(tran_x)
'''
print(preidct_y)
print(tran_x)
pca = PCA(n_components=2)
tran_x_deco = pca.fit_transform(tran_x)
print(tran_x_deco)
print(tran_x_deco[:,0])
print(tran_x_deco[:,1])
plt.xlabel('tran_x_deco[,0]')
plt.ylabel('tran_x_deco[,1]')
plt.show()
'''
#合并数据
data["聚合"] = preidct_y
data = data.sort_values("聚合", ascending=False)
data.to_csv("result.csv", encoding="GBK")
