print("Hello, world!!")

def mean(input):
  sum = 0
  for entry in input:
    sum += entry
  return sum / len(input)

my_list = [0, 1, 2, 3, 4, 5]
print(mean(my_list))
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
