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

  def dfs_pre_order(self):
    """Perform a Depth-First Search (DFS) traversal in Pre-Order."""
    results = []  # List to store the visited nodes

    def traverse(current_node):
      if current_node is None:
        return

      # Visit the current node
      results.append(current_node.value)

      # Traverse the left subtree
      traverse(current_node.left)
      # Traverse the right subtree
      traverse(current_node.right)

    # Start the traversal from the root
    traverse(self.root)
    return results  # Return the list of visited nodes

  def dfs_post_order(self):
    """Perform a Depth-First Search (DFS) traversal in Pre-Order."""
    results = []  # List to store the visited nodes

    def traverse(current_node):
      if current_node is None:
        return

      # Traverse the left subtree
      traverse(current_node.left)
      # Traverse the right subtree
      traverse(current_node.right)

      # Visit the current node
      results.append(current_node.value)

    # Start the traversal from the root
    traverse(self.root)
    return results  # Return the list of visited nodes

  def dfs_in_order(self):
    """Perform a Depth-First Search (DFS) traversal in Pre-Order."""
    results = []  # List to store the visited nodes

    def traverse(current_node):
      if current_node is None:
        return

      # Traverse the left subtree
      traverse(current_node.left)
      # Visit the current node
      results.append(current_node.value)
      # Traverse the right subtree
      traverse(current_node.right)

    # Start the traversal from the root
    traverse(self.root)
    return results  # Return the list of visited nodes

  def is_valid_bst(self):
    """Check if the binary tree is a valid binary search tree."""
    values = self.dfs_in_order()  # Get the values in sorted order

    # Check if the values are in ascending order
    for i in range(1, len(values)):
      if values[i] <= values[i - 1]:  # Not strictly greater
        return False

    return True  # All values are in ascending order

  def kth_smallest_iterative(self, k):
    """Find the kth smallest element in the BST using an iterative approach."""
    stack = []
    current_node = self.root
    count = 0

    while stack or current_node:
      # Go to the leftmost node
      while current_node:
        stack.append(current_node)
        current_node = current_node.left

      # Process the node
      current_node = stack.pop()
      count += 1

      # If we've reached the kth smallest, return its value
      if count == k:
        return current_node.value

      # Move to the right child
      current_node = current_node.right

    return None  # If k is out of bounds


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
