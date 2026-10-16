class Node:
	def __init__(self,value):
		self.data=value
		self.next=None
		self.prev=None

class LinkedList:
	def __init__(self):
		self.head=None 

	def create(self,new_node):
		if self.head==None:
			self.head=new_node
		else:
			temp=self.head
			while(temp.next):
				temp=temp.next
			temp.next=new_node
			new_node.prev=temp

	def display(self):
		temp=self.head
		while(temp):
			print(temp.data,end="->")
			temp=temp.next
		print("None")


li1=LinkedList()
li1.create(Node(10))
li1.create(Node(20))
li1.create(Node(30))
li1.create(Node(40))
li1.display()