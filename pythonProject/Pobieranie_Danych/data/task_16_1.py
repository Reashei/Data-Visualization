import matplotlib.pyplot as plt
import csv
from datetime import datetime

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rains = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            rain = float(row[3])
        except ValueError:
             print(f"Nie ma opadów dla {current_date}.")
        else:
            rains.append(rain)
            dates.append(current_date)

# Dane wykresu
plt.style.use('fast')
fig, ax = plt.subplots()
ax.plot(dates, rains, c='red', alpha=0.5)

# Formatowanie wykresu
ax.set_title("Opady w Sitka", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # to wyświetla etykiety ukośne aby się nie nakładały
ax.set_ylabel('Litry?', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)


plt.show()