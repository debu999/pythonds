class Node:
  """Class representing a node in a binary tree."""

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BinaryTree:
  """Class to manage the binary tree."""

  def __init__(self, root=None):
    self.root = root

  def invert_tree(self):
    """Public method to invert the binary tree."""
    return self.__invert_tree(self.root)

  def __invert_tree(self, node):
    """Private helper method to invert the binary tree recursively."""
    if node is None:
      return None

    # Swap the left and right children
    node.left, node.right = node.right, node.left

    # Recursively invert the left and right subtrees
    self.__invert_tree(node.left)
    self.__invert_tree(node.right)

    return node


# Example usage
if __name__ == "__main__":
  # Create a binary tree
  root = Node(47)
  root.left = Node(21)
  root.right = Node(76)
  root.left.left = Node(15)
  root.left.right = Node(30)
  root.right.left = Node(50)
  root.right.right = Node(90)

  tree = BinaryTree(root)

  # Invert the binary tree
  inverted_root = tree.invert_tree()


  # Function to print the tree in-order for verification
  def print_in_order(node):
    if node:
      print_in_order(node.left)
      print(node.value)
      print_in_order(node.right)


  print("In-order traversal of the inverted binary tree:")
  print_in_order(inverted_root)


class Node:
  """Class representing a node in a binary tree."""

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
