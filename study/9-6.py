#csq 2021 4 26
#9-6
class Restaurant():
	'''fandianxiaochangshi'''
	def __init__(self,restaurant_name,cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type
		self.number_served = 1
		
	def describe_restaurant(self):
		print(self.name + ' is ' + self.type)
	
	def open_restaurant(self):
		print('yingyezhong')
	
	def set_number_served(self,value):
		if value >= self.number_served:
			self.number_served = value
		else :
			print('NO')
		
	def increment_number(self,value):
		if value >=0:
			self.number_served += value
		else :
			pirnt('no')
			
class IceCreamStand(Restaurant):
	
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = ['ta','ba','sdfa','aadsf']
		
	def appear_flavors(self):
		print(self.flavors)

a = IceCreamStand('44a','bbs')
a.appear_flavors()

#9-7
class User():
	'''YONGHU'''
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0
	def describe_user(self):
		print('sd' + self.first_name + self.last_name)
		
	def greet_user(self):
		print('nihao' + self.first_name + self.last_name)
	
	def increment_login_attempts(self):
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		self.login_attempts = 0

class Admin(User):
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privileges = Privileges(['aa','aad','adasf'])
		
	def show_privileges(self):
		print(self.privileges)


		
class Privileges():
	def __init__(self,privileges):
		self.privileges = privileges
		
	def show_privileges(self):
		print(self.privileges)
		
user1 = Admin('safa','adsfads')
user1.privileges.show_privileges()
