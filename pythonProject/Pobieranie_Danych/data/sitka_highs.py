import csv

import matplotlib.pyplot as plt

filename = 'sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) # obiekt przeglądarki do zmiennej reader
    header_row = next(reader) # pobieramy pierwszy wiersz, czyli nagłówki pliku

    # Pobranie maks temperatur z pliku (index 5 to temp max i 2 to data)
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

    print(highs)

# Dane wykresu
plt.style.use('fast')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Formatowanie wykresu
ax.set_title("Najwyższa temperatura dnia, lipiec 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
