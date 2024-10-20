class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class BinarySearchTree:
  def sorted_list_to_bst(self, nums):
    if not nums:
      return None
    return self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

  def __sorted_list_to_bst(self, nums, left, right):
    if left > right:
      return None
    mid = (left + right) // 2
    root = TreeNode(nums[mid])
    root.left = self.__sorted_list_to_bst(nums, left, mid - 1)
    root.right = self.__sorted_list_to_bst(nums, mid + 1, right)
    return root
