#csq 2021 0429
#写一个用户登录及获取信息的程序
import json

def check_username(username):
	file_usernames = 'usernames.txt'
	try:
		with open(file_usernames) as file_nameobj:
			usernames = file_nameobj.read()
	except FileNotFoundError:
		with open(file_usernames,'w') as file_nameob:
			pass
		
	else:
		if username in usernames :
			print('欢迎归来，' + username + '!')
			check_number(username)
		else :
			with open(file_usernames,'a') as file_nameo:
				file_nameo.write(username)
			print(username + ',你下次来时，我会欢迎你的。')
def check_number(username):
	file_numname = username + 'num.txt' 
	try:
		with open(file_numname) as file_numobj:
			num = file_numobj.read()
	except FileNotFoundError:
		num = input('请输入你最喜欢的数字：')
		with open(file_numname,'w') as file_numob:
			file_numob.write(num)
		print(username + ',你下次来时，我会欢迎你并告诉你你最喜欢的数字。')
	else:
		print('你最喜欢的数字是：' + num)	 	

def greet_user():
	username = input('请输入你的昵称：')
	b = check_username(username)
	
greet_user()
