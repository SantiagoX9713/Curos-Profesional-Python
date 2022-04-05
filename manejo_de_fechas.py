import datetime

my_time = datetime.datetime.now()
print(my_time)
print(type(my_time))

my_date = datetime.datetime.today()
print(my_date)
print(type(my_date))

# Accediendo a partes de la fecha
print(f'Año {my_date.year}')
print(f'Mes {my_date.month}')
print(f'Día {my_date.day}')

# Formateo de fechas
"""
%Y -> Year
%m -> Month
%d -> Day
%H -> Hour
%M -> Minute
%S -> Second
"""

# Aplicando el formateo
my_datetime = datetime.datetime.now()
print(my_datetime)

my_str = my_datetime.strftime('%d/%m/%Y')
print(f'Formato para LATAM: {my_str}')

my_str = my_datetime.strftime('%m/%d/%Y')
print(f'Formato para USA: {my_str}')

my_str = my_datetime.strftime('Estamos en el año: %Y')
print(f'Formato x: {my_str}')

my_str = my_datetime.strftime('La hora es: %H:%M:%S')
print(f'Formato x: {my_str}')