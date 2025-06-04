import math

# Modulo nativo para calculos matematicos

# Redondeos

# Para arriba
hojas_importantes_a_guardar = 2.3

folios_necesarios = math.ceil(hojas_importantes_a_guardar)

print(f"Necesitas {folios_necesarios} folios para guardar todo")

# Para abajo
litros_jugo = 17.8

# (floor(x) = el entero más grande menor o igual a x)

botellas_llenas = math.floor(litros_jugo)

print(f"Puedes llenar {botellas_llenas} botellas completas de jugo")