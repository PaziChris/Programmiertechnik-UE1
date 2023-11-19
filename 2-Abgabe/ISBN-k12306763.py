# Name:Stamou Christos
# Matrikelnummer: k12306763
# LVA-Nummer: 382.029
# Beschreibung: Die Funktion entfernt zuerst alle Bindestriche und speichert sie in einer Variablen isbn.
# Die Funktion speichert die Prüfziffer in check_digit.
# alle ziffern der ISBN, ausser die Prüfziffer werden in einer liste digits gesoeichert. 
# die berechnung erfolgt laut der angabe. 
# die Funktion ünerprüft, ob die berechnete Prüfziffer mit der eingegebeben identisch ist
# ist dies der fall, gibt die funktion True zurück, andernfalls False. 
# in der hauptausführung wird checkisbn10(isbn) aufgerufen und es erfolgt eine ausgabe. 

def checkisbn10(isbn):
    #bindestrich mit leerzeichen vertauscht
    isbn=isbn.replace('-','')
    #pruefziffer von eingabe entfert
    check_digit = int(isbn[-1])
    #map, um jedes, au§er dem letzten zeichen des strings in eine liste zu speichern
    #digits hat ziffern ohne pruefziffer, variable check_digit mit prŸfziffer
    digits = list(map(int, isbn[:-1])) # [1, 2, 3, 4, ... ]
    
    total = sum(digits[i-1] * i for i in range(1, 10)) # 1*1 + 2*2 + 3*3 ... + 9*9
    pruefziffer= total % 10 #dieser wert wird mit pruefziffer verglichen
    
    #wenn pruefziffer=10, dann in isbn-10 ein x und wird so umgewandelt
    if pruefziffer == 10:
        check_digit = 'X'
    elif check_digit != pruefziffer: #wenn berechnete pruefziffer nicht mit isbn pruefziffe uebereinstimt, dann false.
        return False
    return True #true, wenn vorherige bedingungen nicht erfuellt


#Ausgabe ob Pruefziffer richtig oder falsch
isbn = input("Bitte geben Sie die ISBN-10 ein (ohne Bindestriche): ")

if len(isbn) != 10 or not isbn.isdigit():
    print("Die ISBN-10 sollte genau 10 Ziffern enthalten!")
elif checkisbn10(isbn):
    print("Die ISBN-10 ist korrekt! ")
else:
    print("Die Pruefziffer ist falsch!")
    
    
    

