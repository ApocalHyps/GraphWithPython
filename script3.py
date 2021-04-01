import matplotlib.pyplot as plt
import math
from numpy import linspace
from math import log

from math import pi
from math import exp

I_p = [0.5, 1, 1.5, 2, 2.5] # Courant A
P_p = [-7, 23.63, 27.1, 29.04, 30.26] # dBm
P_p_W = list(map(lambda p:10**(p/10), P_p)) #mW

I_s_20 = [-5.9, -3.32, -0.2, 3.08, 5.90]
I_s_40 = [0.48, 2.87, 6, 9.07, 11.44]
I_s_60 = [2.92, 5.35, 8.41, 10.65, 10.4]
I_s_80 = [4.44, 6.77, 9.22, 10.08, 10.8]
I_s_100 = [5.51, 7.55, 9.57, 9.58, 11.1]

I_s_20_p_0 = -5.9
I_s_40_p_0 = 0.48
I_s_60_p_0 = 2.92
I_s_80_p_0 = 4.44
I_s_100_p_0 = 5.50

gain_20 = [k-I_s_20_p_0 for k in I_s_20]
gain_40 = [k-I_s_40_p_0 for k in I_s_40]
gain_60 = [k-I_s_60_p_0 for k in I_s_60]
gain_80 = [k-I_s_80_p_0 for k in I_s_80]
gain_100 = [k-I_s_100_p_0 for k in I_s_100]

plt.plot(P_p_W, gain_20, label="{:.3} mW".format(10**(I_s_20_p_0/10)))
plt.plot(P_p_W, gain_40, label="{:.3} mW".format(10**(I_s_40_p_0/10)))
plt.plot(P_p_W, gain_60, label="{:.3} mW".format(10**(I_s_60_p_0/10)))
plt.plot(P_p_W, gain_80, label="{:.3} mW".format(10**(I_s_80_p_0/10)))
plt.plot(P_p_W, gain_100, label="{:.3} mW".format(10**(I_s_100_p_0/10)))

o = 1274e12
op = 1358e12
g_R = 1e-13
w = 5.05e-6
I_s = lambda P_pompe_0,P_signal_0,z: (1+(o * P_pompe_0 / (op * P_signal_0))) / (1+(o * P_pompe_0 / (op * P_signal_0))*exp(-g_R*z*P_pompe_0/(pi*(w**2))))


P_Pompe = linspace(0, 1000, num=100)
z = 10e3


Gain = lambda rapport : 10*log(rapport, 10)

P_signal = 2e-3
I_s_01 = list(map(lambda P : I_s(P/1000, P_signal, z), P_Pompe))

gain_theorique = list(map(Gain, I_s_01))

plt.plot(P_Pompe, gain_theorique, label="2mW théorique")

plt.xlabel("Puissance de pompe (mW)")
plt.ylabel("Gain sur le signal (dB)")
plt.grid()

plt.legend(title="Puissance de Signal Initiale")
plt.show()