class node:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
def validate_BST(root,low=float('-inf'),high=float('inf')):
    if not root:
        return True
    if not (low<root.key<high):
        return False
    return validate_BST(root.left,low,root.key) and validate_BST(root.right,root.key,high)
if __name__=='__main__':
    root=node(10)
    root.right=node(12)
    root.left=node(8)
    print(validate_BST(root))
