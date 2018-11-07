'''
# property()
class Rectangle:
	def __init__(self):
		self.width = 0
		self.height = 0

	def setSize(self,size):
		self.width,self.height = size

	def getSize(self):
		return self.width,self.height


	size = property(getSize,setSize)
r = Rectangle()
#r.width = 100
#r.height = 50
r.setSize((200,100))
print(r.getSize())

r.size = 1000,500

print(r.size)'''
'''
#静态方法和类成员方法

class A:
	def fun():
		print("aaaa")
	fun = staticmethod(fun)   #静态方法定义


	def demo(self):
		print("bb")
	demo = classmethod(demo)  #类成员方法定义
#a = A()
A.fun()
A.demo()'''


'''
#试用装饰器定义静态和类成员方法
class A:

	@staticmethod  #静态方法定义
	def fun():
		print("aaaa")
	

	@classmethod       #类成员方法定义
	def demo(self):
		print("bb")
	
#a = A()
A.fun()
A.demo()'''



class B:
	name = "zhangsan"
	__age = 20

	def fun1(self):
		print("aa")

	def __dd(self):
		print("cc")

b = B()
print(hasattr(b,"name"))
print(hasattr(b,"__age"))
print(hasattr(b,"fun1"))
print(hasattr(b,"__dd"))