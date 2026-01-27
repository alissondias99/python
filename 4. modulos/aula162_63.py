# Criando datas com módulo datetime
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime

data_str_data = '2022/04/20 07:49:23'
data_str_data = '22/04/2022'
data_str_fmt = '%d/%m/%Y'
data = datetime.strptime(data_str_data, data_str_fmt)
print(data)

data_atual = datetime.now()
print(data_atual)

delta = data_atual - data
print(delta.days, delta.seconds, delta.microseconds)

from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
# delta = timedelta(days=10, hours=2)
delta = relativedelta(data_fim, data_inicio)
print(delta.days, delta.years)
# print(data_fim - delta)
# print(data_fim)
# print(data_fim + relativedelta(seconds=60, minutes=10))

from pytz import timezone # usado para recuperar a data de outro lugar
data_atual_belem = datetime.now(timezone('Asia/Tokyo'))
print(data_atual_belem)

contador_segundos = datetime.now()
print(contador_segundos.timestamp()) # retorna os segundos passados desde 1/1/1970 até hoje

