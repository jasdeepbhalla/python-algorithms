


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def lca(root, n1, n2):
	
	if root is None:
		return None

	if (n1 < root.data and n2 < root.data):
		return lca(root.left, n1, n2)

	if (n1 > root.data and n2 > root.data):
		return lca(root.right, n1, n2)

	return root

def main():
	root = Node(20)
	root.left = Node(8)
	root.right = Node(22)
	root.left.left = Node(4)
	root.left.right = Node(12)
	root.left.right.left = Node(10)
	root.left.right.right = Node(14)

	n1 = 10
	n2 = 14
	t = lca(root, n1, n2)
	print "ssd"
	print "LCA of %d and %d is %d" %(n1, n2, t.data)


main()
