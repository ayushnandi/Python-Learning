# importing 
# import matplotlib.pyplot as plt
# x= [1,2,3,4,5,6,7,8,9,10]
# y= [5,4,3,7,8,5,3,6,8,9]
# plt.plot(x,y)
# plt.xlabel('Time (s)')
# plt.ylabel('Temperature (degC)')
# plt.show()






# import numpy as np
# xstart = 0 
# xstop = 2*np.pi
# increment = 0.1

# x = np.arrange(xstart , xstop, increment)
# x = np.sin(x)

# plt.plot(x, y)
# plt.title('Sin')
# plt.xlable('x')
# plt.ylable('sin (X)')
# plt.show()







import numpy as np
xstart = 0 
xstop = 2*np.pi
increment = 0.1

x = np.arrange(xstart , xstop, increment)
x = np.sin(x)

plt.plot(x, y)
plt.title('Sin')
plt.xlable('x')
plt.ylable('sin (X)')
plt.show()

