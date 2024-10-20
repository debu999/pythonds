from collections import deque


def rot_tomatoes(grid):
  rows = len(grid)
  cols = len(grid[0]) if rows > 0 else 0
  queue = deque()
  fresh_count = 0

  # Initialize the queue with all rotten tomatoes and count fresh tomatoes
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == 2:
        queue.append((r, c))
      elif grid[r][c] == 1:
        fresh_count += 1

  # Directions for up, down, left, right
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  days = 0

  # BFS to rot the tomatoes
  while queue and fresh_count > 0:
    for _ in range(len(queue)):
      r, c = queue.popleft()
      for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
          grid[nr][nc] = 2  # Rot the good tomato
          fresh_count -= 1
          queue.append((nr, nc))
    days += 1

  return (
    days if fresh_count == 0 else -1)  # Return -1 if there are still fresh tomatoes


# Sample tests
if __name__ == "__main__":
  # Test 1
  grid1 = [[2, 1, 0], [1, 1, 0], [0, 0, 0]]
  print(rot_tomatoes(grid1))  # Output: 4

  # Test 2
  grid2 = [[0, 1, 2], [1, 0, 1], [0, 1, 1]]
  print(rot_tomatoes(grid2))  # Output: -1 (not all tomatoes can rot)

  # Test 3
  grid3 = [[2, 2, 0], [1, 1, 1], [0, 1, 2]]
  print(rot_tomatoes(grid3))  # Output: 1

  # Test 4
  grid4 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
  print(rot_tomatoes(grid4))  # Output: -1 (no rotten tomatoes to start with)
