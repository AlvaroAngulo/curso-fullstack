
def mayor(a, b):
    if a > b:
        print(f'El mayor es: {a} ')
    else:
        print(f'El mayor es: {b} ')

mayor(2, 4)

# otro ejemplo
def suma (c , d):
    return c + d
resultado = suma(5,3)
print(f'Resultado suma: {resultado}')

# valores por default

def resta (i = 3, p = 2 ):
    return i - p
print(f"Resultado resta: {resta(5, 4)}")

