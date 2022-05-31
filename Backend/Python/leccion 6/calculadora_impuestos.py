"""
Ejercicio: calculadora de impuestos
Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado.
#Formula: pago_total = pago_sin_impuesto * pago_sin_impuesto * (impuesto/100)
"""
pago = float(input("Ingrese el pago sin impuesto: "))
impuesto = int(input("Ingrese el monto del impuesto: "))

def caluladora(impuesto,pago):
    pago_total = pago + pago * (impuesto/100)
    print(f'pago con impuesto: {pago_total}')
caluladora(impuesto,pago)
