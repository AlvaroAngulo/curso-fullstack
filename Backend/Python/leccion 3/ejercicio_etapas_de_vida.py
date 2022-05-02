edad = int(input("Proporciona tu edad: "))

a = None

if edad >= 0 and edad <= 10:
    a = 'La infancia es increible...'
elif edad >= 10 and edad < 20:
    a = 'Muchos cambios y mucho estudio...'
elif edad >= 20 and edad <= 30:
    a = 'Amor y comienza el trabajo... '
else:
    print('Etapa de vidad no reconocidad')

print(f"Grandioso, {a}")
    
    
