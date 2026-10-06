class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


def maxpath(root):
    maxsum = float('-inf')

    def dfs(node):
        nonlocal maxsum
        if not node:
            return 0
        leftgain = max(dfs(node.left), 0)
        rightgain = max(dfs(node.right), 0)
        current_path = node.key + leftgain + rightgain
        maxsum = max(current_path, maxsum)
        return node.key + max(leftgain, rightgain)
    dfs(root)
    return maxsum


# Example usage
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)
    print("Maximum Path Sum:", maxpath(root))
