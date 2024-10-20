class MaxHeap:
  def __init__(self):
    self.heap = []

  def insert(self, value):
    self.heap.append(value)
    self._heapify_up(len(self.heap) - 1)

  def delete(self):
    if len(self.heap) == 0:
      return None
    if len(self.heap) == 1:
      return self.heap.pop()

    root = self.heap[0]
    self.heap[0] = self.heap.pop()
    self._heapify_down(0)
    return root

  def _heapify_up(self, index):
    parent_index = (index - 1) // 2
    if index <= 0:
      return
    elif self.heap[parent_index] < self.heap[index]:
      self.heap[parent_index], self.heap[index] = (
        self.heap[index],
        self.heap[parent_index],
      )
      self._heapify_up(parent_index)

  def _heapify_down(self, index):
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    largest = index

    if (
        len(self.heap) > left_child_index
        and self.heap[left_child_index] > self.heap[largest]
    ):
      largest = left_child_index

    if (
        len(self.heap) > right_child_index
        and self.heap[right_child_index] > self.heap[largest]
    ):
      largest = right_child_index

    if largest != index:
      self.heap[index], self.heap[largest] = self.heap[largest], self.heap[
        index]
      self._heapify_down(largest)

  def insert_new(self, value):
    current = len(self.heap)
    self.heap.append(value)
    while current > 0 and self.heap[current] > self.heap[
      self._parent(current)]:
      parent = self._parent(current)
      self._swap(current, parent)
      current = parent

  # We will be writing the _sink_down method in the next exercise.
  # But I need to include it here for the tests to work for remove.
  # So, don't peek at this one here.  :-)
  def _sink_down(self, index):
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
