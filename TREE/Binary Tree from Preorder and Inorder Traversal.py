class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def buildTree(preorder, inorder):
    # Map each value to its index in inorder for quick lookup
    inorder_index = {val: idx for idx, val in enumerate(inorder)}
    pre_index = [0]  # use list to make it mutable inside dfs

    def dfs(in_left, in_right):
        if in_left > in_right:
            return None
        root_val = preorder[pre_index[0]]
        root = Node(root_val)
        pre_index[0] += 1
        root.left = dfs(in_left, inorder_index[root_val] - 1)
        root.right = dfs(inorder_index[root_val] + 1, in_right)
        return root
    return dfs(0, len(inorder) - 1)
def print_inorder(root):
    if not root:
        return
    print_inorder(root.left)
    print(root.key, end=" ")
    print_inorder(root.right)

# Example usage
if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    root = buildTree(preorder, inorder)
    print("Inorder of constructed tree:", end=" ")
    print_inorder(root)
