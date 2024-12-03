
# Instalacja Matplotlib

Aby zainstalować bibliotekę `matplotlib`, użyj następującej komendy w terminalu:

```bash
python -m pip install matplotlib
```

---

## Kodzik na prosty wykresik z opisem

Poniżej znajduje się przykład prostego wykresu:

```python
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()  # subplots wywołuje wykres (1 lub więcej). 
# Zmienna `fig` przedstawia cały rysunek, a `ax` jeden wykres na rysunku.
ax.plot(squares)  # plot próbuje wyświetlić te liczby w logiczny sposób.

plt.show()  # Wyświetla nasz rysunek i pozwala użytkownikowi go zapisać i się po nim poruszać.
```

---

## Formatowanie wykresu

Możesz dodać tytuł, etykiety i dostosować inne elementy wykresu:

```python
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=5)  # Ustawienie grubości linii wykresu.

# Zdefiniowanie tytułu i etykiet osi.
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# Zdefiniowanie wielkości etykiet osi.
ax.tick_params(axis='both', labelsize=14)

plt.show()
```

---

## Wyświetlanie dostępnych stylów w Matplotlib

Aby wyświetlić dostępne style, uruchom poniższe komendy w powłoce Pythona:

```python
import matplotlib.pyplot as plt
plt.style.available
```

### Użycie stylu w kodzie

Przykład z użyciem stylu:

```python
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('dark_background')  # Wybór stylu.
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=5)  # Pierwszy parametr to wartości na osi X.

# Zdefiniowanie tytułu i etykiet osi.
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# Zdefiniowanie wielkości etykiet osi.
ax.tick_params(axis='both', labelsize=14)

plt.show()
```

---

## Wyświetlanie poszczególnych punktów

```commandline
import matplotlib.pyplot as plt

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200) # koordynaty punktu, param s zmienia wielkość punktu

# definiowanie tytułu wykresu i etykiet osi
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# zdefiniowanie wielkości etykiet
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
```

## Wyświetlanie listy punktów

```commandline
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=200) # koordynaty punktu, param s zmienia wielkość punktu

# definiowanie tytułu wykresu i etykiet osi
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# zdefiniowanie wielkości etykiet
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
```

## Wyświetlanie serii zapętlonych punktów

```commandline
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=200) # koordynaty punktu, param s zmienia wielkość punktu

# definiowanie tytułu wykresu i etykiet osi
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# zdefiniowanie wielkości etykiet
ax.tick_params(axis='both', which='major', labelsize=14)

# zdefiniowanie zakresu dla każdej osi
ax.axis([0, 1100, 0, 1100000])

plt.show()
```

---

## Kolory

```commandline
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='red', s=200) # koordynaty punktu, param s zmienia wielkość punktu, param r to kolor mozna tez hexa podac w krotce np c(33,33,33)

# definiowanie tytułu wykresu i etykiet osi
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# zdefiniowanie wielkości etykiet
ax.tick_params(axis='both', which='major', labelsize=14)

# zdefiniowanie zakresu dla każdej osi
ax.axis([0, 1100, 0, 1100000])

plt.show()
```

## Mapy kolorów (ciepło to -> zimno etc)

```commandline
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) # koordynaty punktu, 
# param c podajemy wg czego chcemy mapowac, i skale kolorow w cmap

# definiowanie tytułu wykresu i etykiet osi
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# zdefiniowanie wielkości etykiet
ax.tick_params(axis='both', which='major', labelsize=14)

# zdefiniowanie zakresu dla każdej osi
ax.axis([0, 1100, 0, 1100000])

plt.show()
```

## Autosave wykresów

Na końcu
```commandline

# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight') # zamiast show to bedzie zapisywal w 
# local directory wykres, 2 arg usuwa biale znaki z nazwy
```

## Zadanko swoje, kilka nowych komend
```commandline
import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('_mpl-gallery')
fig, ax = plt.subplots(figsize=(10,6)) # fig size zmienia rozmiar wykresu
ax.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Blues, s=20)

ax.set_title("Sześciany liczb", fontsize=20)
ax.set_xlabel("Wartości", fontsize=15)
ax.set_ylabel("Wyniki sześcianów", fontsize=15)
ax.tick_params(axis='both', which='major', labelsize=14)

plt.tight_layout() #automatyczne dopsaowanie wykresu bo ucinalo mi widok
plt.show()
```

# Błądzenie losowe

## Klasa błądzenia losowego z generowaniem
```commandline
# tworzymy klasę imitującą losowy ruch

from random import choice

class RandomWalk():
    """Klasa przeznaczona do wygenerowania błądzenia losowego"""
    def __init__(self, num_points=5000): # wybieramy generowanie 5k punktow
        """Inicjalizacja atrybutów błądzenia"""
        self.num_points = num_points

        # punkt początkowy ma współrzędne 0,0
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Wygenerowanie wszystkich punktów aż do chwili osiągnięcia oczekiwanej liczby punktów"""

        # Wykonywanie kroków aż do chwili osiągnięcia oczekiwanej liczby punktów
        while len(self.x_values) < self.num_points:

            # Ustalenie kierunku oraz odległości do pokonania w tym kierunku
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Odczucenie ruchów, które prowadzą donikąd
            if x_step == 0 and y_step == 0:
                continue
            # Ustalenie następnych wartości X i Y
            x = self.x_values[-1] + x_step # -1 to ostatni element listy
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
```

## Wizualizacja i wywołanie klasy
```commandline
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Przygotowanie błądzenia losowego i wyświetlenie punktów
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Wyświetlenie punktów błądzenia losowego
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(20,11.25), dpi=128) # figsize ustawia wielkosc okna z rysunkiem
    point_numbers = range(rw.num_points) # generujemy listę liczby punktów
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.cm.Blues,edgecolors=None, s=1) # edgecolor wylaczy nam obramowki puntkow

    # Podkreślenie pierwszego i ostatniego punktu błądzenia losowego
    ax.scatter(0,0, c='green', edgecolors='none', s=100) # początkowy
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100) # końcowy; -1 to ostatni element listy

    # Ukryjmy sobie osie
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Utworzyć kolejne błądzenie losowe?[t/n]: ")
    if keep_running == 'n':
        break
```

# Symulacja rzutu kością do gry
Instalacja pakietu ploty

```commandline
python -m pip install plotly
```

### Pojedynczy rzut kością 6 ściankową

Plik die.py
```commandline
from random import randint

class Die:
    """Klasa przedstawiająca pojedynczą kość do gry."""

    def __init__(self, num_sides=6):
        """Przyjęcie założenia, że kość do gry ma postać sześcianu."""
        self.num_sides = num_sides

    def roll(self):
        """Zwrot wartości z zakresu od 1 do liczby ścianek, które ma kość do gry."""
        return randint(1, self.num_sides)
```

Plik die_visual.py
```commandline
from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Utworzenie kości typu D6
die = Die()

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście
results = []
for _ in range(1000):
    result = die.roll()
    results.append(result)

# Analiza wyników
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value) # liczy ile wystąpień poszczególnej wartości z danej ścianki
    frequencies.append(frequency)

# Wizualizacja wyników
x_values = list(range(1, die.num_sides+1)) # tworzymy słupki 1 do 6, plotly musi dostać to jako listę więc konwert
data = [Bar(x=x_values, y=frequencies)] # Bar to klasa, która przedstawia zbiór danych formatowany jako wykres słupkowy,
# potrzebuje ona listy wartości osi x i y

x_axis_config = {'title': 'Wynik'} # Tutaj config, w tym przykładzie dajemy tylko tytuł osi
y_axis_config = {'title': 'Częstotliwość występowania wartości'}
my_layout = Layout(title='Wynik rzucania pojedynczą kością D6 tysiąc razy',
                   xaxis=x_axis_config, yaxis=y_axis_config) # klasa layout zwraca obiekt określający wygląd i konfigurację wykresu
# jako całości
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html') # wywołanie wykresu i dane konfiguracyjne
# w tym np. nazwa pliku do której chcemy zapisac wykres
```

### Rzut dwiema kościami
```commandline
# Rzut parą kości

from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Utworzenie kości typu D6
die_1 = Die()
die_2 = Die(10)

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście
results = []
for _ in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analiza wyników
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(2, max_results+1): # no tak bo najmniej sie da wylosować z 2 scianek 1+1
    frequency = results.count(value) # liczy ile wystąpień poszczególnej wartości z danej ścianki
    frequencies.append(frequency)

# Wizualizacja wyników
x_values = list(range(2, max_results+1)) # tworzymy słupki 1 do 12, plotly musi dostać to jako listę więc konwert
data = [Bar(x=x_values, y=frequencies)] # Bar to klasa, która przedstawia zbiór danych formatowany jako wykres słupkowy,
# potrzebuje ona listy wartości osi x i y

x_axis_config = {'title': 'Wynik', 'dtick': 1} # dtick ustawia zawsze etykiety niezależnie od liczby slupkow,
# otherwise plotly bedzie filtrowac niektore etykiety i ich nie wyswietlac :(
y_axis_config = {'title': 'Częstotliwość występowania wartości'}
my_layout = Layout(title='Wynik rzucania dwiema kościami D6 tysiąc razy',
                   xaxis=x_axis_config, yaxis=y_axis_config) # klasa layout zwraca obiekt określający wygląd i konfigurację wykresu
# jako całości
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html') # wywołanie wykresu i dane konfiguracyjne
# w tym np. nazwa pliku do której chcemy zapisac wykres
```

### Rzut kostek z różną ilością ścianek

Plik dice_visual_different_sizes.py
```commandline
# Rzut parą kości

from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Utworzenie kości typu D6
die_1 = Die()
die_2 = Die(10) # kostka będzie miała 10 ścianek

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście
results = []
for _ in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analiza wyników
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(2, max_results+1): # no tak bo najmniej sie da wylosować z 2 scianek 1+1
    frequency = results.count(value) # liczy ile wystąpień poszczególnej wartości z danej ścianki
    frequencies.append(frequency)

# Wizualizacja wyników
x_values = list(range(2, max_results+1)) # tworzymy słupki 1 do 12, plotly musi dostać to jako listę więc konwert
data = [Bar(x=x_values, y=frequencies)] # Bar to klasa, która przedstawia zbiór danych formatowany jako wykres słupkowy,
# potrzebuje ona listy wartości osi x i y

x_axis_config = {'title': 'Wynik', 'dtick': 1} # dtick ustawia zawsze etykiety niezależnie od liczby slupkow,
# otherwise plotly bedzie filtrowac niektore etykiety i ich nie wyswietlac :(
y_axis_config = {'title': 'Częstotliwość występowania wartości'}
my_layout = Layout(title='Wynik rzucania dwiema kościami D6 i D10 PISIONT tysięcy razy',
                   xaxis=x_axis_config, yaxis=y_axis_config) # klasa layout zwraca obiekt określający wygląd i konfigurację wykresu
# jako całości
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html') # wywołanie wykresu i dane konfiguracyjne
# w tym np. nazwa pliku do której chcemy zapisac wykres
```

# Pobieranie danych

## Format CSV - comma separated values