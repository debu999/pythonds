def compute_lps(pattern):
  """Compute the Longest Prefix Suffix (LPS) array for the pattern."""
  lps = [0] * len(pattern)
  length = 0  # Length of the previous longest prefix suffix
  i = 1

  while i < len(pattern):
    if pattern[i] == pattern[length]:
      length += 1
      lps[i] = length
      i += 1
    else:
      if length != 0:
        length = lps[length - 1]  # Use the previous LPS value
      else:
        lps[i] = 0
        i += 1

  return lps


def kmp_search(text, pattern):
  """Search for occurrences of the pattern in the text using KMP algorithm."""
  lps = compute_lps(pattern)
  i = 0  # Index for text
  j = 0  # Index for pattern
  occurrences = []

  while i < len(text):
    if pattern[j] == text[i]:
      i += 1
      j += 1

    if j == len(pattern):
      occurrences.append(i - j)  # Found a match
      j = lps[j - 1]  # Use LPS to find the next match
    elif i < len(text) and pattern[j] != text[i]:
      if j != 0:
        j = lps[j - 1]  # Use LPS to skip characters in the pattern
      else:
        i += 1  # Move to the next character in the text

  return occurrences


# Example usage
if __name__ == "__main__":
  text = "ababcababcabc"
  pattern = "abc"
  result = kmp_search(text, pattern)
  print(f"Pattern found at indices: {result}")
