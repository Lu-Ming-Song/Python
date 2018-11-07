#类的继承和方法重写

#定义父类（基类）
class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		
	def getlnfo(self):
		print("我的名字：%s: 年龄：%d岁"%(self.name,self.age))

#定义子类（派生类）
class Stu(Person):
	def __init__(self,name,age,school):
		Person.__init__(self,name,age)#去构造父类
		self.school = school
	#方法重写（升级，优化）
	def getlnfo(self):
		print("我的名字：%s: 年龄：%d岁.学校：%s"%(self.name,self.age,self.school))
	#子类定义父类没有的方法，叫扩展
	def fun(self):
		print("Hello World!")
#测试
s = Stu("张三",20,"北京大学")
s.getlnfo()


#多继承

print("="*50)
class A:
	def fun(self):
		print("class A......")

class B:
	def fun(self):
		print("class B......")

#C类继承了A和B
class C(A,B):
	pass

c = C()
c.fun()

