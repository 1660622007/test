#csq 2021 04 23
magicians = ['aaa','aa','aaa','aadasfasd']
b = []
c = magicians[:]
def show_magicians(a):
	for  i in a:
		print(i)
def make_greats(a,b):
	
	while c:
		bs = c.pop()
		bs = 'the Great ' + bs
		b.append(bs)
make_greats(magicians,b)
show_magicians(magicians)
show_magicians(b)
