#!/usr/bin/env python3
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import pylab

with open ("data2.dat", "r") as F:
    lines=F.readlines()

#print(len(lines))
depth=[]
magnitude=[]
#print(len(lines))
for dat in lines[1:]:
    #print(dat)
    a,b,c=dat.split()
    if "MW" in c:
        depth.append(float(a))
        magnitude.append(float(b))
print(len(magnitude))

#fig, ax = plt.subplots()
#plt.hist(magnitude, bins='auto')
#ax.set(xlabel='magnitude', ylabel='count',
#      title='Histograma de magnitudes')
#fig.savefig("syntetic.png")
def histogramas(magnitude):
	fig, ax = plt.subplots()
	ax.hist(magnitude, bins=20)
	fig.suptitle('Histograma de magnitud en MW')
	#pylab.legend(loc='upper left')
	plt.show()


histogramas(magnitude)
