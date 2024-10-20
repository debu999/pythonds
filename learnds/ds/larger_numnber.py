def count_greater_elements1(arr):
  result = []
  for i in range(len(arr)):
    count = sum(1 for x in arr[i + 1:] if x > arr[i])
    result.append(count)
  return result


def count_greater_elements(arr):
  n = len(arr)
  rank = {val: i + 1 for i, val in enumerate(sorted(arr))}
  print(rank)
  bit = [0] * (n + 1)
  result = [0] * n

  def update(i):
    while i <= n:
      bit[i] += 1
      i += i & -i

  def query(i):
    res = 0
    while i > 0:
      res += bit[i]
      i -= i & -i
    return res

  for i in range(n - 1, -1, -1):
    result[i] = query(n) - query(rank[arr[i]])
    update(rank[arr[i]])

  return result


# Example usage:
arr = [1, 4, 2, 8, 12, 6, 9]
print(count_greater_elements(arr))  # Output: [6, 4, 4, 2, 0, 1, 0]
