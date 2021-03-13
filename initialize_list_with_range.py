def initialize_list_with_range(end, start = 0, step = 1):
  return list(range(start, end + 1, step))

print(initialize_list_with_range(5))
print(initialize_list_with_range(7, 3))
print(initialize_list_with_range(9, 0, 2))