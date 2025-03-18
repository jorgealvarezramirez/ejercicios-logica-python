# Crear tabla de multiplicar

n = int(input("Ingrese un numero entero: "))

# Se crea la función que presente los valores concatenados igual que una tabla de multiplicar tradiconal, se maneja como string
def tabla_multiplicar(n1,n2):
    return str(n1) + " * " +str(n2) + " = " + str(n1*n2)

# Calcular el valor por cada numero del 1 al 12
for i in range(0,13):
    print(tabla_multiplicar(n, i))
