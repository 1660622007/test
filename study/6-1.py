#csq 2021 4 21
friend1 = {'first_name':'chang','last_name':'shengqing','age':24,'city':'hefei'}
print(friend1['first_name']+friend1['last_name']+'jinnian'+str(friend1['age'])+' live in '+friend1['city'])
a = {'zyy':'1','wjt':'2','zml':'3'}
for i,j in a.items():
	print(i+':'+j)
b = {'changjiang':'china','huanghe':'zhongguo','yamaxun':'buzhidao'}
for i,j in b.items():
	print(i.title()+' runs through '+j.title())
for  i in b.keys():
	print(i)
for i in b.values():
	print(i)
list1 = {'jen':'python','sarah':'c','edward':'c==','phil':'pyhton',}
d = ["jen",'sarah','edward','phil','sar','adas','afaf','afdasfa']
for i in d:
	if i in list1.keys():
		print('thanks')
	else:
		print('yaoqingni '+i+',canjia ')


