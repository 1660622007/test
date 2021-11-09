#csq 2021 04 22
a = 1
b = 1
while a != 'quit':
	a = input('qingshuru:')
	if a !='quit':
		print('jia'+a)	
	else : 
		print('welcome ')
while b!= 'quit':
	b = input('shuru nianling ')
	if b == 'quit':
		print('huanyingxiaci')
	else:
		b=int(b)
		if b < 3:
			print('piaojiawei free')
		elif b > 12:
			print('piaojiawei 15')
		else :
			print('piaojiawei 10')
	
		
