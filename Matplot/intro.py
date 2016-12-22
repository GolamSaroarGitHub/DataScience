import matplotlib.pyplot as plt

import numpy as np


# This will create array with a linear spacing between 0&2 with 5 spacing
x=np.linspace(0,2,10)
y=np.array([2,5,9,15,18,5,13,4,8,7])

plt.plot(x,y,'ro')
plt.show()
