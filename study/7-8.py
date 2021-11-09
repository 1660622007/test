#2021.04.22 csq
sandwich_orders = ['a','pastrami','c','d','pastrami','pastrami']
finish_sandwichs = []
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
while sandwich_orders:
	
	finish_sandwich = sandwich_orders.pop()
	finish_sandwichs.append(finish_sandwich)
	print('id like '+finish_sandwich)
print(finish_sandwichs)
response = {}
active= True
while active:
	name = input('qingshuru nide name:')
	if name == 'no' :
		break
	
	else :
		place = input('qingshuru ni xiangquna :')
		if place == 'no':
			break
		else:
			response[name] = place
	print('shuru no jiehsu')
print(response)

