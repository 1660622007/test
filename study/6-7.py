#csq 2021 4 21
friend1 = {'first_name':'chang','last_name':'shengqing','age':24,'city':'hefei'}
friend2 = {'first_name':'chang','last_name':'qing','age':25,'city':'hf'}
friend3 = {'first_name':'chang','last_name':'sheng','age':23,'city':'he'}
people = [friend1,friend2,friend3]
for i in people:
	print(i)
people_list = {'zml':friend1,'lhz':friend2,'sss':friend3}
for i,j  in people_list.items():
	print(i+":")
	print(j)
cities={
	'hefei':{
		'country':'china',
		'population':'12346789',
		'fact':'nothing'
		},
	'gans':{
		'country':'china',
		'population':'126456',
		'fact':'wi'
		}
	}
for i,j in cities.items():
	print(i)
	print(j)
