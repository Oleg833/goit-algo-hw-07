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

def find_max_value(root):
    while root.right is not None:
        root = root.right
    return root.key

def main():
  bst_root = None
  keys = [15, 8, 20, 6, 12, 17, 25]

  for key in keys:
      bst_root = insert(bst_root, key)


  max_value = find_max_value(bst_root)
  print("Найбільше значення в BST:", max_value)

if __name__ == "__main__":
    main()

