#!/usr/bin/env python3
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import pylab

with open ("earthquakes.dat", "r") as F:
    lines=F.readlines()

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
        #print(fecha)
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
            #print(anio)
            anio+=1
            if float(b) >= umbral:
                count6=1
            else:
            	count6=0
risks=[]
for i in range(len(magnitudes6)):
	p=magnitudes6[i]/magnitudes[i]
	#print("La probabilidad de que ocurra:")
	#print(p)
	#print("La probabilidadde que no ocurra:")
	pno=1-p
	#print(pno)
	#print("No ocurra en el proximo año:")
	noc2=(pno)
	#print(noc2)
	#print("Riesgo de ocurrencia de sismos mayores a",umbral,":")
	#print(1-noc2)
	risk=1-noc2
	risks.append(risk)
#print(len(risks))
#print(len(anios))
def histogramas(x,y):
	z=np.polyfit(x,y,1)
	p = np.poly1d(z)
	tendencia = p(x)
	z2=np.polyfit(x,y,3)
	p2 = np.poly1d(z2)
	tendencia2 = p2(x)
	fig, ax = plt.subplots()
	ax.plot(x,y,".", label='Riesgo de ocurrencia')
	ax.plot(x,tendencia, label='Tendencia lineal')
	ax.plot(x,tendencia2, label='Tendencia cuadratica')
	fig.suptitle('Riesgos de ocurrencia')
	pylab.legend(loc='upper left')
	plt.show()


histogramas(anios, risks)