# Función Range, crea una secuencia que no esta almacenada en memoria



'''for i in range(5):
    print(i)'''

'''for i in range(2,10,2):
    print(i)'''

'''lista = ["Laura", "Pedro", "Javier", "Tamara"]

for i in range(len(lista)):
    print(f"El nombre almacenado en la posición {i} es {lista[i]}")'''

'''frutas = ["manzana", "cambur", "fresa", "naranja", "melon"]

for i in range(len(frutas)):
    print(f"Fruta {i + 1}: {frutas[i]}")'''

'''colores = ["amarillo", "azul", "verde", "morado", "blanco", "negro", "marron", "rosado", "naranja"]

for i in range(0, len(colores), 3):
    color = colores[i]
    print(f"Color en el indica {i}: {color}")'''

'''dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
venta_por_dias = [30, 50, 40, 20, 18]

for i in range(len(dias)):
    print(f"El {dias[i]} vendió: {venta_por_dias[i]}")'''

# agregar un elemento nuevo a una lista

'''dias = ["Lunes", "Martes"]

dias.append("Miércoles")

print(dias)'''

# remover un elemento de la lista

'''dias = ["Lunes", "Martes"]

dias.remove("Martes")

print(dias)'''

# Insertar un elemento en la posición deseada

'''dias = ["Lunes", "Miércoles"]

dias.insert(1, "Martes")

print(dias)'''

mascotas = []

print("\n==================================================")
print(" Lista de Mascotas | Escriba 'fin' para terminar.")
print("==================================================")

while True:
    nombre_mascota = input("Ingrese el nombre de una mascota: ")

    if nombre_mascota.lower() == 'fin':
        break

    mascotas.append(nombre_mascota)
print("==================================================\n")

print("==================================================")
print(" Listado de mascotas:")
print("==================================================")
for mascota in mascotas:
    print(f"- {mascota}")

print("==================================================\n")