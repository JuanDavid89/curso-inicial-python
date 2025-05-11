#Operadores de relación o comparación
'''
== Igual que
!= Distinto que
< Menor que
> Mayor que
<= Menor o igual que
>= Mayor o igual que
print(3 >= 3)
'''

#Operadores lógicos

'''
and --> Y
or  --> O
not --> No
print(not 3 > 3 and 4 == 4)
'''

#Condicionales

'''
numero = int(input("Ingrese un número: "))

if numero > 0:

    print("El número es positivo")
else:
    print("El número es negativo")
'''
claveAlmacenada = "MiClave123"
claveIngresada = input("\n Ingrese su clave: ")

if claveAlmacenada == claveIngresada:
    print("\nClave correcta")
else:
    print("\nClave incorrecta")