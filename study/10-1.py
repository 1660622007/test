#csq 2021 0427
with open('learning_python.txt','w') as file_object:
	file_object.write('IN python you can learn \n')
	file_object.write('IN python you can learn ')
	file_object.write('IN python you can learn ')
	

with open('learning_python.txt') as file_object:
	messages = file_object.read()

	a = messages.replace('python','23')
	print(a)
	
	
