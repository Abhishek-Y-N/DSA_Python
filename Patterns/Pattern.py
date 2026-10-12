n=int(input("Enter no Of Rows:"))
count=0

for i in range(0,n):
	for j in range(0,i+1):
		print(chr(65+count),end=" ")
		count+=1
	print()