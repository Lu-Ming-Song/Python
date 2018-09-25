import os
import pandas as pd
df = pd.DataFrame(columns=['流水号','事件名称','本方户名','对方户名','流水时间','操作员','交易额','流水标志','扇区号'])
l = []
def search(path):
    parents = os.listdir(path)  # 返回指定路径下所有文件和文件夹的名字，并存放于一个列表中
    sum = 0
    for parent in parents:
        child = os.path.join(path,parent) # 将多个路径组合后返回
        if os.path.isdir(child):
            search(child)         # 遍历文件名
        elif os.path.isfile(child):
            if os.path.splitext(child)[1] == '.xls':
                d = pd.read_excel(child)
                l.append(d)
search(r'C:\Users\aming\Desktop\大学生行为分析\后勤数据')
df = pd.concat(l)
df.to_excel('result.xls',index=False) # 保存到result文件里