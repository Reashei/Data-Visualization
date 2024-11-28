import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) # koordynaty punktu, param s zmienia wielkość punktu, param r to kolor mozna tez hexa podac w krotce np c(33,33,33)

# definiowanie tytułu wykresu i etykiet osi
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# zdefiniowanie wielkości etykiet
ax.tick_params(axis='both', which='major', labelsize=14)

# zdefiniowanie zakresu dla każdej osi
ax.axis([0, 1100, 0, 1100000])

# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight') # zamiast show to bedzie zapisywal w local directory wykres
