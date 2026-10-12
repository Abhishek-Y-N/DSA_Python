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

	def reverse(self):	#Reverse Linked List
		curr=self.head
		prev=None
		while(curr):
			nextnode=curr.next
			curr.next=prev 
			prev=curr
			curr=nextnode
		self.head=prev

	def middle(self):
		temp=temp1=self.head 
		prev=None
		while(temp1 and temp1.next):
			temp=temp.next
			temp1=temp1.next.next
		print("Middle Node:",temp.data)
		# prev.next=temp.next			#Deleting middle node(Not Working)
		# temp=None
			
		
	def display(self):
		temp=self.head
		while(temp):
			print(temp.data,end="->")
			temp=temp.next
		print("None")

	def delete(self):
		#For Deletion of First Node
		temp=self.head
		self.head=temp.next
		temp=None
		print("1st Node Deleted")

		#For Deletion Of Last Node
		prev=None
		temp=self.head
		while(temp.next):
			prev=temp 
			temp=temp.next

		prev.next=None
		temp.next=None
		print("Last Node Deleted")



li1=LinkedList()
li1.Create(Node(10))
li1.Create(Node(20))
li1.Create(Node(30))
li1.Create(Node(40))
li1.Create(Node(50))
li1.display()

li1.reverse()
li1.display()

li1.middle()
li1.display()

li1.delete()
li1.display()
