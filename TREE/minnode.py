class Node:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None

def inorder(root,result):
    if not root:
        return []
    inorder(root.left,result)
    result.append(root.key)
    inorder(root.right,result)
def displayre(root,result):
    result=[]
    inorder(root,result)
    return result[k-1]

if __name__ == "__main__":
    root = Node(20)
    root.left = Node(14)
    root.right = Node(24)
    root.left.left = Node(12)
    root.left.right = Node(15)
    root.right.left = Node(23)
    root.right.right = Node(30)
    k=3
    print(displayre(root,k))

