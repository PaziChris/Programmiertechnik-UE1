"""
Dateiname: rational-k12306763
Erstellungsdatum: 23.01.2024
Name: Christos Stamou
Matrikelnummer: k12306763
Beschreibung: 

Die Rational-Klasse repräsentiert rationale Zahlen als Brüche. Der Konstruktor init initialisiert
eine rationale Zahl und kürzt sie dabei. Die Methode shorten kürzt die rationale Zahl weiter. Die Methode ggt berechnet den größten gemeinsamen Teiler.
Die Methode str gibt eine Zeichenkettenrepräsentation der rationalen Zahl aus. Der *-Operator wird überladen, um die Multiplikation von zwei rationalen Zahlen zu ermöglichen.

Im Hauptprogramm können Benutzer zwei rationale Zahlen eingeben, die dann multipliziert und formatiert ausgegeben werden. Eingaben werden auf Gültigkeit überprüft, und Fehler werden behandelt.
"""

class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Der Nenner darf nicht null sein.")
        common_factor = self._gcd(numerator, denominator)
        self.numerator = numerator // common_factor
        self.denominator = denominator // common_factor

    def __ggt__(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __shorten__(self):
        common_factor = self._gcd(self.numerator, self.denominator)
        self.numerator //= common_factor
        self.denominator //= common_factor

    def str(self):
        return f"{self.numerator}/{self.denominator}"

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        result = Rational(new_numerator, new_denominator)
        result.shorten()
        return result


if __name__ == "__main__":
    try:
        num1 = int(input("Geben Sie den Zähler der ersten rationalen Zahl ein: "))
        den1 = int(input("Geben Sie den Nenner der ersten rationalen Zahl ein: "))
        num2 = int(input("Geben Sie den Zähler der zweiten rationalen Zahl ein: "))
        den2 = int(input("Geben Sie den Nenner der zweiten rationalen Zahl ein: "))

        rational1 = Rational(num1, den1)
        rational2 = Rational(num2, den2)

        result = rational1 * rational2

        print(f"Das Produkt der rationalen Zahlen ist: {result}")

    except ValueError as e:
        print(f"Fehler: {e}")
