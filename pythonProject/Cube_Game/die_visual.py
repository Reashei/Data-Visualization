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
for value in range(1, die.num_sides + 1):
    frequency = results.count(
        value
    )  # liczy ile wystąpień poszczególnej wartości z danej ścianki
    frequencies.append(frequency)

# Wizualizacja wyników
x_values = list(
    range(1, die.num_sides + 1)
)  # tworzymy słupki 1 do 6, plotly musi dostać to jako listę więc konwert
data = [
    Bar(x=x_values, y=frequencies)
]  # Bar to klasa, która przedstawia zbiór danych formatowany jako wykres słupkowy,
# potrzebuje ona listy wartości osi x i y

x_axis_config = {
    "title": "Wynik"
}  # Tutaj config, w tym przykładzie dajemy tylko tytuł osi
y_axis_config = {"title": "Częstotliwość występowania wartości"}
my_layout = Layout(
    title="Wynik rzucania pojedynczą kością D6 tysiąc razy",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)  # klasa layout zwraca obiekt określający wygląd i konfigurację wykresu
# jako całości
offline.plot(
    {"data": data, "layout": my_layout}, filename="d6.html"
)  # wywołanie wykresu i dane konfiguracyjne
# w tym np. nazwa pliku do której chcemy zapisac wykres
