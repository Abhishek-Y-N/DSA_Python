class Node:
	def __init__(self,value):
		self.data=value
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None 

	def create(self,new_node):
		if self.head==None:
			self.head=new_node
		else:
			temp=self.head
			while(temp.next!=self.head):	#Traversing to last node
				temp=temp.next
			temp.next=new_node
		new_node.next=self.head   #set new_node to head 

	def insert(self, new_node, pos):
		if pos == 1:
			temp = self.head
			while temp.next != self.head:
				temp = temp.next
			new_node.next = self.head
			temp.next = new_node
			self.head = new_node
		else:
			p = 1
			temp = self.head
			while p < pos - 1 and temp.next != self.head:
				temp = temp.next
				p += 1
			if p == pos - 1:
				new_node.next = temp.next
				temp.next = new_node

	def delete(self, pos):

		if pos == 1:
			temp = self.head

			if temp.next == self.head:
				self.head = None
				return
			last = self.head
			while last.next != self.head:
				last = last.next

			self.head = temp.next
			last.next = self.head
			return
		temp = self.head
		p = 1

		while p < pos - 1 and temp.next != self.head:
			temp = temp.next
			p += 1

		temp.next = temp.next.next
			 
		
	def display(self):
		temp=self.head
		while(True):
			print(temp.data,end="->")
			temp=temp.next
			if temp==self.head:		#Terminate loop when temp reaches head at last node
				break
		print("Head")


li1=LinkedList()
li1.create(Node(10))
li1.create(Node(20))
li1.create(Node(30))
li1.create(Node(40))
li1.display()

li1.insert(Node(90),1)
li1.insert(Node(50),5)
li1.display()

li1.delete(3)
li1.display()