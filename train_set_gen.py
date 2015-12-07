from infrastructure import dec_bin

def addition_set(x=10, y=10, write=0):
  add_set = []
  for i in range(x):
    for j in range(y):
      col_set = []
      col_set.append(dec_bin(i) + dec_bin(j))
      col_set.append(dec_bin(i + j))
      add_set.append(col_set)

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
