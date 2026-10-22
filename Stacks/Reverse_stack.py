#Stack Using LinkedList
class Node:
	def __init__(self,val):
		self.next=None
		self.data=val

class Stack:
	def __init__(self):
		self.top=None

	def isempty(self):
		return self.top==None

	def push(self,newnode):
		newnode.next=self.top
		self.top=newnode 

	def pop(self):
		if self.isempty():
			print("Stack Is Empty")
		else:
			temp=self.top
			print(f"{temp.data} Popped")
			self.top=self.top.next
			temp=None

	def reverse(self):
		temp=self.top
		while(temp):
			s2.push(Node(temp.data))
			temp=temp.next

	def display(self):
		temp=self.top	
		while(temp):
			print(temp.data,end="->")
			temp=temp.next
		print()

s=Stack()
s2=Stack()

s.push(Node(10))
s.push(Node(20))
s.push(Node(30))
s.push(Node(40))
s.display()

s.reverse()
s2.display()
