
import urllib.request
import time
import re

global x # 使用前初次声明
x=1
#获取网页的html，与requests包一样的功能
def getHtml(url):
    #打开网页
    page = urllib.request.urlopen(url)

    htmlcode = page.read() 
    return htmlcode


#获取图片对应的src属性代码


def getImg(html):
    global x  # 再次声明，表示在这里使用的是全局而非局部
    html=html.decode('utf-8')
        
    #通过re-compile-findall二连函数操作来获取图片src属性对应的代码
     
    src = r'https://[^\s]*?\.jpg'  
    imgre = re.compile(src)     #re.compile()，可以把正则表达式编译成一个正则表达式对象
    imglist = re.findall(imgre, html) 
    #re.findall()，读取html中包含imgre（正则表达式）的数据,imglist是包含了所有src元素的数组
        
    #用urlretrieve下载图片。图片命名为0/1/2...之类的名字
       
    
    for imgurl in imglist:
        name = time.strftime("%Y_%m_%d",time.localtime()) + '_' + str(x)
            
         #注意，这里的文件路径，每段路径的首字母一定要大写！！小写会识别出错
        urllib.request.urlretrieve(imgurl, r'C:\Users\aming\Desktop\K\%s.jpg' % name)
        x += 1
        
        
      
    
for i in range(2,4):
        
        html = getHtml("https://tieba.baidu.com/p/2460150866?pn=" + str(i))
        getImg(html)
       