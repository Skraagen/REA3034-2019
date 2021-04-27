# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:52:34 2019

@author: mathi
"""

import numpy as np
import matplotlib.pyplot as plt

N = 100         #Antall tidssteg
a = 0.0             #Start på intervallet
b = 100.0           #Slutt på intervallet
y0 = 20          #Initialverdi koi
r0 = 1            #Initialverdi innhøstning
k = 0.06            #Reproduksjonsrate
B = 100             #Bæreevne koi

#Initialiserer
h = (b-a)/(N-1)     #Steglengde
t = np.linspace(a,b,N)
#Fyller matrise med tomme punkter for senere innfylling
K = np.zeros(N) # koipopulasjon
M = np.zeros(N) # innhøstet masse
R = np.zeros(N)
#Setter startpunkter
K[0] = y0 
M[0] = 0
R[0] = r0

Kder = np.zeros(N-1)
Rder = np.zeros(N-1)
v = 0 # vendepunkt

#Velge innhøstningsmetode
valg_inn = input("Velg mellom variabel eller konstant innhøstning: ")

#Velge mengde og intervall på konstant innhøstning
if valg_inn == "konstant":
        valg_konst = input("Velg konstant innhøstning (kg): ")
        valg_int = input("Velg intervall på konstant innhøstning: ")

#Looper gjennom tidsstegene og fyller matrisene
for i in range(N-1) :   
    
    #Passer på at graf for innhøsting stiger kontinuerlig
    M[i+1] = M[i]
    
    Kder[i] = k*K[i]*(1-K[i]/B) #Formel for logistisk vekstkurve for koipopulasjon
    
    if valg_inn == "variabel":
        if Kder[i-2] < Kder[i-1] and Kder[i] < Kder[i-1]: #Finne maks stigning på koipopulasjon
            K[i]*=0.7 #Fjerner andel av koipopulasjon
            M[i+1] = M[i] + K[i-1]-K[i] #Legger til endring av koipopulasjon til total biomasse
            
    elif valg_inn == "konstant":
        # Velge konstant innhøstning (kg)
        if i % int(valg_int) == 0: #Kjører når i stemmer for valgt intervall
            K[i] -= int(valg_konst) #Fjerner konstant masse fra koipopulasjon
            M[i+1] = M[i] + K[i-1]-K[i] #Legger til endringen i total biomasse
    
    K[i+1] = K[i] + Kder[i]*h #Eulers metode, tilnærmeing ved hjelp av tangenter
    
    Rder[i] = (K[i]/200)*R[i]*(1-R[i]/K[i]*0.05) #Logistisk vekstkurve avhengig av koipopulasjonen
    
    if R[i] >= 20: #Høster inn ruccola dersom total bestand er lik 20 kg
        R[i] = 0
    
    R[i+1] = R[i] + Rder[i]*h #Eulers metode for ruccolagraf

#Plotting
fig = plt.figure()
axK = fig.add_subplot(111)
dataK = axK.plot(t, K, '-b', label='Koi')
dataM = axK.plot(t, M, '-c', label='Innhøstet koi')
dataR = axK.plot(t, R, '-g', label='Ruccola')

#Key
data = dataK + dataM + dataR
datatittel = [l.get_label() for l in data]
axK.legend(data, datatittel, loc=0)

#Koordinatsystem
axK.grid()
axK.set_xlabel('Tid i måneder')
axK.set_ylabel('Masse (kg)')
axK.set_ylim(0, 150)
axK.set_ylim(0, 150)
axK.set_ylim(0, 150)
plt.show()

#Total innhøstet biomasse på slutten av perioden
print("Total innhøstet biomasse", max(M))