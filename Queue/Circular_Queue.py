class Node:
	def __init__(self,val):
		self.next=None
		self.data=val

class CQueue:
	def __init__(self):
		self.front=None
		self.rear=None

	def enqueue(self,newnode):
		if self.front==None:
			self.front=self.rear=newnode
		else:
			self.rear.next=newnode
			self.rear=newnode
		self.rear.next=self.front    #Last Node points to Front node

	def dequeue(self):
		if self.front==None:
			print("Queue Is Empty")
			return
		
		if self.front==self.rear:	#if queue conatins only one node 
			self.front=None
			self.rear=None
			return
		
		temp=self.front
		self.front=self.front.next
		self.rear.next=self.front
		temp=None

	def display(self):
		if self.front==None:
			print("Queue Is Empty")
			return 
		
		print("Queue:")
		temp=self.front
		while(True):
			print(temp.data,end="->")
			temp=temp.next
			if temp==self.front:
				break
		print("front")


q=CQueue()
q.enqueue(Node(10))
q.enqueue(Node(20))
q.enqueue(Node(30))
q.enqueue(Node(40))
q.display()

q.dequeue()
q.display()
q.dequeue()
q.display()