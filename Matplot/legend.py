from matplotlib import pyplot as plt
x=[2,5,6,5,4,8,9]
y=[7,8,9,5,4,6,8]

x2=[2,5,6,5,4,8,9]
y2=[1,5,8,2,9,6,3]
plt.plot(x,y,'g',linewidth=5,label='line 1')
plt.plot(x2,y2,'c',linewidth=10,label='line 2')
plt.title('Just Lines')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.show()