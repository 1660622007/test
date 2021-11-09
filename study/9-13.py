#csq 2021 0426
from random import randint

class Die():
	def __init__(self,sides=6):
		self.sides = sides
		
	def roll_die(self):
		x = randint(1,self.sides)
		print(x)

die1 = Die(8)
die1.roll_die()
