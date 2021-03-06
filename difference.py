def difference(a, b):
  _b = set(b)
  return [item for item in a if item not in _b]

print(difference([1, 2, 3], [1, 2, 4]))
