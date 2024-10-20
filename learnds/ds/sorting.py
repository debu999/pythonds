def bubble_sort(my_list):
  """Sorts a list of integers in ascending order using the Bubble Sort algorithm."""
  n = len(my_list)

  # Iterate through the list from the last element to the first element
  for i in range(n - 1, 0, -1):
    # Iterate through the list from the first element to the element at position i - 1
    for j in range(i):
      # Compare the element at position j with the element at position j + 1
      if my_list[j] > my_list[j + 1]:
        # Swap the two elements
        my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

  return my_list  # Return the sorted list


def selection_sort(my_list):
  """Sorts a list of integers in ascending order using the Selection Sort algorithm."""
  n = len(my_list)

  # Iterate through the list from the first element to the second-to-last element
  for i in range(n - 1):
    min_index = i  # Set min_index to the index of the current element i

    # Iterate through the list from the element at position i + 1 to the last element
    for j in range(i + 1, n):
      # Compare the element at position j with the element at position min_index
      if my_list[j] < my_list[min_index]:
        min_index = j  # Update min_index to the index j

    # If the index i is not equal to min_index, swap the elements
    if i != min_index:
      my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

  return my_list  # Return the sorted list


def insertion_sort(my_list):
  """Sorts a list of integers in ascending order using the Insertion Sort algorithm."""
  n = len(my_list)

  # Iterate through the list from the second element to the last element
  for i in range(1, n):
    temp = my_list[i]  # Store the value of the element at position i
    j = i - 1  # Initialize j to the index of the previous element

    # While temp is less than the element at position j and j is >= 0
    while j >= 0 and temp < my_list[j]:
      my_list[j + 1] = my_list[
        j]  # Move the element at position j to position j + 1
      j -= 1  # Decrement j

    my_list[j + 1] = temp  # Place the value of temp at position j + 1

  return my_list  # Return the sorted list


# Example usage
if __name__ == "__main__":
  unsorted_list = [64, 25, 12, 22, 11]
  sorted_list = selection_sort(unsorted_list)
  print("Sorted list:",
        sorted_list)  # Output: Sorted list: [11, 12, 22, 25, 64]

# Example usage
if __name__ == "__main__":
  unsorted_list = [64, 34, 25, 12, 22, 11, 90]
  sorted_list = bubble_sort(unsorted_list)
  print("Sorted list:",
        sorted_list)  # Output: Sorted list: [11, 12, 22, 25, 34, 64, 90]

  unsorted_list = [64, 25, 12, 22, 11]
  sorted_list = insertion_sort(unsorted_list)
  print("Sorted list:",
        sorted_list)  # Output: Sorted list: [11, 12, 22, 25, 64]
