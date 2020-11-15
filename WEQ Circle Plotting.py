import matplotlib.pyplot as plt
from random import random
import numpy as np

#plotting circle
t = np.linspace(0,np.pi*2,100)
plt.plot(np.cos(t), np.sin(t), 'k', linewidth=1)

gamma = random()
n = 300
print(gamma)
x = []
y = []
title = "Gamma = " + str(gamma)
for i in range(1,n+1):
    colnum = i % 7
    colours = ['b.','g.','r.','c.','m.','y.','k.']
    num = "number" + str(i)
    gmod = 2 * np.pi * ((i * gamma) % 1)
    x.append(np.sin(gmod))
    y.append(np.cos(gmod))
    plt.plot(np.cos(t), np.sin(t), 'k', linewidth=1)
    plt.plot(x, y, 'b.',markersize = 10)
    plt.plot(x[-1], y[-1], 'r.', markersize = 10)
    plt.title(title)
    plt.savefig(num)
