def in_range(n, start, end = 0):
  return start <= n <= end if end >= start else end <= n <= start

print(in_range(3, 2, 5))
print(in_range(3, 4))
print(in_range(2, 3, 5))
print(in_range(3, 2))