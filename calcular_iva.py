# calcular el IVA y valor de la compra con el impuesto

# Solicitamos ingreso del usuario el valor de la compra
valor_compra = round(float(input('Ingrese el valor total de la compra: ')),0)

# calculamos el calor del IVA
def calcula_iva(valor_compra):
    # IVA es igual al el valor de la compra por el 19%
    iva = valor_compra * 0.19
    return iva

iva= round(calcula_iva(valor_compra),0)
neto_pagar = round(valor_compra+iva,0)

print(f"Su compra es de: {valor_compra} \nmas IVA de: {iva} \ntotal a pagar: {neto_pagar}")
