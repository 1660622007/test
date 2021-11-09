#csq 2021 04 23
def sandwich(food):
	'''收集用户的配料'''
	print('\nshuru  q quit')
	while True:
		foods = input('input foods:')
		if foods == 'q':
			break
		else:
			x.append(foods)
	return x
def sandwich_print(food):
	'''打印配料表'''
	print(*food)
x = []

sandwich_print(sandwich(x))
		
		
