class Node:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
def preorder(root):
    if root:
        print(root.key,end="  ")
        preorder(root.left)
        preorder(root.right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end="  ")
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end="  ")
if __name__=='__main__':
    root=Node(20)
    root.left=Node(14)
    root.right=Node(24)
    root.left.right=Node(12)
    root.left.left=Node(15)
    root.right.left=Node(23)
    root.right.right=Node(30)
    print("Inorder Traversal: ")
    inorder(root)

    print("\nPreorder Traversal: ")
    preorder(root)

    print("\nPostorder Traversal: ")
    postorder(root)



