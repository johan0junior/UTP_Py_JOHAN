#generamos la lista de 10 aleatorios
import random as rd
lisT = []
for i in range(10):
    num = rd.randint(1, 10)
    lisT.append(num)
print("Lista original:",lisT)
#realizamos el bucle
for i in range(len(lisT)):
  for j in range(len(lisT)-1):
    if lisT[j] > lisT[j+1]:
       #entonces realizamos el cambio
       lisT[j], lisT[j+1] = lisT[j+1], lisT[j]