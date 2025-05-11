'''texto = "  Python  "
print(texto.strip().upper())'''

# Ejemplo de match
'''fruta = input("\nIngresa una fruta: ")

match fruta:
    case "manzana": 
        print("\nEs una fruta roja o verde. \n")
    case "cambur":
        print("\nEs una fruta amarilla. \n")
    case "naranja": 
        print("\nEs una fruta anaranjada. \n")
    case _:
        print("\nNo tengo información acerca de esta fruta. \n") '''

 # Días de la semana con if - elif - else   
'''print("\n======Días de la semana======")

dia = input("\nIngresa el número de un día de la semana: ")

if dia == "1":
    print("\nLunes")
elif dia == "2":
    print("\nMartes")
elif dia == "3":
    print("\nMiércoles")
elif dia == "4":
    print("\nJueves")
elif dia == "5":
    print("\nViernes")
elif dia == "6":
    print("\nSábado")
elif dia == "7":
    print("\nDomingo")
else:
    print("\nNo es un día de semana")

print("\n====== Fin del programa ======\n")'''

# Días de la semana con match
'''print("\n======Días de la semana======")

dia = input("\nIngresa el número de un día de la semana: ")

match dia:
    case "1":
        print("\nLunes")
    case  "2":
        print("\nMartes")
    case "3":
        print("\nMiércoles")
    case "4":
        print("\nJueves")
    case "5":
        print("\nViernes")
    case "6":
        print("\nSábado")
    case "7":
        print("\nDomingo")
    case _:
        print("\nNo es un día de semana")


print("\n====== Fin del programa ======\n")'''

# Programa para clasificar paquetes por peso
'''print("\n====== Clasificación de paquetes ======")

paquete = input("\nIngresa el nombre del paquete: ")

peso_paquete = int(input("\nIngresa el peso del paquete: "))

if peso_paquete >= 0 and peso_paquete <= 5:
    print("\nNombre:", paquete)
    print("\nPeso:", peso_paquete, "Kg")
    print("\nClasificación: Paquete pequeño.")
elif peso_paquete > 5 and peso_paquete <= 20:
    print("\nNombre:", paquete)
    print("\nPeso:", peso_paquete, "Kg")
    print("\nClasificación: Paquete mediano.")
elif peso_paquete > 20:
    print("\nNombre:", paquete)
    print("\nPeso:", peso_paquete, "Kg")
    print("\nClasificación: Paquete grande.")
else:
    print("\nPeso invalido")

print("\n====== Fin del programa ======\n")'''

# Mismo programa con match
'''print("\n====== Clasificación de paquetes ======")

paquete = input("\nIngresa el nombre del paquete: ")

try:
    peso_paquete = int(input("\nIngresa el peso del paquete: "))
except ValueError:
    print("\nPeso inválido. Debe ser un número entero.")
    exit()

match peso_paquete:
    case p if 0 <= p <= 5:
        print("\nNombre:", paquete)
        print("\nPeso:", peso_paquete, "Kg")
        print("\nClasificación: Paquete pequeño.")
    case p if 6 <= p <= 20:
        print("\nNombre:", paquete)
        print("\nPeso:", peso_paquete, "Kg")
        print("\nClasificación: Paquete mediano.")
    case p if p > 20:
        print("\nNombre:", paquete)
        print("\nPeso:", peso_paquete, "Kg")
        print("\nClasificación: Paquete grande.")
    case _:
        print("\nPeso invalido, no se permiten números negativos")

print("\n====== Fin del programa ======\n")'''

# Manipulación de caracteres o cadenas