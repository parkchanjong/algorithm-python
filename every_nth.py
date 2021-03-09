def every_nth(lst, nth):
  return lst[nth - 1::nth]

print(every_nth([1, 2, 3, 4, 5, 6], 2))