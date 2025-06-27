import math

def median(input):
  x = len(input)
  mid = math.floor(x / 2)

  if x % 2 == 0:
    return (input[mid - 1] + input[mid]) / 2
  else:
    return input[mid]

my_list = [0, 1, 2, 3, 4, 5]
print(median(my_list))