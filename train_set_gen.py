from random import random
from infrastructure import dec_bin

def addition_set(x=12, y=12, write=0):
  add_set = []
  """
  for i in range(x):
    col_set = []
    col_set.append(dec_bin(0) + dec_bin(i))
    col_set.append(dec_bin(0 + i))
    add_set.append(col_set)

  add_set.append([dec_bin(1) + dec_bin(0), dec_bin(1)])
  add_set.append([dec_bin(5) + dec_bin(3), dec_bin(8)])
  add_set.append([dec_bin(9) + dec_bin(0), dec_bin(9)])
  add_set.append([dec_bin(0) + dec_bin(11), dec_bin(11)])
  """
  add_set.append([dec_bin(0) + dec_bin(0), dec_bin(0)])
  add_set.append([dec_bin(0) + dec_bin(1), dec_bin(1)])
  add_set.append([dec_bin(0) + dec_bin(2), dec_bin(2)])
  add_set.append([dec_bin(0) + dec_bin(3), dec_bin(3)])
  add_set.append([dec_bin(0) + dec_bin(4), dec_bin(4)])
  add_set.append([dec_bin(0) + dec_bin(5), dec_bin(5)])
  add_set.append([dec_bin(0) + dec_bin(6), dec_bin(6)])
  add_set.append([dec_bin(0) + dec_bin(7), dec_bin(7)])
  add_set.append([dec_bin(0) + dec_bin(8), dec_bin(8)])
  add_set.append([dec_bin(0) + dec_bin(16), dec_bin(16)])
  add_set.append([dec_bin(1) + dec_bin(0), dec_bin(1)])
  add_set.append([dec_bin(8) + dec_bin(0), dec_bin(8)])
  add_set.append([dec_bin(16) + dec_bin(0), dec_bin(16)])
  """
  for i in range(x):
    col_set = []
    col_set.append(dec_bin(i) + dec_bin(0))
    col_set.append(dec_bin(i + 0))
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
