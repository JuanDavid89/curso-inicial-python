# Try except simple
'''edad = input("Ingresa un número: ")

try:
    edad = int(edad)
    print(f"Tienes {edad} años.")
except:
    print("| Error | Ingresa tu edad en números.")

print("Fin derl programa")'''

# Ejemplo con condicionales y errores mas comunes
'''edad = input("Ingresa un número: ")

try:
    edad = int(edad)
    print(f"Tienes {edad} años.")
except ValueError as e:
    print(f"Ocurrió un error: {e} debe ingresar su edad en números.")

print("\n==== Fin derl programa ====\n")'''

# Ejemplo con validaciones de email
email = input("Ingrese su email: ")

try:
    if '@' not in email:
        raise ValueError("El email debe contener un carácter '@'.")
    
    print("¡Gracias! El formato del email parece válido (contiene un '@').")

except ValueError as e:
    print(f"Ocurrió un error: {e}")
