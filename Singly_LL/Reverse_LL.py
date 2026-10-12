class Node:
	def __init__(self,value):
		self.data=value
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None 

	def reverse(self):	#Reverse Linked List
		curr=self.head
		prev=None
		while(curr):
			nextnode=curr.next
			curr.next=prev 
			prev=curr
			curr=nextnode
		self.head=prev

	def Create(self,new_node):
		if self.head==None:
			self.head=new_node
		else:
			temp=self.head
			while(temp.next):
				temp=temp.next
			temp.next=new_node

			 
		
	def display(self):
		temp=self.head
		while(temp):
			print(temp.data,end="->")
			temp=temp.next
		print("None")


li1=LinkedList()
li1.Create(Node(10))
li1.Create(Node(20))
li1.Create(Node(30))
li1.Create(Node(40))
li1.Create(Node(50))
li1.display()

li1.reverse()
li1.display()


