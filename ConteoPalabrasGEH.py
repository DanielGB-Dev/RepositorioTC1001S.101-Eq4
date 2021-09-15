import matplotlib.pyplot as plt
import numpy as np




palabras=[]

with open("GEH.txt") as texto:
    for lineas in texto:
        lineas=lineas.lower()
        palabras.extend(lineas.split())



palabrasunicas=[]

repeticiones=[]

for i in palabras:
    if not i in palabrasunicas:
        palabrasunicas.append(i)

for i in palabrasunicas:
    repeticiones.append(palabras.count(i))
        
print(repeticiones)
print(palabrasunicas)

print(len(palabrasunicas))



