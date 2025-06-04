# Este es un modulo nativo de python
import random

# este modulo se puede usar por ejemplo para generar un token
# Genera valores flotantes 
'''valor = random.random()
print(valor)'''

# Genera valores enteros en 1 y 10
'''valor = random.randint(1, 10)
print(valor)'''

# Ejercicio Lanza dados
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2

    print(f"Lanazaste un {dado1} y un {dado2}. Tu suma es: {suma}")

lanzar_dados()