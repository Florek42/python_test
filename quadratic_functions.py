import math

def calculate_vertex(a, b, c):
    P = (-b) / (2 * a)
    Q = (-delta) / (4 * a)
    return P, Q

def calculate_delta(a, b, c):
    delta = b ** 2 - 4 * a * c
    return delta

def calculate_zero_places(a, b, c, delta):
    if delta == 0:
        x_zero = (-b) / (2 * a)
        return round(x_zero)
    elif delta > 0:
        x_pierwszy = ((-b) - math.sqrt(delta)) / (2 * a)
        x_drugi = ((-b) + math.sqrt(delta)) / (2 * a)
        return round(x_pierwszy), round(x_drugi)
    else:
        return None
