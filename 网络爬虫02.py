import json
import requests
from requests.exceptions import RequestException
import re
import time
global x 
x=1

#定义一个读取一个url并返回相应信息的函数
def get_one_page(url):
    try:
    	#伪装浏览器
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        #读取网页
        response = requests.get(url, headers=headers)
        #判断是否成功
        if response.status_code == 200:
			#返回读取的内容（html代码）           
            return response.text
        return None
    except RequestException:
        return None
 
#定义一个解析html代码的函数
def parse_one_page(html):
	#编译成一个正则表达式对象
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    #开始查找
    items = re.findall(pattern, html)
    #遍历查找到的内容
    for item in items:
		 #使用关键字yield 类似于return 返回的是一个生成器对象
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }
 
#将结果写到一个txt文档中 
def write_to_file(content):
    global x 
    #下载图片并且以排名命名 
    urllib.request.urlretrieve(content['image'], r'C:\Users\Lenovo\Desktop\Img\%s.jpg' % x)
    x += 1
    with open('resul.txt', 'a', encoding='utf-8') as f:
         f.write(json.dumps(content['title'], ensure_ascii=False) )
         f.write(json.dumps(content['time'], ensure_ascii=False)
         f.write(json.dumps(content['score'], ensure_ascii=False))
         f.write("\n")

#打开需要爬取得所有网页，并进行爬取
def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    #请求网页，获取html
    html = get_one_page(url)
    #遍历处理后的html结果
    for item in parse_one_page(html):
    	#下载图片
        pic_download(item['image'],item['title'])
        #将所有信息写入文件
        write_to_file(item)
  
 
 
if __name__ == '__main__':
    for i in range(10):
        main(i*10)
        #延迟1秒，避免反爬机制
        time.sleep(1)
