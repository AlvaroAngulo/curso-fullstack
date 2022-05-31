"""
Imprimir numero de 5 a 1 de manera descenndente usando funciones recursivas.
puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5 , debe imprimir:

5
4
3
2
1

En caso de pasar el  valor  de  3, debe imprimir
3
2
1

Si se pasan valores negativos no imprime nada 

"""
def decendiente(numero):
    if numero < 0:
        return 
    if numero > 0:
        print(numero)
        numero -= 1
        decendiente(numero)
    
decendiente(-3)
