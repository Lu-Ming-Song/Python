#类中的属性和方法
class Person:
	name = ""
	__age = 0 #私有属性
	def __init__(self,name,age):
		self.name = name
		self.__age = age
	def getlnfo(self):
		print(self.name,":",self.__age)
		self.__demo()
	def __demo(self):
		print("peivate method()")
#构造方法可以实现，实例化对象的使用就可以初始化属性
p = Person("lisi",30)
#print(p.__age) #不可访问对象中私有属性
p.getlnfo()
#p.__domo()