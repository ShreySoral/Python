import numpy as np
import matplotlib.pyplot as plt
height = np.random.normal(160,30, 1000)
plt.hist(height, ec='gold',bins=30)
plt.show()