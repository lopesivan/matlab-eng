#!/usr/bin/env python
import matplotlib.pyplot as plt

i = [0, 0, 0, 33, 47, 65, 85]
v = [0, 80, 100, 120, 160, 180, 200]

plt.plot(v, i)
plt.xlabel('Tensao no secundario [V]')
plt.ylabel('Corrente no primario [mA]')
plt.grid(True)
plt.show()


