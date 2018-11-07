import pandas as pd
import numpy as np
from sklearn import preprocessing
from pandas.core.frame import DataFrame
from sklearn import neighbors
total, M, B, change = [], [], [], []
wbcd = pd.read_csv(r"C:\Users\aming\Desktop\KNN\wisconsin.csv")
#去除‘id’列
wbcd = wbcd.drop('id',axis=1)
#计算'M','B'的总值
total.append(len( wbcd[wbcd['diagnosis'] == 'M']))
total.append(len( wbcd[wbcd['diagnosis'] == 'B']))
#将列表转化为数据框
c = {"M":total[0],"B":total[1]}
#改变特定行的特定值
for i in wbcd['diagnosis']:
	if i == 'M':
		M.append('Malignant')
		change.append('Malignant')
	else:
		B.append('Benign')
		change.append('Benign')
wbcd['diagnosis'] = pd.Series(change)
#'M','B'所占比例
M_scale = len(M) / len(change) * 100
B_scale = len(B) / len(change) * 100
#转换—min-max标准化数值数据
X_train = wbcd.ix[:,1:31]
#min-max标准化
min_max_sacler = preprocessing.MinMaxScaler()
wbcd_MinMax = min_max_sacler.fit_transform(X_train)
#print(min_max_sacler.transform(X_train))

'''#使用z-score标准化
X_scaled = preprocessing.scale(X_train)'''

#将列表转化为数据框
wbcd_n = pd.DataFrame(wbcd_MinMax)

#汇总检测
#summary = min_max_sacler.transform(X_train).sum(axis=1)

#对数据集进行分类
wbcd_train = wbcd_n.ix[0:468]
wbcd_test = wbcd_n.ix[468:568]

#创建数据标签
wbcd_train_lables = wbcd.ix[0:468,0:1]
wbcd_test_lables = wbcd.ix[468:568,0:1]

#对类进行初始化

knn = neighbors.KNeighborsClassifier(n_neighbors = 5, algorithm = 'kd_tree',
	weights = 'uniform')

#对数据进行训练
knn.fit(wbcd_train,wbcd_train_lables)

#预测数据的diagnosis类型
predict_result = knn.predict(wbcd_test)
predict_result = pd.DataFrame(predict_result)
#print(predict_result)

#观察预测结果
predict_result[0].value_counts()

# 实际测试集中数据结果
wbcd_test_lables['diagnosis'].value_counts()

# 输出预测的正确率
print(knn.score(wbcd_test, wbcd_test_lables))