import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Przygotowanie błądzenia losowego i wyświetlenie punktów
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Wyświetlenie punktów błądzenia losowego
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(20,11.25), dpi=128) # figsize ustawia wielkosc okna z rysunkiem
    point_numbers = range(rw.num_points) # generujemy listę liczby punktów
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers,t
    #            cmap=plt.cm.Blues,edgecolors=None, s=1) # edgecolor wylaczy nam obramowki puntkow

    ax.plot(rw.x_values, rw.y_values, linewidth=0.5, color='blue')

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
