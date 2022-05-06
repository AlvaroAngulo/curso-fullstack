# dict (key, value)

diccionario = {
    "nombre": "Juan",
    "edad": 20,
    "ciudad": "Madrid"
}

print(diccionario)

# largo del diccionario

print(len(diccionario))

# aceder a un elemento (key)
print(diccionario["nombre"])

#otra forma de acceder a un elemento
print(diccionario.get("nombre"))

# modificar un elemento
diccionario["nombre"] = "Juanito"
print(diccionario)

# recorrer un diccionario
for key, value in diccionario.items():
    print(key, value)

for key in diccionario.keys():
    print(key)

for value in diccionario.values():
    print(value)

# comprobar si un elemento esta en el diccionario  
print("nombre" in diccionario)

# agregar un elemento al diccionario
diccionario["apellido"] = "Perez"
print(diccionario)

# remover un elemento del diccionario
diccionario.pop("apellido")
print(diccionario)

# limpiar el diccionario
diccionario.clear()
print(diccionario)

# eliminar el diccionario
del diccionario
print(diccionario)
