def NOD(a,b):
	r = a % b
	while r != 0:
		a = b
		b = r
		r = a % b
	return b
	
def power(a,n):
	m = []
	while n > 0:
		m.append(n%2)
		n = n // 2
	s = 1
	q = len(m)
	for i in range(q):
		if m[q - i - 1] == 0:
			s = s*s
		else:
			s=s*s*a
	return s
	
class frac:
	def __init__(self,up,down=1):
		if down == 0:
			print('blue screen of  death(we can\'t div 0)')
			return None
		c = NOD(int(up),int(down))
		self.up = up // c
		self.down = down // c
		print('drob\' is created')
		
		
	def __str__(self):
		if self.down == 1:
			return '{}'.format(self.up)
		else:
			return ('{}/{}'.format(self.up,self.down))
			
			
	def __add__(self,other):
		if type(other) == frac:
			return frac(self.up*other.down+self.down*other.up,self.down*other.down)
		elif type(other) == int:
			return frac(self.up+other*self.down,self.down)
		else:
			print('oops')
			
	def __radd__(self,other):
		if type(other) == int:
			return self + other
		else:
			print('oops')
			
	
	def __sub__(self,other):
		if type(other) == frac:
			return self + frac(-1*other.up,other.down)
		elif type(other) == int:
			return self + (-1*other)
		else:
			print('oops')
			
	def __rsub__(self,other):
		if type(other) == int:
			return -self + other		
			
			
	def __mul__(self,other):
		if type(other) == frac:
			return frac(self.up*other.up,self.down*other.down)
		elif type(other) == int:
			return frac(self.up*other,self.down)
		else:
			print('oops')
			
	def __rmul__(self,other):
		return self * other
		
			
	def __neg__(self):
		return frac(-self.up,self.down)
		
		
	def __div__(self,other):  #should answer after '/', but print error
		if type(other) == frac:
			return frac(self.up*other.down,self.down*other.up)
		elif type(other) == int:
			return frac(self.up,self.down*other)
		else:
			print('oops')
			
	def __rdiv__(self,other):
		if type(other) == int:
			return frac(other*self.down,self.up)
		else:
			print('oops')
			
			
	def __pow__(self,p):
		return frac(power(self.up,p),power(self.down,p))
	
	
	def __eq__(self,other):
		if type(other) == frac:
			if self.up == other.up and self.down == other.down:
				return True
			else:
				return False
		elif type(other) == int:
			return self == frac(other)
		else:
			print('oops')
	
	def __ne__(self,other):
		return not(self == other)
	
	def __lt__(self,other):
		if type(other) == frac:
			if (self - other).up < 0:
				return True
			else:
				return False
		elif type(other) == int:
			return self<frac(other)
		else:
			print('oops')
	
	def __gt__(self,other):
		if type(other) == frac:
			if (self - other).up > 0:
				return True
			else:
				return False
		elif type(other) == int:
			return self>frac(other)
		else:
			print('oops')
	
	def __le__(self,other):
		if type(other) == frac:
			if (self - other).up <= 0:
				return True
			else:
				return False
		elif type(other) == int:
			return self<=frac(other)
		else:
			print('oops')
			
	def __ge__(self,other):
		if type(other) == frac:
			if (self - other).up >= 0:
				return True
			else:
				return False
		elif type(other) == int:
			return self>=frac(other)
		else:
			print('oops')
			
		
	def __float__(self):
		return self.up/self.down

		

a=frac(4,1)
print(a)			
b=frac(2,3)
print(b)
print(dir(int))

