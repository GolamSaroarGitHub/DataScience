import numpy as np

a=np.random.random_integers(0,20,15)
print(a)
mask=a%3==0
print(mask)

# change the value everywhere
a[a%3==0]=-1

extrac_from_a=a[mask]
print(extrac_from_a)

print(a)