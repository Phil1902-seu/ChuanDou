import numpy as np
import matplotlib.pyplot as plt

record = "Elcentro_NS.txt"
data = np.loadtxt(record)

dt = 0.02
nPts = len(data)

t = np.arange(dt, dt * (nPts + 1), 0.02)
a = data
amin = np.amin(a)
amax = np.amax(a)
PGA = max(sorted([amin, amax], key=abs))
plt.figure(figsize=(16, 8))
plt.plot(t, a)
plt.ylabel(' Acceleration (mm/s2)')
plt.xlabel('Time (s)')
plt.title("PGA = {}g".format(PGA/1000))
plt.show()
