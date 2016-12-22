from matplotlib import pyplot as plt
import numpy as np

x,y = np.loadtxt('example_data.csv',
               unpack=True,
               delimiter=','
               )

plt.plot(x,y)
plt.title('Line from CSV')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()

