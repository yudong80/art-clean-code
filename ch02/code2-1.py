import numpy as np
import matplotlib.pyplot as plt

alpha = 0.7

x = np.arange(100)
y = alpha * x / x**(alpha+1)

plt.plot(x, y)

plt.grid()
plt.title('Pareto Distribution')
plt.show()