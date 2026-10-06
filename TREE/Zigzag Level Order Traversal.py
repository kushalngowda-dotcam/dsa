from collections import deque
class Node:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
def zigzagorder(root):
    if not root:
        return[]
    queue=deque([root])
    result=[]
    lefttoright=True
    while queue:
        size=len(queue)
        level_nodes=[]
        for _ in range(size):
            node=queue.popleft()
            level_nodes.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if not lefttoright:
            level_nodes.reverse()
        result.append(level_nodes)
        lefttoright=not lefttoright
    return result
if __name__ == "__main__":
    root = Node(20)
    root.left = Node(14)
    root.right = Node(24)
    root.left.left = Node(12)
    root.left.right = Node(15)
    root.right.left = Node(23)
    root.right.right = Node(30)

    print("Zigzag Traversal:", zigzagorder(root))

