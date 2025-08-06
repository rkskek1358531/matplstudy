
import matplotlib.pyplot as plt
import numpy as np

stock_a = [100, 102, 99, 101, 101, 100, 102]
stock_b = [98, 95, 102, 104, 105, 103, 109]
stock_c = [110, 115, 100, 105, 100, 98, 95]

plt.plot(stock_a, label='A')
plt.plot(stock_b, label='B')
plt.plot(stock_c, label='C')

plt.legend(loc='lower right')
plt.show()

