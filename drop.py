def drop(a, n = 1):
  return a[n:]

print(drop([1, 2, 3]))
print(drop([1, 2, 3], 2))
print(drop([1, 2, 3], 42))