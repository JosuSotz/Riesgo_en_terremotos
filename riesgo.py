#!/usr/bin/env python3
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import pylab

with open ("earthquakes.dat", "r") as F:
    lines=F.readlines()

def tendency(x,y):
	z=np.polyfit(x,y,1)
	p = np.poly1d(z)
	tendencia = p(x)
	z2=np.polyfit(x,y,3)
	p2 = np.poly1d(z2)
	tendencia2 = p2(x)
	fig, ax = plt.subplots()
	ax.plot(x,y,".", label='Riesgo de ocurrencia')
	ax.plot(x,tendencia, label='Tendencia lineal')
	ax.plot(x,tendencia2, label='Tendencia cúbica')
	fig.suptitle('Riesgos de ocurrencia')
	pylab.legend(loc='upper left')
	fig.savefig("riesgo.png")
	plt.show()
def calculate_risk(total_earthquakes, earthquakesup6_5,n):
	p=earthquakesup6_5/total_earthquakes
	p_no=1-p
	no_occ= p_no**n
	risk=1-no_occ
	return risk

date=[]
magnitude=[]
umbral=6.5
anio=1984
anios=[]
count=0
count6=0
magnitudes=[]
magnitudes6=[]
for dat in lines[1:]:
    a,b,c=dat.split()
    fecha = int(a[6:])
    if "MW" in c:
        date.append(fecha)
        magnitude.append(float(b))
        if anio == fecha:
            count+=1
            if float(b) >= umbral:
            	count6+=1
        else:
            magnitudes.append(count)
            magnitudes6.append(count6)
            anios.append(anio+1)
            count=1
            anio+=1
            if float(b) >= umbral:
                count6=1
            else:
            	count6=0
risks=[]
for i in range(len(magnitudes6)):
	risk=calculate_risk(magnitudes[i],magnitudes6[i],1)
	risks.append(risk)

print("El riesgo de ocurrencia de un sismo de magnitud 6.5 o mayor en un periodo de 10 años en todo el mundo es:",calculate_risk(magnitudes[-1],magnitudes6[-1],10))
tendency(anios, risks)
