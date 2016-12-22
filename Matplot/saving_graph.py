
import numpy as np
import matplotlib.pyplot as plt

X=np.linspace(-np.pi,np.pi,256,endpoint=True)

C,S=np.cos(X),np.sin(X)
###creating y limit in y direction#####
plt.ylim(-2.0,2.0)
########$-------------$#########E

plt.plot(X,C,color="blue", linewidth=3.0, linestyle=":")
plt.plot(X,S)
plt.savefig("graphs//exercice.png",dpi=72)


plt.show()