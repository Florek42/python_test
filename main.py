import math

nums = input("Podaj a, b oraz c rozdzielone spacją: ")
a, b, c = map(int, nums.split())
delta = b ** 2 - 4 * a * c
print(f"Wzór funkcji kwadratowej to: {a}x² + {b}x + {c}\n")
P = (-b) / (2 * a)
Q = (-delta) / (4 * a)

if a>0:
    print("Funkcja jest rosnąca!\n")
if a<0:
    print("Funkcja jest malejąca!\n")


print(f"Wierzchołki paraboli (P,Q) to: ({round(P)},{round(Q)})\n")

if delta >= 0:
    p_delta = math.sqrt(delta)
    print(f"Delta tej funkcji i jej pierwiastek wynoszą: √{delta} = {p_delta}\n")
else:
    print("Delta jest ujemna, brak rozwiązań!")

# miejsca zerowe jesli są
if delta == 0:
    x_zero = (-b) / (2 * a)
    print(f"Miejsce zerowe wynosi: {x_zero}")
elif delta > 0:
    x_pierwszy = ((-b) - p_delta) / (2 * a)
    x_drugi = ((-b) + p_delta) / (2 * a)
    print(f"Miejsca zerowe to: x1 = {round(x_pierwszy)}, x2 = {round(x_drugi)}")

kanoniczna = a+"'('x - "+P+"')'² + "+Q
print(f"Postać kanoniczna funkcji to: {kanoniczna}")
iloczynowa = a+"(x - "+x_pierwszy+")"+"(x - "+x_drugi+")"
print(f"Postać iloczynowa funkcji to: {iloczynowa}")