#2021 0428 csq 
import json

'''num= input('nums:')
with open('nums.json','w') as file1:
	json.dump(num,file1)

with open('nums.json') as file1:
	num = json.load(file1)
	print('i know your,its:'+ num)

def get_user():
	file_name = 'username.json'
	try :
		with open(file_name) as file1:
			username = json.load(file1)
	except FileNotFoundError:
		return None
	else :
		return username

def greet_user():
	username = get_user()
	if username :
		print(username + 'nihao,nizuixihuandeshuzishi:' + num)
	else :
		username = input('qingshuru nide mingzi:')
		num = input('qingshurunizuixihuandeshuzi:')
		filename = usename + '.json'
		with open(filename,'w') as file2:
			json.dump(num,filename)

greet_user()
'''
a = {'asadf':'sf','asdfs':'sfasdf'}
b = input('sdf')
c = b + 'sdaf.json'
with open(c,'w') as file1:
	json.dump(a,file1)
with open(c) as file1:	
	print(json.load(file1)['asdfs'])
