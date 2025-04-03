
print("Menu")

print("1 - Prosty kalkulator dwoch liczb")
print("2 - Konwerter temperatur (Celsjusz ↔ Fahrenheit)")
print("3 - Srednia ocen ucznia")

menu_option = int(input("Opcja: "))

def switch_menu(menu_option):
    match menu_option:
        case 1:
             print("Prosty kalkulator dwoch liczb")
             a = int(input("Podaj pierwsza liczbe: "))
             b = int(input("Podaj druga liczbe: "))
             print("Podaj jaka operacje arytmetyczna chcesz wykonac (+, -, *, /): ")
             zad1_option = input()
             if zad1_option == "+":
                wynik1 = a + b
             elif zad1_option == "-":
                wynik1 = a - b
             elif zad1_option == "*":
                wynik1 = a * b
             elif zad1_option == "/":
                 if b != 0:
                     wynik1 = a / b
                 else:
                     return ("Nie mozna dzielic przez 0")
             else:
                 return "Bledna operacja arytmetyczna" 
             return (f"Wynik = {wynik1}")
        case 2:
             print("Konwerter temperatur (Celsjusz ↔ Fahrenheit")
             zad2_option = input("Wybierz kierunek konwersji (C = (Celsjusz -> Fahrenheit) F = (Fahrenheit -> Celsjusz)): " )
             c = int(input("Wprowadz wartosc temperatury: "))
             if zad2_option in ("C", "c"):
                    wynik2 = c * 1.8 + 32
                    return (f"Wynik = {wynik2}°F")
             elif zad2_option in ("F", "f"):
                    wynik2 = (c - 32) / 1.8
                    return (f"Wynik = {wynik2}°C")
             else:
                 return "Blednie wprowadzony kierunek konwersji"
        case 3:
             print("Srednia ocen ucznia")
        case _:
             return "Niepoprawna opcja"

print(switch_menu(menu_option))