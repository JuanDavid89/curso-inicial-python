# Ejercicio práctico clase 7

'''
En TalentoLab necesitamos llevar un registro ordenado de los nombres de clientes y clientas  que se van incorporando.Tu tarea es escribir un programa en Python que haga lo siguiente:

Solicite los nombres de los y las clientes uno por uno y valide que cada nombre no esté vacío. Si se deja el campo vacío, mostrar un mensaje de advertencia y volver a pedir el nombre.

Guarde cada nombre válido en una lista, asegurándote de agregarlo con el método .append(). 

Permití que se finalice la carga de nombres escribiendo la palabra "fin". 

Una vez finalizada la carga, ordená alfabéticamente los nombres en la lista y mostrá la lista ordenada utilizando un bucle for.

Saludos, Mariana.
'''

print("\n========  |Registro ordenado de clientes|  ========")
print("========   Ingresar 'Fin' para finalizar   ========")

clientes = []

print("\n===================================================")
print("=======   Nombres de clientes ingresados    =======")
print("===================================================")

while True:
    nombre = input("Ingrese el nombre del cliente: ").strip()

    if not nombre:
        print("El nombre no puede estar vacío. Intente nuevamente.")
        continue

    if nombre.lower() == "fin":
        break

    clientes.append(nombre)

print("===================================================\n")

print("===================================================")
print("========    Lista ordenada de Clientes     ========")
print("===================================================")
for cliente in clientes:
    print(f"- {cliente}")
print("===================================================")


print("\n========  |Final de la lista de clientes|  ========\n")
