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
        
def actualizar_curso(id_alumno, nuevo_curso):
    cursor.execute("UPDATE alumnos SET curso = ? WHERE id = ?", (nuevo_curso, id_alumno))
    conexion.commit()
    print(f"\nCurso: {nuevo_curso} actualizado exitosamente en el ID: {id_alumno}.")
    
def eliminar_alumno(id_alumno):
    cursor.execute("DELETE FROM alumnos WHERE id = ?", (id_alumno,))
    conexion.commit()
    print("\nAlumno con ID {id_alumno} eliminado exitosamente.")

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
             
    elif opcion == 3:
        mostrar_alumnos()
        id_alumno = input("\nIngrese el ID del alumno a actualizar: ").strip()
        nuevo_curso = input("Ingrese el nuevo curso: ").strip()
        
        if id_alumno.isdigit():
            actualizar_curso(int(id_alumno), nuevo_curso)
        else:
            print("El ID debe ser un número válido.")
            

    elif opcion == 4:
        mostrar_alumnos()
        
        id_alumno = input("\nIngrese el ID del alumno a eliminar: ").strip()
        if id_alumno.isdigit():
            eliminar_alumno(int(id_alumno))
        else:
            print("El ID debe ser un número válido.")
        

    elif opcion == 5:        
        print("============================================================\n")

        print("                   Fin del programa...")
        print("\n============================================================\n")
        break
    
    else:
        print("Opción fuera de rango (1-5). Intente nuevamente.")
        
print("============================================================")
print("              Desarrollado por: Juan Saavedra            ")
print("============================================================\n")