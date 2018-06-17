import matplotlib.pyplot as plt
import numpy as np

f = lambda x: x**2
xx = np.linspace(-3,3,100) 
yy = f(xx) + np.random.rand(100)

plt.plot(xx, yy)
plt.show()
