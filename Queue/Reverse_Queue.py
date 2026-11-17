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

	#Print stack
	def display(self):
		temp=self.top	
		while(temp):
			print(temp.data,end="-")
			temp=temp.next
		print()
	

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

	#Remove Front Element
	def dequeue(self):
		if self.front==None:
			print("Queue Is Empty1")
			return
		else:
			temp=self.front
			self.front=self.front.next
			if self.front==None:
				self.rear=None
			return temp.data
	
	#Check If Queue Is Empty
	def is_empty(self):
		if self.front:
			return False
		return True


	#Print Queue Elements
	def display(self):
		if self.front==None:
			print("Queue Is Empty")
			return 
		print("Queue:")
		temp=self.front
		while(temp):
			print(temp.data,end="-")
			temp=temp.next
		print()

	#Reverse Queue
	def reverseQueue(self,q):
		s=Stack()
		while not q.is_empty():
			s.push(Node(q.dequeue()))
		s.display()
		


q=Queue()
q.enqueue(Node(10))
q.enqueue(Node(20))
q.enqueue(Node(30))
q.enqueue(Node(40))
q.display()

print("Reverse Queue:")
q.reverseQueue(q)
