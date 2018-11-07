# 魔法方法实例

# __del__()析构方法

'''class File:
	def __init__(self,name):
		self.name = name
		print("open file",self.name)

		# read
		#
		# write

	def __del__():
		print("close file",self.name)


f1 = File("a.txt")

f2 = File("b.txt")

f3 = File("c.txt")
del f3

print("read...write...")'''

'''
# __str__()使用	
class Stu:
	name = "张三"
	age = 20

	def __str__(self):
		return "name：%s;age:%d"%(self.name,self.age)
s = Stu()

print(s)'''

#__add__()
#
class Demo():
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __str__(self):
		return "Demo(%d,%d)"%(self.x,self.y)

	def __add__(self,other):
		return Demo(self.x+other.x,self.y+other.y)

d1 = Demo(5,8)
d2 = Demo(9,-4)

print(d1+d2)