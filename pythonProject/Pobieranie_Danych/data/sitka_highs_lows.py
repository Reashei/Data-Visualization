import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) # obiekt przeglądarki do zmiennej reader
    header_row = next(reader) # pobieramy pierwszy wiersz, czyli nagłówki pliku

    # Pobranie maks temperatur z pliku (index 5 to temp max i 2 to data)
    dates, highs, lows = [], [], [] # puste listy do przechowywania danych z pliku
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d") # konwersja daty z tekstowej
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    print(highs)

# Dane wykresu
plt.style.use('fast')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5) # przekazujemy na wykres nasze dane
ax.plot(dates, lows, c='blue', alpha=0.5) # alpha to przezroczystość koloru w skali od 0 do 1
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# fill_between koloruje obszar między jednym wykresem a drugim. 1 arg to serua wartosci i kolejno potem listy
# miedzy ktorymi chcemy zaznaczyc dane, facecolor to kolor obszaru

# Formatowanie wykresu
ax.set_title("Najwyższa i najniższa temperatura dnia 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # to wyświetla etykiety ukośne aby się nie nakładały
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
