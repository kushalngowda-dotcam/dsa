class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def diameter(root):
    max_diameter = [0]  # use list to make it mutable inside dfs

    def dfs(node):
        if not node:
            return 0
        left_height = dfs(node.left)
        right_height = dfs(node.right)
        max_diameter[0] = max(max_diameter[0], left_height + right_height)
        return 1 + max(left_height, right_height)

    dfs(root)
    return max_diameter[0]

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)

    print("Diameter of the tree:", diameter(root))

