def drop_right(a, n = 1):
  return a[:-n]

print(drop_right([1, 2, 3]))
print(drop_right([1, 2, 3], 2))
print(drop_right([1, 2, 3], 42))