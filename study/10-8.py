#csq 2021 0428

'''with open('cats.txt','w') as file1:
	file1.write('cat1')
	file1.write('cat2')
	file1.write('cat3')
	file1.write('cat4')'''
with open('dogs.txt','w') as file2:
	file2.write('dog1\n ')
	file2.write('dog3')
	file2.write('dog3')
	file2.write('dog3')

try:
	with open('cats.txt','r') as file1:
		print(file1.read())
	
	with open('dogs.txt','r') as file2:
		a = file2.read()
		
		print(a.count('dog3'))
except FileNotFoundError :
	pass

