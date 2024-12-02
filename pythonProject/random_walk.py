# tworzymy klasę imitującą losowy ruch

from random import choice


class RandomWalk:
    """Klasa przeznaczona do wygenerowania błądzenia losowego"""

    def __init__(self, num_points=5000):  # wybieramy generowanie 5k punktow
        """Inicjalizacja atrybutów błądzenia"""
        self.num_points = num_points

        # punkt początkowy ma współrzędne 0,0
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        # Ustalenie kierunku oraz odległości do pokonania w tym kierunku
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        x_step = x_direction * x_distance

        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4])
        y_step = y_direction * y_distance

        return x_step, y_step

    def fill_walk(self):
        """Wygenerowanie wszystkich punktów aż do chwili osiągnięcia oczekiwanej liczby punktów"""

        # Wykonywanie kroków aż do chwili osiągnięcia oczekiwanej liczby punktów
        while len(self.x_values) < self.num_points:
            x_step, y_step = self.get_step()
            # Odczucenie ruchów, które prowadzą donikąd
            if x_step == 0 and y_step == 0:
                continue
            # Ustalenie następnych wartości X i Y
            x = self.x_values[-1] + x_step  # -1 to ostatni element listy
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
