'''
Napisz program, który oblicza pole i obwód koła o promieniu podanym przez użytkownika. Wartość stałej
π weź z biblioteki math. Promień nie może być ujemny. W przypadku podania liczby ujemnej, program
powinien wypisywać komunikat informujący o błędnej wartości i nic nie liczyć.
'''
import math
while True:
    r = float(input("Podaj promień koła: "))
    if r > 0:
        pole, obwod = math.pi*r**2, 2*math.pi*r

        print(f"Pole koła wynosi: {pole:.2f}, natomiast obwód wynosi {obwod:.2f}")
        break
    else:
        print("Promień nie może być ujemny!")


