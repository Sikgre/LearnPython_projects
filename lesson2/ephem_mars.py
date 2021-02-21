import ephem
from datetime import date

today = date.today()
mars = ephem.Mars(today)
constell = ephem.constellation(mars)

print(constell)



