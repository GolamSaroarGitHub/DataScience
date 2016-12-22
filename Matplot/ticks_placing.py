
import numpy as np
import matplotlib.pyplot as plt


X=np.linspace(-np.pi,np.pi,256,endpoint=True)

C,S=np.cos(X),np.sin(X)
plt.plot(X,C)
plt.plot(X,S)

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])

plt.show()