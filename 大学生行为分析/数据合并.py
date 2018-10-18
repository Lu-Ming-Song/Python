import os
import pandas as pd
df = pd.DataFrame(columns=['流水号','事件名称','本方户名','对方户名','流水时间','操作员','交易额','流水标志','扇区号'])
l = []
num = []
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
#search(r'C:\\Users\aming\\Desktop\\大学生行为分析\\后勤数据\\学生数据_YJ_LHJ')
search(r'C:\Users\aming\Desktop\大学生行为分析\1250111')
#search(r'C:\\Users\aming\\Desktop\\大学生行为分析\\后勤数据\\学生数据_LHJ_YJ\1250111\2012-8-1_2014-7-15')

df = pd.concat(l)
da = pd.Series(num)
df['学号'] = da
df = df.drop(columns=['流水号','扇区号','流水号','操作员','流水标志'],axis=1) #删除整列全为NAN的列
df.to_csv('学生考试.csv',index=False) # 保存为result文件
