from collections import deque
class Node:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
def serialize(root):
    if not root:
        return[]
    queue=deque([root])
    result=[]
    while queue:
        node=queue.popleft()
        if node:
            result.append(node.key)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    return result
def deserialize(data):
    if not data or data[0] is None:
        return None
    root=Node(data[0])
    queue=deque([root])
    i=1
    while data and i<len(data):
        node=queue.popleft()
        if data[i] is not None:
            node.left=Node(data[i])
            queue.append(node.left)
        i+=1
        if  i < len(data) and data[i] is not None:
            node.right = Node(data[i])
            queue.append(node.right)
        i += 1

    return root

if __name__ == "__main__":
    root = Node(20)
    root.left = Node(14)
    root.right = Node(24)
    root.left.left = Node(12)
    root.left.right = Node(15)
    root.right.left = Node(23)
    root.right.right = Node(30)

    data = serialize(root)
    print("Serialized Tree:", data)

    new_root = deserialize(data)
    print("Deserialized Root:", new_root.key)


