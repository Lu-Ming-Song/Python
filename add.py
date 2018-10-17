import os
import pandas as pd
import numpy as np
df = pd.DataFrame(columns=['流水号','事件名称','本方户名','对方户名','流水时间','操作员','交易额','流水标志','扇区号'])
l, num, money = [], [], []
def search(path):
    parents = os.listdir(path)
    sum = 0
    for parent in parents:                              # 返回指定路径下所有文件和文件夹的名字，并存放于一个列表中
        child = os.path.join(path,parent)
        if os.path.isdir(child):                       # 将多个路径组合后返回
            search(child)
        elif os.path.isfile(child):                    # 如果是目录，则继续遍历子目录的文件
            if os.path.splitext(child)[1] == '.xls':   # 分割文件名和文件扩展名，并且扩展名为'xls'
                d = pd.read_excel(child)
                for i in range(len(d)):
                    num.append(os.path.split(child)[1][0:9])
                l.append(d)
                k = d[d['对方户名'].notnull()]  # 排除NAN
                k = k.loc[k['对方户名'].str.contains('网络缴费')]  # 筛选出一列中特殊的数据
                money.append(k['交易额'].sum()) # 求筛选出的数据之和       
search(r'C:\Users\aming\Desktop\大学生行为分析\学生数据_YJ_LHJ\1150712')
df = pd.concat(l)
#da = pd.Series(num)
#df['学号'] = da
#df['网络缴费'] = pd.Series(money)

#df = df[df['对方户名'].notnull()]  # 排除NAN
#df = df.loc[df['对方户名'].str.contains('网络缴费')]  # 筛选出一列中特殊的数据
df = df.drop(columns=['对方户名','流水号','交易额','事件名称','流水时间','流水标志','操作员','扇区号'],axis=1) #删除整列全为NAN的列
df = df.drop_duplicates(subset=['本方户名'],keep='last')
df['学号'] = np.unique(num)
df['网络缴费'] = money
df.to_csv('1.csv',index=False) # 保存为result文件
