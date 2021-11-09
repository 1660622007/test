#csq 2021.4.23
def make_car(model,manufacturer,**user_info):
	'''打印汽车信息，输出字典'''
	dic = {}
	dic['model'] = model
	dic['manufacturer'] = manufacturer
	for i,j in user_info.items():
		dic[i] = j
	print(dic)
car = make_car('subra','outback',color='blue',tow_package=True)


 
