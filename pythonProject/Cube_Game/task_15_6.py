# Rzut parą kości

from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Utworzenie kości typu D6
die_1 = Die(8)
die_2 = Die(8)

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście
results = []
for _ in range(100000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analiza wyników
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(
    2, max_results + 1
):  # no tak bo najmniej sie da wylosować z 2 scianek 1+1
    frequency = results.count(
        value
    )  # liczy ile wystąpień poszczególnej wartości z danej ścianki
    frequencies.append(frequency)

# Wizualizacja wyników
x_values = list(
    range(2, max_results + 1)
)  # tworzymy słupki 1 do 12, plotly musi dostać to jako listę więc konwert
data = [
    Bar(x=x_values, y=frequencies)
]  # Bar to klasa, która przedstawia zbiór danych formatowany jako wykres słupkowy,
# potrzebuje ona listy wartości osi x i y

x_axis_config = {
    "title": "Wynik",
    "dtick": 1,
}  # dtick ustawia zawsze etykiety niezależnie od liczby slupkow,
# otherwise plotly bedzie filtrowac niektore etykiety i ich nie wyswietlac :(
y_axis_config = {"title": "Częstotliwość występowania wartości"}
my_layout = Layout(
    title="Wynik rzucania dwiema kościami D6 i D10 PISIONT tysięcy razy",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)  # klasa layout zwraca obiekt określający wygląd i konfigurację wykresu
# jako całości
offline.plot(
    {"data": data, "layout": my_layout}, filename="d6_d10.html"
)  # wywołanie wykresu i dane konfiguracyjne
# w tym np. nazwa pliku do której chcemy zapisac wykres
