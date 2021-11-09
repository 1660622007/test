#csq 2021 0428 有问题
import json

def check_username():
	'''检验用户'''
	
	try:
		file_name = 'usernames.json'
		with open(file_name) as file_obj:
			usernames1 = json.load(file_obj)
	except FileNotFoundError:
		create_user()
	else:
		if username in usernames1:
			print('欢迎归来！' + username)
			try:
				num1 = get_num()
			except FileNotFoundError:
				num = input('请输入你喜欢的数字：')
				create_usernum()
			else:
				print('你喜欢的数字是：' + num1)
		else :
			create_user()
			num = input('请输入你喜欢的数字：')
			create_usernum()
def create_user():
	'''在usernames中加入新用户'''
	file_name = 'usernames.json'
	with open(file_name,'w') as file_obj1:
		json.dump(username,file_obj1)
		print('下次来时我会欢迎你' + username)
		
def create_usernum():
	'''创建新用户的数字文件'''
	numfile_name = username + 'num.json'
	with open(numfile_name,'w') as file_num1:
		json.dump(num,file_num1)

def get_num():
	'''读取用户喜爱的数字'''
	numfile_name = username + 'num.json'
	with open(numfile_name) as file_num:
		num = json.load(file_num)
	return num	
def greet_users():
	'''与用户交互'''
	username = input('请输入用户昵称:')
	
username = input('请输入用户昵称:')	
check_username()
