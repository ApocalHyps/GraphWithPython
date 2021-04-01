import matplotlib.pyplot as plt
import math

filename = "DATA211"
skip = 24

xlab = "Longueur d'onde (nm)"
ylab = "Puissance (dBm)"

x_formula = lambda x: x
y_formula = lambda y: 10*math.log(y, 10)
#y_formula = lambda y: y*1000000

with open((filename+".txt"), 'r') as f:
	for i in range(skip):
		print("Discarding : " + f.readline().replace("\n", ""))
	data = f.read().split('\n')

x = []
y = []

for line in data:
	if line == "": continue
	t = line.split(",")
	x.append(x_formula(eval(t[0])))
	y.append(y_formula(eval(t[1])))

plt.plot(x, y)
plt.xlabel(xlab)
plt.ylim([-90, -50])
plt.ylabel(ylab)
plt.grid()
plt.show()

