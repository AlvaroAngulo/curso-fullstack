#definir una tupla

frutas = ('Naranja', 'Platano', 'Mango')

print(frutas)
#largo de la tupla

print(len(frutas))

#acceder a un elemento

print(frutas[0])

# navegacion inversa
print(frutas[-1])

#acceder a un rango

print(frutas[0:1])# sin incluir el ultimo indice


for i in frutas:
    print(frutas, end=' ' )

# cambiar valor de una tupla...  (no se puede)
#frutas[0] = 'Úva'

frutaslista = list(frutas)
frutaslista[0] = 'Uva'
frutas = tuple(frutaslista)
print(frutas)

#eliminar tupla

del frutas
print(frutas)