#2021 0430 csq 四月最后一天，基础完事
import unittest

class Employee():
	
	def __init__(self,first_name,last_name,salary):
		self.first_name = first_name
		self.last_name = last_name
		self.salary = salary
		
	def give_raise(self,incsalary=5000):
		self.salary += incsalary
		return self.salary
	
class Testemployee(unittest.TestCase):
	
	def setUp(self):
		self.Employee = Employee('li','wang',2000)
	
	def test_give_default_raise(self):
		a = self.Employee.give_raise()
		self.assertEqual(a,7000)
		
	def test_give_custom_raise(self):
		b = self.Employee.give_raise(1000)
		self.assertEqual(b,3000)
unittest.main()
