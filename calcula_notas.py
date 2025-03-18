#Calcular el valor de la nota final

# Solicitamos por el usuario el ingreso de las notas
nota_uno = float(input('Ingrese la priemra nota: '))
nota_dos = float(input('Ingrese la segunda nota: '))
nota_tres =float(input('Ingrese la tercera nota: '))


# Definimos la función que realiza el calculo de la notafinal
def calcular_nota (nota_uno, nota_dos , nota_tres):
    # toma las notas ingresadas por el usuario, le calcula el porcentaje para cada nota y las suma
    return (nota_uno*0.3) + (nota_dos*0.3) + (nota_tres*0.4)



nota_final = calcular_nota(nota_uno, nota_dos, nota_tres)
nota_final = round(nota_final,1)

print(f"La nota final es: {nota_final}")


