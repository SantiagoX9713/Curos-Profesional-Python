from datetime import datetime
import pytz


bogota_tz = pytz.timezone('America/Bogota')
argentina_tz = pytz.timezone('America/Argentina/Buenos_Aires')
canada_tz = pytz.timezone('Canada/Central')
bogota_date = datetime.now(bogota_tz)
argentina_date = datetime.now(argentina_tz)
canada_date = datetime.now(canada_tz)
print('La hora en Colombia es: ' + bogota_date.strftime('%H:%S:%M'))
print('La hora en Argentina es: ' + argentina_date.strftime('%H:%S:%M'))
print('La hora en Cánada es: ' + canada_date.strftime('%H:%S:%M'))