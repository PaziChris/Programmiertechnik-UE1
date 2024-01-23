"""
Dateiname: spam-iterativ-k12306763
Erstellungsdatum: 23.01.2024
Name: Christos Stamou
Matrikelnummer: k12306763
Beschreibung: 
Das Programm enthält zwei Funktionen zur Überprüfung, ob eine positive Integer-Zahl eine Primzahl ist:
    1. Rekursive Primzahlüberprüfung (spam-Funktion):
Überprüft rekursiv, ob n eine Primzahl ist, indem es alle potenziellen Teiler von 2 bis n-1 prüft.
Gibt True zurück, wenn n keine Teiler außer 1 und n hat, andernfalls False. 

    2. Iterative Primzahlüberprüfung (spam_iterative-Funktion)
Überprüft iterativ, ob n eine Primzahl ist, indem es alle potenziellen Teiler von 2 bis n-1 prüft.
Gibt True zurück, wenn n keine Teiler außer 1 und n hat, andernfalls False.

Das Hauptprogramm testet beide Funktionen mit verschiedenen Zahlen und vergleicht ihre Ergebnisse.
        
"""
"""
a.) Zusammengefasst überprüft die Funktion für eine gegebene positive Integer-Zahl n, 
ob es einen Teiler größer als 1 und kleiner oder gleich n gibt. Wenn kein solcher Teiler gefunden wird, 
wird True zurückgegeben, was bedeutet, dass n eine Primzahl ist. Andernfalls wird False zurückgegeben.
"""

def spam(n, a=2):
 if n <= a :
     return True
 elif n % a == 0:
     return False
 else:
     return spam(n, a+1)


def spam_iterativ(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    # Testen der iterativen Funktion mit verschiedenen Werten
    numbers_to_test = [2, 3, 5, 10, 15, 20, 25, 30, 89]

    for num in numbers_to_test:
        print(f"{num} ist eine Primzahl: {spam_iterativ(num)}")

        # Vergleich mit der gegebenen rekursiven Funktion spam
        print(f"Vergleich mit spam-Funktion: {spam(num)}")
