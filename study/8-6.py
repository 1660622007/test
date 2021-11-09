#csq 2021 04 23
def city_country(name,country):
	a = '\"' + name +', ' + country + '\"'
	return a
dic = {'dalian':'china','newyork':'america'}
for i,j in dic.items():	
	print(city_country(i,j))
def make_album(name,album,nums=''):
	dic = {}
	dic['name'] = name
	dic['album'] = album
	if nums:
		dic['nums'] = nums
	return dic
print(make_album('wio','sdfa',6))
active = True
while active:
	print('rushuru jieshu qing shuru quit!')
	name = input('qingshuru singer:')
	if name=='quit':
		break
	album = input('qingshuru zhuanjiming:')
	if album=='quit':
		break
	nums = input('qingshuru gequshuliang: ')
	if nums=='quit':
		break
	print(make_album(name,album,nums))
