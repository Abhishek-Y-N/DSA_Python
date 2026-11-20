#Structure Of Node
class Node:
	def __init__(self,val):
		self.data=val
		self.left=None
		self.right=None

class BST:
	def __init__(self):
		self.root=None

	def insert(self,newnode):
		if self.root==None:
			self.root=newnode
			return

		temp=self.root
		while True:
			if newnode.data<temp.data:
				if temp.left==None:
					temp.left=newnode
					return
				else:
					temp=temp.left 
			else:
				if temp.right==None:
					temp.right=newnode
					return
				else:
					temp=temp.right
	#In-Order Traversal
	def inorder_display(self,r):
		if r==None:
			return
		self.inorder_display(r.left)
		print(r.data,end=" ")
		self.inorder_display(r.right)

	#Post-Order Traversal
	def postorder_display(self,r):
		if r==None:
			return
		self.postorder_display(r.left)
		self.postorder_display(r.right)
		print(r.data,end=" ")

	#Pre-Order Traversal
	def preorder_display(self,r):
		if r==None:
			return
		print(r.data,end=" ")
		self.preorder_display(r.left)
		self.preorder_display(r.right)

t=BST()
t.insert(Node(27))
t.insert(Node(14))
t.insert(Node(19))
t.insert(Node(35))
t.insert(Node(31))
t.insert(Node(10))
t.insert(Node(42))
t.insert(Node(15))
t.insert(Node(55))
t.insert(Node(92))
t.insert(Node(50))
t.insert(Node(-3))

print("\nIn-Order:",end="")
t.inorder_display(t.root)

print("\nPost-Order:",end="")
t.postorder_display(t.root)

print("\nPre-Order:",end="")
t.preorder_display(t.root)