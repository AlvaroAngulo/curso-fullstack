
#def sumar(*args):
#    total = 0
#    for i in args:
#        total +=  i
#    return total

#print(f"Resultado suma: {sumar(3, 4, 3)}") 

# segundo ejercicio 

def multi(*tupla):
    re = 1
    for p in tupla:
        re = re * p
    return re
print(f'Resultado de la multiplicacion es: {multi(2, 2)}')
