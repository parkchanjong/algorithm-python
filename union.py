def union(a, b):
  return list(set(a + b))

print(union([1, 2, 3], [4, 3, 2]))

def unique_elements(li):
  return list(set(li))

print(unique_elements([1, 2, 2, 3, 4, 3]))

def values_only(flat_dict):
  return list(flat_dict.values())

ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
print(values_only(ages))