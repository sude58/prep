my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]
index = 0
while index < len(my_list):
  index_2 = 0
  while index_2 < len(my_list[index]):
    number = my_list[index][index_2]
    if number % 2 == 0:
      print(number)
    index_2 += 1
  index += 1