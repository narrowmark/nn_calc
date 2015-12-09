import random
import math

from infrastructure import *
from addition_set import add_set
from network import Network

def demo():
  params = iho_len(add_set[0])
  first = Network(params[0], params[1], params[2])
  first.train(add_set)
  first.test(add_set)
  """
  x = [0, 1, 2, 3, 4, 5, 6]
  y = [9, 8, 7, 6, 4, 3, 3]
  print ''
  for i, j in zip(x, y):
    first.test([[dec_bin(i) + dec_bin(j), dec_bin(i + j)]])
  """
  print ''
  for i in range(32):
    first.test([[dec_bin(i) + dec_bin(0), dec_bin(i + 0)]])
  print ''
  for i in range(22):
    print "Testing " + str(i)
    for j in range(8):
      first.test([[dec_bin(i) + dec_bin(j), dec_bin(i + j)]])

if __name__ == '__main__':
  demo()
