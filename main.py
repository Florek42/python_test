'''
Napisz program, który oblicza pole i obwód koła o promieniu podanym przez użytkownika. Wartość stałej
π weź z biblioteki math. Promień nie może być ujemny. W przypadku podania liczby ujemnej, program
powinien wypisywać komunikat informujący o błędnej wartości i nic nie liczyć.
'''



nums = input("Podaj a oraz b rozdzielone spacją: ")
a, b = map(int, nums.split())  

print(f"suma {a} i {b}=", a + b)
print(f"iloczyn {a} i {b} =", a * b)
print(f"iloraz {a} i {b} =", a / b)
print(f"pierwiastek {a}+{b} =", math.sqrt(a + b))
print(f"{a} do potegi {b} =", a ** b)
