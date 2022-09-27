
import random
import numpy as np


# Aufgabe 1
def Lotto():
    numb = []
    f= 44

    for i in range(0,45):
        numb.append(i)



    for j in range(0, 45):
        a = random.randrange(0, 45, 1)
        y = numb[a]
        z = numb[f]
        numb[f] =y
        numb[a] = z
        f = f - 1


    for k in range(0,45):
        print(numb[k])




#Aufgabe 2
def Lotto_Warscheinlichkeit():
    dictio = {}

    for i in range (0,45):
        dictio[i] =0


    for j in range (0,1000):
        a = random.randrange(0, 45, 1)
        dictio[a] +=1

    for k in range(0, 45):
        print(k ,':' ,dictio[k], 'mal')