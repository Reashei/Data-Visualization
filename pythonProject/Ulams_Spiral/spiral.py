import matplotlib.pyplot as plt
import numpy as np


# Funkcja sprawdzająca czy liczba pierwsza
def is_prime(n):
    if n < 2:
        return False
    for i in range(
        2, int(np.sqrt(n)) + 1
    ):  # Aby sprawdzić, czy liczba n jest liczbą pierwszą,
        # wystarczy sprawdzić, czy istnieje liczba całkowita w zakresie od 2 do √n, która dzieli n bez reszty.
        if n % i == 0:
            return False
    return True


# Funkcja generująca współrzędna spiralne
def generate_spiral(size):
    x, y = 0, 0  # Start po środku
    dx, dy = 0, -1  # Kierunek początkowy
    spiral = []

    for i in range(1, size + 1):
        if -size // 2 < x <= size // 2 and -size // 2 < y < size // 2:
            spiral.append((x, y, i))

        # Sprawdz czy trzeba zmienić kierunek (kwadratowe wzory)
        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx

        x, y = x + dx, y + dy
    return spiral


size = 1000
spiral = generate_spiral(size**2)

prime_x = []
prime_y = []

for x, y, num in spiral:
    if is_prime(num):
        prime_x.append(x)
        prime_y.append(y)

plt.figure(figsize=(10, 10))
plt.scatter(
    *zip(*[(x, y) for x, y, _ in spiral]),
    color="lightgray",
    s=1,
    label="Liczby całkowite",
)
plt.scatter(prime_x, prime_y, color="blue", s=5, label="Liczby pierwsze")
plt.axis("equal")
plt.axis("off")
plt.title("Spirala Ulama", fontsize=16)
plt.legend()
plt.show()
