import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(-1, 1)
y = np.sin(x)
plt.plot(x,y)

title = "kite"
filename = "kite.jpg"

plt.title(title)
plt.savefig(filename)