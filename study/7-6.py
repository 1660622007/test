#csq 2021 4 22
active = True
a = 'qingshurushiwumingcheng\n'
a += 'shuruquitlikai'
while active:
	message = input(a)
	if message == 'quit':
		active= False
		break
	else:
		print(message)


