n=int(input("Enter A Number:"))
print(f"Enter {n} elements:")
li=[]

for i in range(0,n):
	num=int(input(f"Enter {i+1} Element:"))
	li.append(num)

print("List:",li)
large=li[0]
small=li[0]
large2=li[0]
small2=li[0]

for i in li:
	if i>large:
		large=i

	if i<small:
		small=i

for i in li:
	if i>large2:
		if i!=large:
			large2=i

	if i<small2:
		if i!=small:
			small2=i

print("Largest Element:",large)
print("Second Largest Element:",large2)
print("Smallest Element:",small)
print("Second Smallest Element:",small2)

