class Node:
	def __init__(self,value):
		self.data=value
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None 

	def Create(self,new_node):
		if self.head==None:
			self.head=new_node
		else:
			temp=self.head
			while(temp.next):
				temp=temp.next
			temp.next=new_node

	def insert(self,new_node,pos):
		if pos==1:
			new_node.next=self.head 
			self.head=new_node
		else:
			p=1
			temp=self.head
			while(p!=pos-1):
				temp=temp.next
				p+=1 
			new_node.next=temp.next
			temp.next=new_node 

	def delete(self,pos):
		if pos==1:
			temp=self.head
			self.head=temp.next
		else:
			p=1
			temp=self.head
			while(p!=pos-1):
				temp=temp.next
				p+=1
			temp.next=temp.next.next
			 
		
	def display(self):
		temp=self.head
		while(temp):
			print(temp.data,end="->")
			temp=temp.next
		print("None")


li1=LinkedList()
n1=Node(10)
n2=Node(20)
li1.Create(n1)
li1.Create(n2)
li1.Create(Node(30))
li1.Create(Node(40))
li1.display()

li1.insert(Node(90),3)
li1.insert(Node(50),5)
li1.display()

li1.delete(3)
li1.delete(1)
li1.delete(4) 
li1.display()