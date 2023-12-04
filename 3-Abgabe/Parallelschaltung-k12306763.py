"""
Dateiname: Parallelschaltung-k12306763
Erstellungsdatum: 03.12.2023
Name: Christos Stamou
Matrikelnummer: k12306763
Beschreibung:In diesem Programm können wir die Anzahl der Widerstände und die Werte der Widerstände selbst eingeben. 
Die Funktion "parallel" berechnet dann den Gesamtwiderstand, wenn die Widerstände parallel geschaltet werden.
"""


def parallel(widerstaende):
    return 1 / sum(1 / w for w in widerstaende)

def gib_zahl_ein(text):
    while True:
        try:
            n = int(input(text))
            if n < 1:
                print("Die Anzahl muss größer oder gleich 1 sein.")
                continue
            return n
        except ValueError:
            print("Das war keine gültige Zahl. Bitte versuchen Sie es erneut.")

def gib_widerstand_ein(i):
    while True:
        try:
            w = float(input(f"Widerstand Nr.{i} in Ohm: "))
            if w <= 0:
                print("Der Widerstandswert muss größer als 0 sein.")
                continue
            return w
        except ValueError:
            print("Das war keine gültige Zahl. Bitte versuchen Sie es erneut.")

def main():
    n = gib_zahl_ein("Wie viele Widerstände sollen parallel geschaltet werden? ")
    widerstaende = [gib_widerstand_ein(i) for i in range(1, n + 1)]
    try:
        gesamt_widerstand = parallel(widerstaende)
        print(f"Diese Widerstände parallel ergeben einen Gesamtwiderstand von: {gesamt_widerstand} Ohm")
    except ZeroDivisionError:
        print("Der Gesamtwiderstand konnte nicht berechnet werden, da ein oder mehrere Widerstände gleich 0 Ohm sind.")

if __name__ == "__main__":
    main()