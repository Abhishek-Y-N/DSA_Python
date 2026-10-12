n=int(input("Enter A Number:"))
print(f"Enter {n} elements:")
li=[]
odd=0
even=0

for i in range(0,n):
	li.append(int(input(f"Enter {i+1} Element:")))
	if li[i]%2==0:
		even+=1
	else:
		odd+=1


print("List:",li)
print("Odd:",odd)
print("Even:",even)