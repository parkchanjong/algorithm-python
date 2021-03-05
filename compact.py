def compact(lst):
  return list(filter(None, lst))

print(compact([0, 1, False, 2, '', 3, 'a', 's', 34]))