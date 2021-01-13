import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math

v = int(input("Podaj prędkość początkową(m/s): "))
alfa = int(input("Podaj kąt rzutu: "))
g = 9.81
time = 2 * v * np.sin(math.radians(alfa)) / g   # całkowity czas
t = np.linspace(0, time, num=20 * int(time))    # czas jako parametr
h = (v**2 * np.sin(math.radians(alfa))**2)/(2 * g) # max wysokość
z = (v**2 * np.sin(math.radians(2 * alfa)))/ g  # zasięg
print("Wysokość maksymalna: ", round(h, 2),"m; Zasięg rzutu: ", round(z, 2),"m; Czas lotu: ", round(time, 2), "s")
x = ((v * t) * np.cos(math.radians(alfa)))
y = ((v * t) * np.sin(math.radians(alfa))) - ((0.5 * g) * (t ** 2))
vx = v * np.cos(math.radians(alfa))    # prędkość chwilowa pozioma
vy = v * np.sin(math.radians(alfa)) - g * t    # prędkość chwilowa pionowa
fig, axs = plt.subplots(3)
fig.suptitle('Rzut ukośny')
axs[0].plot(t, vy, label='vy')
axs[0].hlines(y=vx, xmin=0, xmax=time, color='r', linestyle='-' , label='vx')
axs[0].set_xlim([-0.5,time+0.5])
axs[0].legend()
axs[1].plot(t, x, color="purple")
axs[1].set_ylabel('x', color="purple")

ax2 = axs[1].twinx()  # instantiate a second axes that shares the same x-axis
ax2.set_ylabel('y', color="g")  # we already handled the x-label with ax1
ax2.plot(t, y, color="green")
ax2.tick_params(axis='y')
axs[1].set_xlim([-0.5,time+0.5])
axs[2].plot(x, y)
axs[2].set_ylim([0,h+5])
axs[2].set_xlim([0,z+5])
axs[2].set_xlabel('x')
axs[2].set_ylabel('y')
plt.show()

