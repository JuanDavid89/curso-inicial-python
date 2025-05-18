# Bucles - while/for

'''nombre = ""

while nombre == "":
    nombre = input("Ingrese su sombre")
    if nombre == "":
        print("El nombre no puede estar vacío.")

print(f"\nHola, {nombre}\n")'''

'''contador = 1

while contador <= 5:
    print(f"Este es el intento número {contador}.")
    contador += 1

print("Bucle terminado.")'''

'''suma = 0    # acumulador
indice = 1  # contador

while indice <= 2:
    print(f"Soy la repetición {indice}")

    suma += int(input("Ingresa un valor númerico para sumar: "))

    indice += 1 #incrementador

print(f"\nLa suma de los valores ingresados es: {suma}\n")'''

# ======| Tabla del 2 |======

'''print("\n======| Tabla del 3 |======")

x = 0
while x <= 10:
    print(f"3 x {x} = {3 * x}")
    x +=1

print("===========================\n")'''

# Ejercicio práctico 1

'''intentos = 0
max_intentos = 3

while intentos < max_intentos:
    nombre = input("Ingrese su nombre de usuario: ").strip()

    if nombre != "":
        print(f"Bienvenido/a, {nombre}!")
        break
    else:
        print("El nombre no puede estar vacío. Intentá de nuevo")

    intentos += 1

if intentos == max_intentos:
    print("Se agotaron los intentos. Intenta más tarde")'''

# Ejercicio práctico 2
# Usamos un bucle while que se ejecuta hasta que el usuario ingrese 0

# Numero declarandolo dentro del while funciona
# numero = 0
'''suma = 0

while True:
    numero = int(input("Ingresa un número: "))
    if numero < 0:
        print("El número es negativo, intenta de nuevo.")
        continue # Saltamos el resto del código en esta iteración

    if numero == 0:
        break
    
    # Sumamos el número positivo total
    suma += numero

# Mostramos el resultado final
print(f"\nLa suma de los números positivos es: {suma}\n")'''

# Ejercicio maquina expendedora
print("\n==== Maquina Expendedora de Bebidas ====")

while True:
    print("\n================")
    print("Opciones:")
    print("================")
    print("1. Café")
    print("2. Té")
    print("3. Matecocido")
    print("4. Chocolate")
    print("================")
    print("5. Salir")
    print("================")

    opcion_str = input(f"\nIngresa el número de la opción deseada: ")

    if not opcion_str.isdigit():
        print("\nDebe ingresar solo caracteres numéricos.")
        continue

    try:
        opcion = int(opcion_str)

        if opcion <= 0 or opcion > 5:
            print("Número invalido, vuelva a intentarlo.")
            continue

        if opcion == 1:
            print("\nPreparando Café\n")
            break
        elif opcion == 2:
            print("\nPreparando Té")
            break
        elif opcion == 3:
            print("\nPreparando Matecocido")
            break
        elif opcion == 4:
            print("\nPreparando Chocolate")
            break
        elif opcion == 5:
            print("\nHasta luego")
            break

    except ValueError:
        print("\nOcurrió un error al convertir el número. Intente nuevamente.")
        
print("\n================")
print("¡Finalizado!")
print("================")

# Listas

'''numero = [3, "Hola", 6, 7, True]

nombre = ["Juan", "David"]

print(nombre[0])'''