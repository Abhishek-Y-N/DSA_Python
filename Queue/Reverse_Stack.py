#Structure of Node
class Node:
	def __init__(self,val):
		self.next=None
		self.data=val

class Stack:
	def __init__(self):
		self.top=None

	#Add new element in stack
	def push(self,newnode):
		newnode.next=self.top
		self.top=newnode 

	#Remove Last Element
	def pop(self):
		if self.is_empty():
			print("Stack Is Empty")
		else:
			temp=self.top
			self.top=self.top.next
			return temp.data

	#Check If Stack Is Empty
	def is_empty(self):
		if self.top:
			return False
		return True

		
	#Print stack
	def display(self):
		temp=self.top	
		while(temp):
			print(temp.data,end="-")
			temp=temp.next
		print()

	#Reverse Stack
	def reverseStack(self,s):
		q=Queue()
		while not s.is_empty():
			q.enqueue(Node(s.pop()))
		q.display()
	

class Queue:
	def __init__(self):
		self.front=None
		self.rear=None

	#Add Elements to Queue
	def enqueue(self,newnode):
		if self.front==None:
			self.front=self.rear=newnode
		else:
			self.rear.next=newnode
			self.rear=newnode

	#Print Queue Elements
	def display(self):
		if self.front==None:
			print("Queue Is Empty")
			return 
		temp=self.front
		while(temp):
			print(temp.data,end="-")
			temp=temp.next
		print()
		


s=Stack()
s.push(Node(10))
s.push(Node(20))
s.push(Node(30))
s.push(Node(40))
s.display()

print("Reverse Stack:")
s.reverseStack(s)
