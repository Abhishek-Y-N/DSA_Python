n=int(input("Enter A Number:"))
print(f"Enter {n} elements:")
li=[]
count=0

for i in range(0,n):
	num=int(input(f"Enter {i+1} Element:"))
	if num==0:
		count+=1
	li.append(num)

print("Orignal List:",li)

for i in range(0,count):
	li.remove(0)

for i in range(0,count):
	li.append(0)
	
print("After Change:",li)