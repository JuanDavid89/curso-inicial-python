import datetime
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UFT-8')

fecha_hora_actual = datetime.datetime.now()

dia_capitalizado = fecha_hora_actual.strftime("%A").capitalize()
mes_capitalizado = fecha_hora_actual.strftime("%B").capitalize()

print("Fecha y hora actual:", fecha_hora_actual)
print("Fecha actual:", fecha_hora_actual.strftime("%Y/%m/%d"))
print("Hora actual:", fecha_hora_actual.strftime("%H:%M:%S"))

# Mostrar la fecha en formato legible
print("Fecha legible:", fecha_hora_actual.strftime("%d de %B de %Y"))

print("Fecha legible:", fecha_hora_actual.strftime(f"{dia_capitalizado} %d de {mes_capitalizado} de %Y"))