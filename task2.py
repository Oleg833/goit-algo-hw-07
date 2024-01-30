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

def find_min_value(root):
    while root.left is not None:
        root = root.left
    return root.key

def main():
    bst_root = None
    keys = [15, 8, 20, 6, 12, 17, 25]

    for key in keys:
        bst_root = insert(bst_root, key)

    min_value = find_min_value(bst_root)
    print("Найменше значення в BST:", min_value)

if __name__=="__main__":
    main()