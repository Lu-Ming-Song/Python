#构造函数：__init__()

'''class A:
	def __init__(self):
		print("AAAA")
	def fun(self):
		print("class A...")

a = A()'''
class Person:
	name = ""
	age = 0
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def getlnfo(self):
		print(self.name,":",self.age)
#构造方法可以实现，实例化对象的使用就可以初始化属性
p = Person("lisi",20)

p.getlnfo()