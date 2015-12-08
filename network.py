import random
import math

from infrastructure import *

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

  def train(self, patterns, iterations=1000, learn_rate=0.3, momentum=0.1):
    for i in range(iterations):
      error = 0.0
      for p in patterns:
        inputs = p[0]
        targets = p[1]
        self.update(inputs)
        error += self.backpropagate(targets, learn_rate, momentum)
      if i % 100 == 0:
        print('Error %-.5f' % error)
