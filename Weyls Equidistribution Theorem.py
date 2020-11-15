import matplotlib.pyplot as plt
from random import random
import numpy as np

n = 1000
gamma = random()
nest = 100

def weq(gamma,n,nest):
    yjlist = []
    x = range(1,n+1)
    j = 0
    while j < nest:
        yj = []
        card = 0
        a = random()
        b = random()
        if a > b:
            a, b = b, a
        for i in x:
            if a <= (i * gamma) %1 <= b:
                card += 1
            yj.append((card/i - (b-a))**2)
        yjlist.append(yj)
        j += 1
    arrays = [np.array(x) for x in yjlist]
    y = [np.mean(k) for k in zip(*arrays)]
    return x, y

colours = ['b.','g.','r.','c.','m.','y.','k.']
actcolours = [" blue", " green", " red", " cyan", " magenta", " yellow"," black"]

gammalist = []
for i in range(0,len(colours)):
    gamma = random()
    # while 0 <= gamma < 0.09 or 0.11 < gamma <= 1 :
    #     gamma = random()
    gammalist.append(gamma)
gammalist.sort(reverse=True)

for c in range(0,len(colours)):
    x, y = weq(gammalist[c],200,1000)
    col = colours[c]
    accol = actcolours[c]
    plt.plot(x,y,col,label=str(gammalist[c]),markersize = 1.5)
    plt.legend(loc="upper right", title="Gamma")
plt.show()

#think it depends on how well gamma is approximated by a fraction with
#a (possibly low) denominator
