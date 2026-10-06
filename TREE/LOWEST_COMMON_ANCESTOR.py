class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def lca(root,p,q):
    if not root:
        return 0
    if root.key==p or root.key==q:
        return root
    left=lca(root.left,p,q)
    right=lca(root.right,p,q)
    if left and right:
        return root
    return left if left else right
if __name__ == "__main__":
    root = Node(20)
    root.left = Node(14)
    root.right = Node(24)
    root.left.right = Node(12)
    root.left.left = Node(15)
    root.right.left = Node(23)
    root.right.right = Node(30)

    lca1 = lca(root, 15, 12)
    print("LCA of 15 and 12:", lca1.key)  # Output: 14

    lca2= lca(root, 15, 23)
    print("LCA of 15 and 23:", lca2.key)  # Output: 20