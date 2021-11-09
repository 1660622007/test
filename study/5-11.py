#csq 2021 0421
current_users = ['csq','lzy','zyy','wza','sss']
new_users = ['Zyy','lzy','wza','fas','aaa']
c = []
for i in current_users:
	c.append(i.lower())
for i in new_users:
	if i.lower() in c:
		print(i+' yibeishiyong,qingchongxinshuru')
	else:
		print(i+' weibeishiyong')
nums = [2,1,3,4,9,8,7,6,5]
c = 0
for i in nums:
	c+=1
	if i == nums[0]:
		print(str(i)+"\n1st")		
	elif i == nums[1]:
		print(str(i)+"\n2ed")
	elif i == nums[2]:
		print(str(i)+'\n3rd')
	else:
		print(str(i)+'\n'+str(c)+'th' )
