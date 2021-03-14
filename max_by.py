def max_by(lst, fn):
  return max(map(fn, lst))

print(max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) )

def max_element_index(arr):
  return arr.index(max(arr))

print(max_element_index([5, 8, 9, 7, 10, 3, 0]) )


def max_n(lst, n = 1):
  return sorted(lst, reverse = True)[:n]

print(max_n([1, 2, 3]))
print(max_n([1, 2, 3], 2))