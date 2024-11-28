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
