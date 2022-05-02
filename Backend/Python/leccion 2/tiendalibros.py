from xmlrpc.client import boolean


print(
    "TIENDA DE LIBROS!"
)

nombre = input("Proporciona el nombre: ")
id = int(input("Proporciona el ID: "))
precio = float(input("Proporcione el precio: "))
envio = input("Indica si el envio es gratuito(True/False): " )

if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = 'Valor incorrecto, debe escribir True/False'
    
print(f'''
      Nombre: {nombre}
      precio: {precio}
      Envio Gratuito?: {envio}
''')
