import random
import math

# Converts a decimal number to a binary list.
def dec_bin(number):
  base = bin(number)[2:]
  bin_list = []
  [bin_list.append(int(x)) for x in list(base)]
  while len(bin_list) < 4:
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

class Network:
  def __init__(self, inp, hid, out):
    self.inp = inp + 1
    self.hid = hid
    self.out = out

    self.inp_activation = [1.0] * self.inp
    self.hid_activation = [1.0] * self.hid
    self.out_activation = [1.0] * self.out

    self.inp_weight = new_rand_matrix(self.inp, self.hid, -0.2, 0.2)
    self.out_weight = new_rand_matrix(self.hid, self.out, -2.0, 2.0)

    self.inp_change = new_matrix(self.inp, self.hid)
    self.out_change = new_matrix(self.hid, self.out)

  def update(self, inputs):
    if len(inputs) != self.inp - 1:
      print "Need " + str(self.inp) + ", given " + str(len(inputs)) + " inputs"
      raise ValueError("Incorrect numbr of inputs")

    for i in range(self.inp - 1):
      self.inp_activation[i] = inputs[i]

    for j in range(self.hid):
      total = 0.0
      for i in range(self.inp):
        total += self.inp_activation[i] * self.inp_weight[i][j]
      self.hid_activation[j] = sigmoid(total)

    for j in range(self.out):
      total = 0.0
      for i in range(self.hid):
        total += self.hid_activation[i] * self.out_weight[i][j]
      self.out_activation[j] = sigmoid(total)

    return self.out_activation

  def backpropagate(self, targets, learn_rate, momentum):
    if len(targets) != self.out:
      raise ValueError("Incorrect number of targets")

    out_delta = [0.0] * self.out
    for k in range(self.out):
      error = targets[k] - self.out_activation[k]
      out_delta[k] = sigmoid_prime(self.out_activation[k]) * error

    hid_delta = [0.0] * self.hid
    for j in range(self.hid):
      error = 0.0
      for k in range(self.out):
        error += out_delta[k] * self.out_weight[j][k]
      hid_delta[j] = sigmoid_prime(self.hid_activation[j]) * error

    for j in range(self.hid):
      for k in range(self.out):
        change = out_delta[k] * self.hid_activation[j]
        self.out_weight[j][k] = self.out_weight[j][k] + learn_rate * change + \
                                momentum * self.out_change[j][k]
        self.out_change[j][k] = change

    for i in range(self.inp):
      for j in range(self.hid):
        change = hid_delta[j] * self.inp_activation[i]
        self.inp_weight[i][j] = self.inp_weight[i][j] + learn_rate * change + \
                                momentum * self.out_change[j][k]
        self.inp_change[i][j] = change

    error = 0.0
    for k in range(len(targets)):
      error += 0.5 * (targets[k] - self.out_activation[k]) ** 2
    return error


  def test(self, patterns):
    for p in patterns:
      print(p[0], '->', bin_dec(threshold(self.update(p[0]))))

  def train(self, patterns, iterations=1000, learn_rate=0.5, momentum=0.1):
    for i in range(iterations):
      error = 0.0
      for p in patterns:
        inputs = p[0]
        targets = p[1]
        self.update(inputs)
        error += self.backpropagate(targets, learn_rate, momentum)
      if i % 100 == 0:
        print('Error %-.5f' % error)

def demo():
  pat = [
    [dec_bin(0) + dec_bin(1), dec_bin(1)],
    [dec_bin(1) + dec_bin(0), dec_bin(1)],
    [dec_bin(0) + dec_bin(2), dec_bin(2)],
    [dec_bin(2) + dec_bin(0), dec_bin(2)],
    [dec_bin(4) + dec_bin(0), dec_bin(4)],
    [dec_bin(0) + dec_bin(4), dec_bin(4)]
  ]

  xor = [
    [[0,0],[0]],
    [[0,1],[1]],
    [[1,0],[1]],
    [[1,1],[0]]
  ]

  first = Network(8, 7, 4)
  first.train(pat)
  first.test(pat)

if __name__ == '__main__':
  demo()
