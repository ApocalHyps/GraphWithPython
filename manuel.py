import matplotlib.pyplot as plt
import math

xname = "Intensité (mA)"
yname = "Puissance de sortie (dBm)"

x_data = [5*k for k in range(21)]
y_data = [-61, -30, -25.9, -9, -0.84, 1.84, 3.48, 4.65, 5.56, 6.31, 6.96, 7.51, 8, 8.44, 8.84, 9.2, 9.53, 9.84, 10.12, 10.39, 10.63]

y_data = list(map(lambda x:x+20, y_data))

plt.plot(x_data, y_data, "-o")
plt.ylabel(yname)
plt.xlabel(xname)
plt.grid()
plt.show()