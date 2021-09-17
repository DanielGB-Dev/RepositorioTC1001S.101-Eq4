import matplotlib.pyplot as plt
import numpy as np
# Run in terminal.
# py -m pip install matplotlib 

""" 
palabras is an array that will contain the GEH.txt file separed word by word
palabrasunicas is an array that will contain the unique words found in the GEH.txt file with no repetitions
repeticiones is an array that will contain the numer of repetitions of every unique word in the GEH.txt file    
"""
palabras=[]
palabrasunicas=[]
repeticiones=[]

"""Open the GEH.txt file"""
with open("GEH.txt") as texto: # Add your local path
    """Use for to get every line of the text"""
    for lineas in texto:
        """Transform every upper into lower in order to standardize words"""
        lineas=lineas.lower()
        """Append to palabras every line splited by single words"""
        palabras.extend(lineas.split())
        
"""
At this moment palabras contains the GEH.txt file
separed word by word

Append every unique word without repeating to palabrasunicas"""
for i in palabras:
    """If word in palabras is not found in palabras unicas, apped word to palabrasunicas"""
    if not i in palabrasunicas:
        palabrasunicas.append(i)

"""
At this moment palabrasunicas contains every unique word without repetitions
len(palabrasunicas) gives us the numer of unique words founded in GEH.txt file

Count number of repetitions of every unique word in GEH.txt file"""
for i in palabrasunicas:
    """Store the number of repetitions of each word in repeticiones"""
    repeticiones.append(palabras.count(i))

"""Print every array with the information"""
print("Numero de palabras sin repetirse: " + str(len(palabrasunicas)))
print("Palabras unicas encontradas \n" + str(palabrasunicas))
print("Numero de repeticiones de cada plabra \n" + str(repeticiones))

"""
Create a figure with 10 subplots
Every subplot contains five unique words with the number of repetitions in the GEH.txt file
"""
fig, ax = plt.subplots(2,5,figsize=[14,5])
fig.suptitle("Veces que se repite cada palabra en el cuento GEH")
ax[0,0].hist(palabrasunicas[0:6],weights=repeticiones[0:6], width=0.3)
ax[0,1].hist(palabrasunicas[6:11],weights=repeticiones[6:11], width=0.3)
ax[0,2].hist(palabrasunicas[11:16],weights=repeticiones[11:16], width=0.3)
ax[0,3].hist(palabrasunicas[16:21],weights=repeticiones[16:21], width=0.3)
ax[0,4].hist(palabrasunicas[21:26],weights=repeticiones[21:26], width=0.3)
ax[1,0].hist(palabrasunicas[26:31],weights=repeticiones[26:31], width=0.3)
ax[1,1].hist(palabrasunicas[31:36],weights=repeticiones[31:36], width=0.3)
ax[1,2].hist(palabrasunicas[36:41],weights=repeticiones[36:41], width=0.3)
ax[1,3].hist(palabrasunicas[41:46],weights=repeticiones[41:46], width=0.3)
ax[1,4].hist(palabrasunicas[46:51],weights=repeticiones[46:51], width=0.3)
plt.show()
