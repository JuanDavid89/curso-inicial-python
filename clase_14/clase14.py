# CRUD

import sqlite3

conexion = sqlite3.connect("instituto.db")
cursor = conexion.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS alumnos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL,
                   edad INTEGER NOT NULL,
                   curso TEXT NOT NULL
               )
               ''')

conexion.commit()

def agregar_alumno(nombre, edad, curso):
    cursor.execute(" INSERT INTO alumnos (nombre, edad, curso) VALUES (?, ?, ?)" , (nombre, edad, curso))
    conexion.commit()
    print("El alumno/a fue agregado exitosamente.")
    
def mostrar_alumnos():
    cursor.execute("SELECT * FROM alumnos")
    alumnos = cursor.fetchall()
    print("\nLista de Alumnos\n")
    
    for alumno in alumnos:
        print(f"ID: {alumno[0]}, Nombre: {alumno[1]}, Edad: {alumno[2]}, Curso: {alumno[3]}")

while True:
    print("\n================ Gestión de Alumnos ==========================")
    print("1. Agregar alumno")
    print("2. Mostrar alumno")
    print("3. Actualizar curso de alumno")
    print("4. Eliminar alumno")
    print("5. Salir")
    print("============================================================")

    opcion = input("Seleccione una opción entre 1 y 5: ").strip()

    # Validación: debe ser un número del 1 al 5
    if not opcion.isdigit():
        print("Debe ingresar solo números.")
        continue

    opcion = int(opcion)

    if opcion == 1:
        nombre = input("Ingrese el nombre del alumno: ").strip()
        edad = input("Ingrese la edad del alumno: ").strip()
        curso = input("Ingrese el curso del alumno: ").strip()
        
        if edad.isdigit():
            agregar_alumno(nombre, int(edad), curso)
        else:
            print("La edad debe ser un número válido.")
            
    elif opcion == 2:
        mostrar_alumnos()
        
            
    '''elif opcion == 3:
        buscar = input("Ingrese el nombre del producto a buscar: ").strip().lower()
        encontrados = 0
        for producto in productos:
            if buscar == producto[0].lower():
                print("Producto encontrado:")
                print(f"- Nombre: {producto[0]}")
                print(f"- Categoría: {producto[1]}")
                print(f"- Precio: ${producto[2]}")
                encontrados += 1
        if encontrados == 0:
            print("Producto no encontrado.")

    elif opcion == 4:
        eliminar = input("Ingrese el nombre exacto del producto a eliminar: ").strip().lower()
        eliminado = False
        for producto in productos:
            if eliminar == producto[0].lower():
                productos.remove(producto)
                print("Producto eliminado con éxito.")
                eliminado = True
                break
        if not eliminado:
            print("Producto no encontrado.")

    elif opcion == 5:
        if len(productos) > 0:
            print("\n=================== Productos ingresados ===================")
            contador = 1
            for producto in productos:
                print(f"{contador}. Nombre: {producto[0]} | Categoría: {producto[1]} | Precio: ${producto[2]}")
                contador += 1
            print("============================================================\n")
        else:
            print("No se ingresaron productos.")
            print("============================================================\n")

        print("                   Fin del programa...")
        print("\n============================================================\n")
        break

    else:
        print("Opción fuera de rango (1-5). Intente nuevamente.")

print("============================================================")
print("              Desarrollado por: Juan Saavedra            ")
print("============================================================\n")'''

conexion.close()

