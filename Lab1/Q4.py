n=int(input("Enter A Number:"))
print(f"Enter {n} elements:")
li=[]
flag=1

for i in range(0,n):
	num=int(input(f"Enter {i+1} Element:"))
	li.append(num)

target=int(input("Enter Element To Search:"))

for i in range(0,len(li)):
	if target==li[i]:
		print(f"Element {target} found at Index {i}")
		flag=0

if(flag):
	print("Element is Not Present")