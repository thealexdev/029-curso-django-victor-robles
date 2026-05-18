# modulo de fechas
import datetime

print(f"La fecha de hoy es: {datetime.date.today()}")

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.day)
print(fecha_completa.month)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print(fecha_personalizada)

print(datetime.datetime.now().timestamp())
