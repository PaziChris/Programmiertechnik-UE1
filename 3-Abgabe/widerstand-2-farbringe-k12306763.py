"""
Aufgabe 3: Farben von WiderstÃ¤nde
Erstellungsdatum: 04.12.2023
Name: Stamou Christos
Matrikelnummer: k12306763
Beschreibung: Die Funktion "farben_resistor(value)" nimmt eine Zahl
(value) als Eingabe und gibt eine Liste von drei Farben zurück, die den 
gegebenen Widerstandswert reprÃ¤sentieren. Diese Farben repräsentieren 
die drei Bänder eines Widerstands, wobei die ersten beiden Bänder den 
Wert des Widerstands in Ohm darstellen und das dritte Band einen Faktor, um den Wert zu skalieren, 
repräsentiert. Die Funktion "test()", fordert den Benutzer auf, einen 
Widerstandswert in Ohm anzugeben.
"""
def farben_resistor(value):
    color_codes = {
        0: "schwarz", 1: "braun", 2: "rot", 3: "orange",
        4: "gelb", 5: "grÃ¼n", 6: "blau", 7: "violett",
        8: "grau", 9: "weiÃ"
    }

    value_str = str(value)

    if int(value_str[0] != 0) and int(value_str[1] == 0):
        first_band = "schwarz"
        second_band = color_codes[int(value_str[0])]
        third_band = color_codes[len(value_str) - 1]
        
    elif int(value_str[0] == 0) and int(value_str[1] != 0):
        first_band = "schwarz"
        second_band = color_codes[int(value_str[0])]
        third_band = color_codes[len(value_str) - 1]
    
    else:    
        first_band = color_codes[int(value_str[0])]
        second_band = color_codes[int(value_str[1])]
        third_band = color_codes[len(value_str) - 2] 

    return [first_band, second_band, third_band]

def test():
    try:
        value = int(input("Geben Sie den Widerstandswert ein (in Ohm): "))
        if value <= 0:
            print("Bitte geben Sie einen positiven Wert ein.")
            return
        color_code = farben_resistor(value)
        print(f"Farbcode des Widerstands {value}: {color_code}")
    except ValueError:
        print("UngÃ¼ltige Eingabe. Bitte geben Sie eine ganze Zahl ein.")

if __name__ == "__main__":
    test()
