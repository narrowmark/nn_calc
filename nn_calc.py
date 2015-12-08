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
  first.test([[dec_bin(4) + dec_bin(0), dec_bin(4)]])
  first.test([[dec_bin(8) + dec_bin(0), dec_bin(8)]])

if __name__ == '__main__':
  demo()
