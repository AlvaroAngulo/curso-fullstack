"""
Ejercicio: Convertidor de temperatura
Realizar dos funciones para conventir de grados celcius a fahrenheit y viciversa

Fahrenheit a celcius
#Ejemplo: (75F - 32) x 0.5556 = 23.6C

Celcius a Fahrenheit 
#Ejemplo: (50C x 1.8) + 32 = 122F

"""

def convertidor(fahrenheit):
     return (fahrenheit - 32) * 0.5556 

fahrenheit = float(input("Ingrese la temperatura en fahrenheit: "))
i = convertidor(fahrenheit)
print(f"La temperatura es: {i:.2f}")

def convertidor(celcius ):
    return (celcius * 1.8) + 32
    

celcius = float(input("Ingrese la temperatura en celcius: "))
resultadoc = convertidor(celcius)
print(f"La temperatura es: {resultadoc:.2f}")


