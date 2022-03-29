import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([6,5,7,8,7])

reg = np.polyfit(x,y,deg=1)     # out: array(slope, intercept)
print(reg)

#r_square
correlation_mat = np.corrcoef(x,y)
r = correlation_mat[0,1]
r_square = r**2
#print(correlation_mat)
print(r_square)

# Linear regression plot
trend = np.polyval(reg,x)
plt.scatter(x,y)
plt.plot(x,trend,'r')
plt.title('TITLE',fontsize = 14)
plt.legend('LEGEND',fontsize = 12)
plt.xlabel('XLABLE',fontsize = 12)
plt.ylabel('YLABLE',fontsize = 12)
plt.show()
