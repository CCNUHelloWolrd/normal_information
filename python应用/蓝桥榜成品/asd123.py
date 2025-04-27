import matplotlib.pyplot as plt
import numpy as np
list_x = [i for i in range(100)]
list_y = [np.sin(i) for i in list_x]

plt.figure(figsize=(2, 2))
plt.plot(list_x, list_y, "ro-")
plt.show()

