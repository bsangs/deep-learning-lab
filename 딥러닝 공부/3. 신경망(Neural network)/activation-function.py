import numpy as np
import matplotlib.pylab as plt

def step_function(x):
  return np.array(x > 0, dtype=np.int)

def sigmoid(x): # 계단 함수의 그래프를 곡선으로 바꿈 (매끄러움, 실수도 반환됨)
  return 1 / (1 + np.exp(-x)) # exp(x) = e^x

def relu(x): # 1 이상의 값을 반환할 수 있는 함수
  return np.maximum(0, x) # ReLU(Rectified Linear Unit)

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
y = step_function(x)
y = relu(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1) # Y limit
plt.show()