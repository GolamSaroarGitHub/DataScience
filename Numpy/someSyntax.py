import numpy as np

b = np.array([[0, 1, 2], [3, 4, 5]])

print(b.ndim)  #prints the dimention of the array
print(b.shape) #it also prints the dimention of the array in different format

c = np.array([[[1], [2]], [[3], [4]]])
print(c.shape) #it also prints the dimention of the array in different format


d = np.linspace(0, 1, 6)   # start, end, num-points
print(d)

e = np.linspace(0, 1, 5, endpoint=False)
print(e)

a = np.ones((3, 3))
print(a)

b = np.zeros((2, 2))
print(b)


a_slice = np.arange(10)
b=a_slice[2:9:3]   # [start:end:step]
print("The sliced arrat is: ",end='')

print(b)