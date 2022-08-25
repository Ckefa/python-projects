class Node:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None
		
class Tree:
		def __init__(self, root):
			self.root = Node(root)
			self.inod = []
			self.pre = []
			self.post = []
			
		def in_order(self):
			tree = self.root
			
			def left(root):
				if root:
					left(root.left)
					self.inod.append(root.data)
					print(root.data)
					left(root.right)
			left(tree)
			print("\n")
			
		def post_order(self):
			tree = self.root
			
			def right(root):
				if root:
					right(root.left)
					right(root.right)
					self.post.append(root.data)	
					print(root.data)
			right(tree)
			print()
			
			print(self.inod)
			print(self.pre)	
			print(self.post)
			
		def pre_order(self):
			tree = self.root
			
			def right(root):
				if root:
					self.pre.append(root.data)	
					print(root.data)
					right(root.left)
					right(root.right)
			right(tree)
			print()
		
				
mytree = Tree(7)
mt= mytree.root
mt.left = Node(5)
mt.left.left = Node(2)
mt.left.left.left = Node(3)
mt.left.left.right = Node(1)
mt.left.right  = Node(4)

mt.right = Node(8)
mt.right.right = Node(6)
mt.right.right.right = Node(9)
mt.right.right.left = Node(10)
mt.right.left= Node(11)

mytree.in_order()
mytree.pre_order()
mytree.post_order()
			
		