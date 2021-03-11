def for_each(itr, fn):
  for el in itr:
    fn(el)

for_each([1, 2, 3], print)