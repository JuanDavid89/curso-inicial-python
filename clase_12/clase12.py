# Persistencia de datos

# Leer lo que contiene el archivo
'''archivo = open("datos.txt", "r", encoding="utf-8")
lineas = archivo.readlines()
for linea in lineas:
    print(linea.strip(""))
archivo.close()'''

# Escribir o sobre escribir lo que contiene el archivo
'''archivo = open("mensajes.txt", "w", encoding="utf-8")
archivo.write("Hola Analista!\n")
archivo.write("Ven a comenzar en tu camino del análisis de datos")
archivo.close()'''

# Agrega un nuevo texto
'''archivo = open("mensajes.txt", "a", encoding="utf-8")
archivo.write("\nPor Juan, futuro analista de datos!\n")
archivo.close()'''

# Escribir nombres en un archivo
archivo = open("nombres.txt", "w", encoding="utf-8")
archivo.write("Juan\n")
archivo.write("Barbara\n")
archivo.write("Gina\n")
archivo.write("Juan Gregorio\n")
archivo.write("Ada\n")
archivo.write("Emma\n")
archivo.write("Sara\n")
archivo.write("Sebastian\n")
archivo.close()

archivo = open("nombres.txt", "r", encoding="utf-8")
print("\n=== Contenido del archivo ===\n")
for linea in archivo:
    print(linea.strip(""))
print("=== Fin del programa ===\n")
archivo.close()