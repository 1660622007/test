#csq 2021 04 26 
class Restaurant():
	'''fandianxiaochangshi'''
	def __init__(self,restaurant_name,cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type
		self.number_served = 0
		
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
			self.number_ served += value
		else :
			pirnt('no')
		
restaurant1 = Restaurant('a','b')
print(restaurant1.name + str(restaurant1.number_served))
restaurant1.numer_served = 3
print(str(restaurant1.number_served))
restaurant1.describe_restaurant()
restaurant1.set_number_served(55)
print(str(restaurant1.number_served))
restaurant1.increment_number(2)
print(str(restaurant1.number_served))

#9-5
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
		self.login_attempts =0
		
user1 = User('adfads','adfas')
user1.describe_user
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

