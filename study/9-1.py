# csqcsq 2021 4 26
class Restaurant():
	'''fandianxiaochangshi'''
	def __init__(self,restaurant_name,cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type
		
	def describe_restaurant(self):
		print(self.name + 'is' + self.type)
	
	
	def open_restaurant(self):
		print('yingyezhong')
	
restaurant1 = Restaurant('a','b')
print(restaurant1.name + restaurant1.type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
#9 - 2 
restaurant2 = Restaurant('c','d')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('e','f')
restaurant3.describe_restaurant()
# 9 -3
class User():
	'''YONGHU'''
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
	
	def describe_user(self):
		print('sd' + self.first_name + self.last_name)
		
	def greet_user(self):
		print('nihao' + self.first_name + self.last_name)

user1 = User('45','45')
user2 = User('23','232')
user3 = User('456','45456')
user1.greet_user()
user1.describe_user()
