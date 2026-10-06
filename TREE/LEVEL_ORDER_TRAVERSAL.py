from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def levelorder(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.key)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

if __name__ == "__main__":
    root = Node(20)
    root.left = Node(14)
    root.right = Node(24)
    root.left.right = Node(12)
    root.left.left = Node(15)
    root.right.left = Node(23)
    root.right.right = Node(30)

    print("Level Order Traversal:")
    print(levelorder(root))  # Output: [20, 14, 24, 15, 12, 23, 30]
