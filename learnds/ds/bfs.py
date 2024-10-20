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

  def bfs(self):
    """Perform a Breadth-First Search traversal on the binary tree."""
    if not self.root:
      return []

    queue = []  # Initialize the queue
    results = []  # List to store the visited nodes
    current_node = self.root  # Start with the root node

    queue.append(current_node)  # Append the root to the queue

    while queue:  # Loop until the queue is empty
      current_node = queue.pop(0)  # Get the first element in the queue
      results.append(current_node.value)  # Append the value to results

      if current_node.left:  # If there is a left child, add it to the queue
        queue.append(current_node.left)
      if current_node.right:  # If there is a right child, add it to the queue
        queue.append(current_node.right)

    return results  # Return the list of visited nodes


# Example usage
if __name__ == "__main__":
  # Create a binary tree
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)

  tree = BinaryTree(root)

  # Perform BFS traversal
  bfs_result = tree.bfs()
  print("BFS traversal of the binary tree:",
        bfs_result)  # Output: [1, 2, 3, 4, 5]
