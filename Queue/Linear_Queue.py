class Node:
	def __init__(self,val):
		self.next=None
		self.data=val

class Queue:
	def __init__(self):
		self.front=None
		self.rear=None

	def enqueue(self,newnode):
		if self.front==None:
			self.front=self.rear=newnode
		else:
			self.rear.next=newnode
			self.rear=newnode

	def dequeue(self):
		if self.front==None:
			print("Queue Is Empty1")
			return
		else:
			temp=self.front
			self.front=self.front.next
			if self.front==None:
				self.rear=None
			temp=None


	def display(self):
		if self.front==None:
			print("Queue Is Empty")
			return 
		print("Queue:")
		temp=self.front
		while(temp):
			print(temp.data,end="->")
			temp=temp.next
		print()

q=Queue()
q.enqueue(Node(10))
q.enqueue(Node(20))
q.enqueue(Node(30))
q.enqueue(Node(40))
q.display()

q.dequeue()
q.display()
q.dequeue()