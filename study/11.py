#2021.04.12 csq
member=['wang','guoqi','zhanga','wangli']
for i in range(4):
	print(member[i].title()+'，你好小常请您吃饭。')
member[1] = 'xiaoli'
for i in range(4):
	print(member[i].title()+'，你好小常请您吃饭。')
print('我找到了更大的餐主桌')
member.insert(0,'zhangyiyin')
member.insert(2,'zhangyi')
member.append('zjamng')
for i in range(7):
	print(member[i].title()+'，你好小常请您吃饭。')
for i in range(5):
	j=member.pop()
	print('im sorry,'+j)
for i in range(2):
	print(member[i].title()+'，你好小常请您吃饭。')
del member[0]
del member[0]
print(member)
	
