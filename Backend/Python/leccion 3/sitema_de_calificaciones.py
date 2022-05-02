valor = int(input("Proporcione un valor entre (0 y 10): "))
i = None

if valor >=  9 and valor <= 10:
    i = 'A'
elif valor >=  8 and valor < 9:
    i = 'B'
elif valor >=  7 and valor < 8:
    i = 'C'
elif valor >=  6 and valor < 7:
    i = 'D'
elif valor >=  0 and valor < 6:
    i = 'F'
else:
    print("VALOR INCORRECTO!! ")
    
print(f"Su calificacion es: {i}")