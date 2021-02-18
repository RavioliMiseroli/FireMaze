import matplotlib.pyplot as plt
import numpy as np

x = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9]
y = [0.85, 0.6, 0.45, 0.35, 0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.05, 0.05, 0, 0]
y2 = [0.95, 0.85, 0.75, 0.4, 0.35, 0.05, 0, 0, 0.05, 0, 0, 0, 0, 0, 0, 0.05, 0, 0]
plt.plot(x, y, label = "Strategy 1")
plt.plot(x, y2, label = "Strategy 2")
plt.xlabel(' Flammability ')
plt.ylabel(' Probability of Success')

plt.title(' Strategy 1 vs. Strategy 2 ')
plt.xticks(np.arange(0, 1, 0.1))
plt.yticks(np.arange(0, 1, 0.05))

plt.show()