import random
import math

# Converts a decimal number to a binary list.
def dec_bin(number):
  base = bin(number)[2:]
  bin_list = []
  [bin_list.append(int(x)) for x in list(base)]
  while len(bin_list) < 5:
    bin_list.insert(0, 0)
  return bin_list

def bin_dec(bin_list):
  base = ''
  for i in bin_list:
    base += str(i)
  return int(base, 2)

def threshold(inputs, line=0.5):
  outputs = []
  for i in inputs:
    if i < line:
      outputs.append(0)
    else:
      outputs.append(1)
  return outputs

# Returns decimal numbers between low and high.
def random_range(low, high):
  return (high - low) * random.random() + low

# Creates a matrix of row_num * col_num dimensions.
def new_matrix(row_num, col_num, fill=0.0):
  matrix = []
  for i in range(row_num):
    matrix.append([fill] * col_num)
  return matrix

def new_rand_matrix(row_num, col_num, low_fill, high_fill):
  matrix = new_matrix(row_num, col_num)
  for i in range(row_num):
    for j in range(col_num):
      matrix[i][j] = random_range(low_fill, high_fill)
  return matrix

def sigmoid(x):
  return math.tanh(x)

def sigmoid_prime(x):
  return 1.0 - x ** 2

def iho_len(test):
  return [len(test[0]), len(test[0]) + len(test[1]), len(test[1])]
