class MaxHeap:
  """A MaxHeap data structure that supports insertion and deletion of elements."""

  def __init__(self):
    """Initializes an empty MaxHeap."""
    self.heap = []

  def insert(self, value):
    """Inserts a new value into the MaxHeap."""
    self.heap.append(value)  # Add the new value to the end of the heap
    self._heapify_up(len(self.heap) - 1)  # Restore the heap property

  def remove(self):
    """Removes and returns the maximum value from the MaxHeap."""
    if not self.heap:
      return None  # Return None if the heap is empty
    if len(self.heap) == 1:
      return self.heap.pop()  # Remove and return the only element

    # Store the maximum value (root) to return later
    root_value = self.heap[0]
    # Move the last element to the root
    self.heap[0] = self.heap.pop()
    # Restore the heap property
    self._sink_down(0)
    return root_value  # Return the removed maximum value

  def _left_child(self, index):
    """Returns the index of the left child of the node at the given index."""
    return 2 * index + 1

  def _right_child(self, index):
    """Returns the index of the right child of the node at the given index."""
    return 2 * index + 2

  def _swap(self, index1, index2):
    """Swaps the elements at the two specified indices in the heap."""
    self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

  def _heapify_up(self, index):
    """Restores the heap property by moving the element at the given index up."""
    while index > 0:
      parent_index = (index - 1) // 2
      if self.heap[index] > self.heap[parent_index]:
        self._swap(index, parent_index)
        index = parent_index
      else:
        break

  def _sink_down(self, index):
    """Restores the heap property by moving the element at the given index down."""
    max_index = index
    while True:
      left_index = self._left_child(index)
      right_index = self._right_child(index)

      if (left_index < len(self.heap) and
          self.heap[left_index] > self.heap[max_index]):
        max_index = left_index

      if (right_index < len(self.heap) and
          self.heap[right_index] > self.heap[max_index]):
        max_index = right_index

      if max_index != index:
        self._swap(index, max_index)
        index = max_index
      else:
        return


def find_kth_smallest(nums, k):
  """Finds the kth smallest element in the list using a MaxHeap."""
  max_heap = MaxHeap()

  # Insert the first k elements into the max heap
  for num in nums[:k]:
    max_heap.insert(num)

  # Process the remaining elements
  for num in nums[k:]:
    if num < max_heap.heap[0]:  # Compare with the max element in the heap
      max_heap.remove()  # Remove the largest element
      max_heap.insert(num)  # Insert the new number

  return max_heap.heap[
    0]  # The root of the max heap is the kth smallest element


def stream_max(nums):
  """Returns a list of the maximum numbers seen so far in the input list."""
  max_heap = MaxHeap()
  max_values = []

  for num in nums:
    max_heap.insert(num)  # Insert the current number into the max heap
    max_values.append(max_heap.heap[0])  # The root is the maximum so far

  return max_values


# Example usage
if __name__ == "__main__":
  nums1 = [3, 2, 1, 5, 6, 4]
  k1 = 2
  print(find_kth_smallest(nums1, k1))  # Output: 2

  nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
  k2 = 4
  print(find_kth_smallest(nums2, k2))  # Output: 3
