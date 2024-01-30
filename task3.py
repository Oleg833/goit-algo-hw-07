class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.key < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def tree_sum(root):
    if root is None:
        return 0
    return root.key + tree_sum(root.left) + tree_sum(root.right)

def main():
    bst_root = None
    keys = [15, 8, 20, 6, 12, 17, 25]

    for key in keys:
        bst_root = insert(bst_root, key)


    total_sum = tree_sum(bst_root)
    print("Сума всіх значень в BST:", total_sum)

if __name__=="__main__":
    main()