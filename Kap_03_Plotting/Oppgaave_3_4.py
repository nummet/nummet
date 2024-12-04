import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 24, 200)
y = 3.2 * np.sin(np.pi/6*(x-3))

plt.rcParams.update({'font.size': 15})

plt.xlabel('t [timar]')
plt.ylabel('T [meter]')

plt.plot(x, y, linewidth=3, label='T(t)')
plt.hlines(-1, 0, 24, 'k', label='y=-1')
plt.plot(np.array([6, 18]), np.array([3.2, 3.2]), 'ro', 
         linewidth=2, label='Flo')
plt.plot(np.array([2.39, 9.61, 14.39, 21.61]), 
         -np.ones([4, 1]), 'md', linewidth=2, 
         label='T(t)=-1')

plt.axis([0, 27, -4, 4])
plt.grid(visible=True)
plt.legend(loc='upper right')
plt.show()