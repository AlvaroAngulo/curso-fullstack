#Definir una lista de tipo str
nombres = ["Juan", "Karla", "Maria", "Camilo"]
print(nombres)                #se imprime la lista

# acceder a los elementos de una lista
print(nombres[0])

#acceder a los elementos de una lista de manera inversa
print(nombres[-1])
print(nombres[-2])
#imprir un rango

print(nombres[0:2])#sin incluir el indice 2

#ir del inicio de la lista al indice sin incluirla 
print(nombres[:3])

#desde el indice indicado hata el final 
print(nombres[1:])

#cambios un valor 
nombres[3] = 'Fernando'
print(nombres)

#iterar una lista
for i in nombres:
    print(i)
else:
    print("No existen mas nombres ")
    
#preguntar el largo de una lista
print(len(nombres))

#agregar un elemento
nombres.append("Shary")
print(nombres)

#insertar un elemento en un indice en especifico
nombres.insert(1,'Elkin')
print(nombres)

# remover un elemento
nombres.remove('Elkin')
print(nombres)

#remover el ultimo valor agregado
nombres.pop()
print(nombres)

#eliminar un indice
del nombres[0]
print(nombres)

#limpiar la lista
nombres.clear()
print(nombres)

#borrar la lista por completo
del nombres
print(nombres)