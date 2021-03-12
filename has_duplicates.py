def has_duplicates(lst):
  return len(lst) != len(set(lst))

x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]

print(has_duplicates(x))
print(has_duplicates(y))