class TreeNode:
  """Class representing a node in a binary tree."""

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BinaryTree:
  """Class to manage the binary tree."""

  def __init__(self, root=None):
    self.root = root


# Example usage
if __name__ == "__main__":
  # Create a binary tree
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)

  tree = BinaryTree(root)

  # Perform DFS Pre-Order traversal
  pre_order_result = tree.dfs_pre_order()
  print("Pre-Order DFS traversal of the binary tree:",
        pre_order_result)  # Output: [1, 2, 4, 5, 3]
