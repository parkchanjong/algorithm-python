def min_by(lst, fn):
  return min(map(fn, lst))

print(min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']))


def min_n(lst, n = 1):
  return sorted(lst, reverse = False)[:n]

print(min_n([1, 2, 3]))
print(min_n([1, 2, 3], 2))

def most_frequent(lst):
  return max(set(lst), key = lst.count)

print(most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]))