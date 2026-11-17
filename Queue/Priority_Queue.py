class Node:
	def __init__(self,value,pr):
		self.data=value
		self.priority=pr
		self.next=None

class PriorityQueue:
	def __init__(self):
		self.front=self.rear=None

	def enqueue(self,newnode):
		#if queue is empty newnode becomes first node
		if self.front==None:
			self.front=newnode
			return

		#For inserting at first position
		if self.front.priority>newnode.priority:
			newnode.next=self.front
			self.front=newnode 
		else:
			temp=self.front
			while temp:        
				if newnode.priority<=temp.priority:
					break
				prev=temp
				temp=temp.next
			prev.next=newnode
			newnode.next=temp

	#Delete Front Element
	def dequeue(self):
		if self.front:
			print(self.front.data,"Deleted")
			self.front=self.front.next
		else:
			print("Queue Is Empty!")

	#Display All Elemenet
	def display(self):
		temp=self.front
		while temp:
			print(temp.data,end="->")
			temp=temp.next
		print()
		
pq=PriorityQueue()
pq.enqueue(Node(10,2))
pq.enqueue(Node(20,1))
pq.enqueue(Node(30,4))
pq.enqueue(Node(40,3))
pq.display()

pq.dequeue()
pq.dequeue()
pq.display()