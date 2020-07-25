#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter


# In[97]:


# Generating an array of 1000 rolls of 3 die
rolls = np.random.randint(1, 6, size = (3, 1000))

# Calculating the sum
sum_of_rolls = np.sum(rolls, axis = 0)

# Plot Histogram
n, bins, kwargs = plt.hist(sum_of_rolls, bins = np.arange(19), density = True, histtype = 'step', align = 'left')

plt.figure(figsize = [10 ,5])
plt.plot(bins[3:-1], n[3:])
# plt.plot(np.linspace(0, 18, 100), np.interp(np.linspace(0, 18, 100), bins[:-1], n))
plt.plot(np.linspace(3, 18, 100), savgol_filter(np.interp(np.linspace(3, 18, 100), bins[:-1], n), 21, 2))
plt.xticks(np.linspace(0, 19, 20))
plt.ylim(0, max(n) * 1.05)
plt.xlim(2, 19)
plt.xlabel("Sum of the numbers on 3 die")
plt.ylabel("Probability of Sum of numbers")
plt.title('Barchart - Probability of Sum of numbers on 3 Die')
plt.savefig("Plot_1.png", dpi = 100)

plt.figure(figsize = [10 ,5])
plt.bar(bins[3:-1], n[3:])
plt.xticks(np.linspace(0, 19, 20))
# plt.ylim(0, max(n) * 1.05)
plt.ylim(0, max(n) * 1.05)
plt.xlim(2, 19)
plt.title('Barchart - Probabilities of Sum of Numbers on 3 die')
plt.xlabel("Sum of the numbers on 3 die")
plt.ylabel("Probability of Sum of numbers")
plt.savefig("Plot_2.png", dpi = 100)


# In[ ]:




