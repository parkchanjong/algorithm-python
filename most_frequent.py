def most_frequent(lst):
  return max(set(lst), key = lst.count)

print(most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]))

def offset(lst, offset):
  return lst[offset:] + lst[:offset]

print(offset([1, 2, 3, 4, 5], 2))
print(offset([1, 2, 3, 4, 5], -2))

def similarity(a, b):
  return [item for item in a if item in b]

print(similarity([1, 2, 3], [1, 2, 4]))

def sum_by(lst, fn):
  return sum(map(fn, lst))

print(sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']))