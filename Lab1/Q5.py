n=int(input("Enter A Number:"))
print(f"Enter {n} elements:")
li=[]
li2=[]

for i in range(0,n):
	num=int(input(f"Enter {i+1} Element:"))
	li.append(num)

print("List:",li)

for i in range(len(li)-1,-1,-1):
	li2.append(li[i])


print("Reverse List:",li2)