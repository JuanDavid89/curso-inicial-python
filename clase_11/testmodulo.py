# Para importar todas las funciones
'''
import utilidades

utilidades.saludar("Juan")
utilidades.despedir("Juan")
''' 

# Para cuando solo se usa una función
'''
from utilidades import despedir

despedir("Lucas")
'''

# Para renombrar una función, esto es util para que vaya acorde al main

from utilidades import despedir as despedida

despedida("Lucas")
