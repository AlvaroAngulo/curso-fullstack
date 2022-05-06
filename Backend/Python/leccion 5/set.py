# set
from traceback import print_tb


planetas = {'Marte', 'Pluton', 'Venus' }

print(planetas) # los set no se impren en orden

#largo 
print(len(planetas))

#revisar si un elemento esta en el set

print('Venus' in planetas) # True
print('Jupiter' in planetas) # False

#agregar un elemento al set
planetas.add('Jupiter')
print(planetas)

#no se pueden duplicar elementos
planetas.add('Jupiter')
print(planetas)

#eliminar un elemento del set
planetas.remove('Jupiter')
print(planetas)

# elimunar un elemento sin arrojar no error
planetas.discard('Jupiter')
print(planetas)

# limpiar el set
planetas.clear()
print(planetas)

# eliminiar el set
del planetas
print(planetas)