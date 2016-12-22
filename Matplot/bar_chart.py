from matplotlib import pyplot as plt
x=[2,5,6,5,4,8]
y=[7,8,9,5,4,6]

x2=[3,4,9,6,7]
y2=[1,5,8,2,9]
plt.bar(x,y,color='g')
plt.bar(x2,y2,color='c')
plt.title('Just Bars')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()