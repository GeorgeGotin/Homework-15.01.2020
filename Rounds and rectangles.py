import math

class round:
	def __init__(self,x=0,y=0,r=1):
		self.x = x
		self.y = y
		self.r = abs(r)
	def translate(self,delta_x=0,delta_y=0):
		self.x+=delta_x
		self.y+=+delta_y
		print('New coordinates = ({};{})'.format(self.x,self.y))
	def scale(self,k=1):
		self.r*=abs(k)
		print('New radius = ',self.r)
	def check(self,p_x=0,p_y=0):
		if (p_x-self.x)**2+(p_y-self.y)**2 <= self.r**2:
			return True
		else:
			return False
	def __str__(self):
		return '({};{}),r={}'.format(self.x,self.y,self.r)
	def per(self):
		return 2*math.pi*self.r
	def area(self):
		return math.pi*self.r*self.r
		
class rectangle:
	def __init__(self,x=0,y=0,a=1,b=1):
		self.x = x
		self.y = y
		self.a = abs(a)
		self.b = abs(b)
	def translate(self,delta_x=0,delta_y=0):
		self.x+=delta_x
		self.y+=+delta_y
		print('New coordinates = ({};{})'.format(self.x,self.y))
	def scale(self,k=1):
		self.a*=abs(k)
		self.b*=abs(k)
		print('New sides: a={}, b={}'.format(self.a,self.b))
	def check(self,p_x=0,p_y=0):
		if (p_x <= self.x+0.5*self.a) and (p_x >= self.x-0.5*self.a) and (p_y <= self.y+0.5*self.b) and (p_y >= self.y-0.5*self.b):
			return True
		else:
			return False
	def __str__(self):
		return '({};{}),a={},b={}'.format(self.x,self.y,self.a,self.b)
	def per(self):
		return 2*(self.a+self.b)
	def area(self):
		return self.a*self.b
		
a = rectangle()
print(a)
a.translate(1,1)
a.scale(2)
print(a)
print(a.check())
print(a.per(),a.area())
		
