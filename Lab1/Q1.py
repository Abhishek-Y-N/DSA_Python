n=int(input("Enter A Number:"))
print(f"Enter {n} elements:")
li=[]
sum=0

for i in range(0,n):
	num=int(input(f"Enter {i+1} Element:"))
	li.append(num)
	sum+=num

print("List:",li)
print("Addition Of Elemnts:",sum)