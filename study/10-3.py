#csq 2021 0427


input1 = input('请输入名字：')
with open('guest.txt','a') as file_object:
	file_object.write(input1+'\n')

while True:
	name = input('请输入名字：')
	if name == 'q':
		break
	else:
		print('nihao' + name)
		print('shuru q likai')
		with open('guest_book.txt','a') as file_bool:
			file_bool.write(name + 'fangwen\n')
