import quadratic_functions
import calculations

def main():
    nums = input("Podaj a, b oraz c rozdzielone spacją: ")
    a, b, c = map(int, nums.split())

    choice = input("Co chcesz obliczyć? (1 - Wierzchołki paraboli, 2 - Delta, 3 - Miejsca zerowe, 4 - Kierunek funkcji): ")

    if choice == "1":
        P, Q = quadratic_functions.calculate_vertex(a, b, c)
        print(f"Wierzchołki paraboli (P,Q) to: ({round(P)},{round(Q)})")
    elif choice == "2":
        delta = quadratic_functions.calculate_delta(a, b, c)
        print(f"Delta tej funkcji i jej pierwiastek wynoszą: √{delta} = {math.sqrt(delta)}")
    elif choice == "3":
        delta = quadratic_functions.calculate_delta(a, b, c)
        zeros = quadratic_functions.calculate_zero_places(a, b, c, delta)
        if zeros:
            if isinstance(zeros, int):
                print(f"Miejsce zerowe wynosi: {zeros}")
            else:
                print(f"Miejsca zerowe to: x1 = {zeros[0]}, x2 = {zeros[1]}")
        else:
            print("Brak miejsc zerowych dla tej funkcji.")
    elif choice == "4":
        if calculations.is_increasing(a):
            print("Funkcja jest rosnąca!")
        elif calculations.is_decreasing(a):
            print("Funkcja jest malejąca!")
    else:
        print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    main()
