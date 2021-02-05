from BinaryHeap import BST

A = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
B = list(sorted(A))

tree = BST(A)
A = tree.inorder(tree.root, [])
print(A)
print("\nSorting Successfully!" if A == B else "\n!!!!!Error!!!!!")