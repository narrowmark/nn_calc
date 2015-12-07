import random
import math

from infrastructure import *
from addition_set import add_set
from network import Network

def demo():
  params = iho_len(add_set[0])
  first = Network(params[0], params[1]/4, params[2])
  first.train(add_set)
  first.test(add_set)

if __name__ == '__main__':
  demo()
