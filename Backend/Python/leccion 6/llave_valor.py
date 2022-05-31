#def listarTerminos(**terminos):
#    for llave , valor in terminos.items():
#        print(f'{llave}: {valor}')


#listarTerminos(Youtube='Reproduccion de videos', Google='buscador')


def casa(**termino):
    for nombre , valor in termino.items():
        print(f'{nombre}: {valor}')

casa(Palacio_Angulo='200')

def suma(*tupla):
    resultado = 1
    for i in tupla:
        resultado =+ i
    return resultado
print(f'El resultado de su suma es: {suma(2,2)}')
