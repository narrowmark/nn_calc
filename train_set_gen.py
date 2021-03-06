from random import random
from infrastructure import dec_bin

def addition_set(x=12, y=12, write=0):
  add_set = []
  for i in range(5):
    col_set = []
    #col_set.append(dec_bin(0) + dec_bin(i))
    col_set.append([0, 2**i])
    col_set.append(dec_bin(0 + 2**i))
    add_set.append(col_set)

  for i in range(5):
    col_set = []
    #col_set.append(dec_bin(i) + dec_bin(0))
    col_set.append([2**i, 0])
    col_set.append(dec_bin(2**i + 0))
    add_set.append(col_set)

  for i in range(5):
    col_set = []
    col_set.append([1, i])
    col_set.append(dec_bin(1 + i))
    add_set.append(col_set)

  for i in range(5):
    col_set = []
    col_set.append([i, 1])
    col_set.append(dec_bin(i + 1))
    add_set.append(col_set)

  """
  for i in range(8):
    col_set = []
    col_set.append([0, i])
    col_set.append(dec_bin(0 + i))
    add_set.append(col_set)
  """

  """
  #x = [0, 2, 4, 8, 12, 16, 20]
  #y = [31, 24, 16, 18, 8, 10]

  #x = [2, 5, 3, 1, 7, 4, 2, 4, 6]
  #y = [1, 6, 2, 4, 3, 3, 7, 8, 5]

  x = [1, 2, 2, 4, 5, 8]
  y = [1, 2, 3, 4, 3, 8]
  for i, j in zip(x, y):
    col_set = []
    #col_set.append(dec_bin(i) + dec_bin(j))
    col_set.append(dec_bin(i + j))
    add_set.append(col_set)
  """

  if (write == 1):
    file = open('addition_set.py', 'w+')
    file.write('add_set = [')
    for test in add_set:
      file.write(str(test) + ",\n")
    file.write(']')
    file.close

  return add_set

if __name__ == '__main__':
  test = addition_set(write=1)
