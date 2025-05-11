# Bucles - For

'''print("\n========| Lista de nombres |=========\n")
lista = ['Laura', 'Pedro', 'Javier', 'Tamara', 'Claudio']

for nombre in lista:
    print(f"Hola, {nombre}")

print("\n========| Lista de frutas |=========\n")
frutas = ["Manzana", "Cambur", "Cereza", "Frambuesa"]

for fruta in frutas:
    print(f"Fruta:, {fruta}")

print("\n========| Fin de las listas |========\n")'''

# Recorriendo lista de clientes

'''print("\n=======| Lista de clientes |========\n")

clientes = ["Juan", "maria", "", "PEDRO", "LuIsA", "ANA"]

for cliente in clientes:
    print("Cliente:", cliente)
    print("Cliente:", cliente, end=" ") # el end imprime en la misma linea'''

# recorriendo lista de productos

productos = ["P001", "P002", "P003", "P004", "P005"]

producto_a_buscar = input("\nIngrese el código del producto a buscar: ")

for producto in productos:
    print(f"Buscando...")
    if producto == producto_a_buscar:
        print(f"\tEl producto: {producto} fue encontrado.")
        break

if producto != producto_a_buscar:
    print(f"\nEl producto: {producto_a_buscar} no fue encontrado.")

print("\n======== Fin de la búsqueda ========")