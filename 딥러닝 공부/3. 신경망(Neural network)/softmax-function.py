import numpy as np

def softmax(a):
  c = np.array([np.min(a), np.max(a)])
  c = c[1] if np.max(np.abs(c)) == c[1] else c[0]
  exp_a = np.exp(a - c)
  sum_exp_a = np.sum(exp_a)
  return exp_a / sum_exp_a

a = np.array([9999, 9997, 9998])

print(softmax(a))