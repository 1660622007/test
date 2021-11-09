#csq 2021 4 27
while True:
	num1 = input('qingshuru zhenghsu:')
	num2 = input('qingshuru zhenghsu:')
	try:
		num1 = int(num1)
		num2 = int(num2)
	except ValueError:
		print('qingshuru shuzhixingshuju ')
	else :
		a = num1 + num2
		print(a)
	
