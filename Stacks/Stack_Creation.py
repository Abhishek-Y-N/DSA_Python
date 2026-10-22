#Stack Using LinkedList

#Structure of Node
class Node:
	def __init__(self,val):
		self.next=None
		self.data=val

class Stack:
	def __init__(self):
		self.top=None

	#check if stack is empty
	def isempty(self):
		return self.top==None

	#Add new element in stack
	def push(self,newnode):
		newnode.next=self.top
		self.top=newnode 

	#Remove top most element from stack
	def pop(self):
		if self.isempty():
			print("Stack Is Empty")
			return
		temp=self.top
		print(f"{temp.data} Popped")
		self.top=self.top.next
		temp=None

	#Print stack
	def display(self):
		temp=self.top	
		while(temp):
			print(temp.data,end="->")
			temp=temp.next
		print()

s=Stack()
s.push(Node(10))
s.push(Node(20))
s.push(Node(30))
s.push(Node(40))

s.display()

s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.display()