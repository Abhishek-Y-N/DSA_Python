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

	def insert(self,new_node,pos):
		if pos==1:
			new_node.next=self.head 
			self.head.prev=new_node 
			self.head=new_node
		else:
			p=1
			temp=self.head
			while(p!=pos-1 and temp.next):
				temp=temp.next
				p+=1 
			if temp.next:	#insert at last position
				temp.next.prev=new_node

			new_node.next=temp.next
			new_node.prev=temp
			temp.next=new_node

	
	def delete(self, pos):
		if self.head is None:
			print("List Is Empty")
			return
		temp = self.head
		if pos==1:
			self.head=temp.next

			if self.head:
				self.head.prev=None
			temp = None
			return
		p=1
		while temp is not None and p < pos:
			temp = temp.next
			p += 1
		if temp is None:
			print("Invalid Position")
			return
		temp.prev.next = temp.next
		if temp.next:
			temp.next.prev = temp.prev
		temp = None

	def reverse_print(self):
		temp=self.head
		while(temp.next):
			temp=temp.next
		print("List In Reverse Order:",end="")
		while(temp):
			print(temp.data,end="->")
			temp=temp.prev
		print("None")

	def occurance(self,val):
		temp=self.head
		count=0
		while(temp):
			if temp.data == val:
				count+=1
			temp=temp.next
		print(f"Count of {val} is {count}")


li=LinkedList()
li.create(Node(10))
li.create(Node(20))
li.create(Node(30))
li.create(Node(10))
li.create(Node(40))
li.display()

li.insert(Node(90),3) 	#insert at middle position 
li.insert(Node(11),1) 	#insert at 1st position
li.display()
print()

li.delete(1)
print("1st Position Deleted")
li.display()

li.delete(3)	#Need fix
print("3rd Position Deleted")
li.display()

li.reverse_print()

li.occurance(10)