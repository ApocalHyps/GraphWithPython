o = 1274e12
op = 1358e12
g_R = 1e-13
from math import pi
from math import exp
w = 5.05e-6
I_s = lambda P_pompe_0,P_signal_0,z: (1+(o * P_pompe_0 / (op * P_signal_0))) / (1+(o * P_pompe_0 / (op * P_signal_0))*exp(-g_R*z*P_pompe_0/(pi*(w**2)))
I_p = lambda P_pompe_0,P_signal_0,z: (1+1/(o * P_pompe_0 / (op * P_signal_0))) / (1+1/(o * P_pompe_0 / (op * P_signal_0))*exp(+g_R*z*P_pompe_0/(pi*(w**2)))
import matplotlib.pyplot as plt
from numpy import linspace
P_Signal = linspace(0, 10e-3, num=100)
z = 10e3

from math import log
Gain = lambda rapport : 10*log(rapport, 10)

P_pompe = 0.1
I_s_01 = list(map(lambda P : I_s(P_pompe, P, z), P_Signal))
P_pompe = 0.5
I_s_05 = list(map(lambda P : I_s(P_pompe, P, z), P_Signal))
P_pompe = 2
I_s_2 = list(map(lambda P : I_s(P_pompe, P, z), P_Signal))

gain_01 = list(map(Gain, I_s_01))
gain_05 = list(map(Gain, I_s_05))
gain_2 = list(map(Gain, I_s_2))

#plt.semilogy(P_Pompe, I_s_01, label="0,1 mW")
#plt.semilogy(P_Pompe, I_s_05, label="0,5 mW")
#plt.semilogy(P_Pompe, I_s_2, label="2 mW")
#plt.ylabel("Rapport sortie/entrée de l'intensité signal")

plt.plot(P_Signal, gain_01, label="0,1 W")
plt.plot(P_Signal, gain_05, label="0,5 W")
plt.plot(P_Signal, gain_2, label="2 W")
plt.xlabel("Puissance du Signal Inital (W)")
plt.ylabel("Gain sur le signal (dB)")


plt.legend(title="Puissance de Pompe")
plt.show()