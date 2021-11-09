#2021 4 19 csq
a = [1,2,3,4,5,6,7]
print("The first three items in the list are:")
print(a[:3])
print("The items from the middle of the list are:")
print(a[len(a)//2-1:len(a)//2+2])
print("The last three items in the list are:")
print(a[-3:])
b = a[:]
a.insert(1,8)
b.insert(1,9)
print(a)
print(b)
for i in a:
	print(i)
hotel_1 = ("p",'e','a','c','h')
hotel_2 = []
for i in hotel_1:
	print(i)
	hotel_2.append(i)
hotel_1 = hotel_2
hotel_1[1]="a"
print(hotel_1)
