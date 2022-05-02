a = int(input("Ingrese un numero: "))

numerotext = ''

if a == 1:
    numerotext = 'NUMERO 1'
elif a == 2:
    numerotext = 'NUMERO 2'
elif a == 3:
    numerotext = 'NUMERO 3'
else:
    numerotext = 'FUERA DE RANGO'
    
print(f"Numero proporcionado: {a}: {numerotext}")