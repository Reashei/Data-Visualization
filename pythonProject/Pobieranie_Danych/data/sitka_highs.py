import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) # obiekt przeglądarki do zmiennej reader
    header_row = next(reader) # pobieramy pierwszy wiersz, czyli nagłówki pliku

    # Pobranie maks temperatur z pliku (index 5 to temp max i 2 to data)
    dates, highs = [], [] # puste listy do przechowywania danych z pliku
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d") # konwersja daty z tekstowej
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
    print(highs)

# Dane wykresu
plt.style.use('fast')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red') # przekazujemy na wykres nasze dane

# Formatowanie wykresu
ax.set_title("Najwyższa temperatura dnia 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # to wyświetla etykiety ukośne aby się nie nakładały
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
