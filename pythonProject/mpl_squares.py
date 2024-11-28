import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots() # subplots wywoluje wykres (1 lub wiecej). Zmienna fig przedstawia caly rysunek, a ax jeden wykres na rysunku
ax.plot(input_values, squares, linewidth=5) # plot probuje wyswqietlic te liczby w logiczny sposob, jako 1 parametr to wartosci na osi x,
# bo normalnie numeracja jest od 0 :(

# zdefiniowanie tytułu i etykiet osi
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# zdefiniowanie wielkości etykiet
ax.tick_params(axis='both', labelsize=14)

plt.show() # wyswietla nasz rysunek i pozwala userowi go zapiswyac i sie po nim poruszac
