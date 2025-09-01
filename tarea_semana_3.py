#generamos la lista de 10 aleatorios
import random as rd
lisT = []
for i in range(10):
    num = rd.randint(1, 10)
    lisT.append(num)
print("Lista original:",lisT)
#realizamos el bucle para ordenar la lista de forma ascendente
for i in range(len(lisT)):
  for j in range(len(lisT)-1):
    if lisT[j] > lisT[j+1]:
       #entonces realizamos el cambio
       lisT[j], lisT[j+1] = lisT[j+1], lisT[j]
#ordenamos la lista de forma descedente
lista_des = lisT.copy()
#copiamos la lista original para no modificarla 
for i in range(len(lista_des)):
    #usamos el "len" para obtener el tamaño de la lista
   for j in range(len(lista_des)-1):
     #usamos el rango de esta manera porque si dejamos solo el "len" el ultimo elemento no se compara
     if lista_des[j] < lista_des[j+1]:
        #comparamos y intercambiamos
        lista_des[j], lista_des[j+1] = lista_des[j+1], lista_des[j]

print("lista Ascendente:", lisT)
print("lista Descendente:", lista_des)