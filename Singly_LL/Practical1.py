class Node:
	def __init__(self,val):
		self.next=None
		self.data=val

class Linkedlist:
	def __init__(self):
		self.head=None

	def create(self,newnode):
		if self.head==None:
			self.head=newnode
		else:
			temp=self.head
			while(temp.next):
				temp=temp.next
			temp.next=newnode

	def insert(self,newnode,pos):
		if pos==1:
			newnode.next=self.head
			self.head=newnode
		else:
			temp=self.head
			p=1
			while(p!=pos-1):
				temp=temp.next
				p+=1
			newnode.next=temp.next
			temp.next=newnode

	def alter_delete(self):
		temp=self.head
		count=0
		while(temp):
			temp=temp.next
			count+=1
		temp=self.head
		for i in range(1,(count//2)+1):
			temp.next=temp.next.next
			temp=temp.next

	def display(self):
		temp=self.head
		while(temp):
			print(temp.data,end=" ")
			temp=temp.next
		print("None")

li=Linkedlist()
li.create(Node(10))
li.create(Node(20))
li.create(Node(30))
li.create(Node(40))
print("List created")

li.display()

#insert at 1st and 3rd position
li.insert(Node(90),1)
li.insert(Node(80),3)
li.display()

#display Alternate nodes
li.alter_delete()
li.display()