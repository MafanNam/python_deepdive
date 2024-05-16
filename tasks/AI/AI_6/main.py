import numpy as np
import matplotlib.pyplot as plt

f = open('ЕКГ_КП6_1.txt')
r = []
for line in f:
    line = line.strip()
    line = line.split('    ')
    r = r + line

Ar = np.array(r, dtype=float)
print(Ar.size)
print(Ar)
signal1 = np.reshape(Ar, (1253))

t = [i * 0.05 for i in range(len(signal1))]
d = np.gradient(signal1, t)

pause = int(input('Введіть паузу\n'))
y = np.zeros(len(signal1))
for i in range(pause, len(signal1)):
    y[i - pause] = signal1[i]

# Plotting
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(10, 8))

plt.subplots_adjust(wspace=0, hspace=0.4)
ax1.plot(t, signal1, color="yellow", linewidth=1)
ax1.grid(True)
ax1.set_title('Cигнал КП6')
ax1.set_facecolor('black')

ax2.plot(d, signal1, color="green", linewidth=1)
ax2.grid(True)
ax2.set_title('Фазовый портет dz/dt')
ax2.set_facecolor('black')

ax3.plot(y, signal1, color="white", linewidth=1)
ax3.grid(True)
ax3.set_title('Фазовый портер с задержкой')
ax3.set_facecolor('black')
fig.set_facecolor('grey')

plt.show()
