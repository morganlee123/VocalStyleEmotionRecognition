# Author: Morgan Sandler (sandle20@msu.edu)
# Only boxplot of the baseline scores

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import describe

# Load baseline scores
scores = np.fromfile('./baseline.txt', sep=', ')
print(scores)
print(describe(scores))

plt.boxplot(scores)
plt.show()
"""
import random
c = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(15)]

plt.bar(scores['comp'], scores['sim'], color=c, edgecolor='black')
plt.xticks(rotation = 45)
plt.show()  
"""