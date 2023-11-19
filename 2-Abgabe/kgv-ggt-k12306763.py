# Aufgabe 2: Programmgerüst aus Angabe
# Name:Stamou Christos
# Matrikelnummer: k12306763
# LVA-Nummer: 382.029
# Beschreibung: In diesem Programm werden die ggt und das kgv vielfache von zwei Natürlichen Zahlen berechnet.
# Die Funktion ggt(a,b) berechnet den ggt von zwei Zahlen und kgv(a,b) das kgv.
# Im Hauptteil werden zwei Zahlen eingegeben und werden in der try-Anweisung in int umgewandelt.
#Ist die Umwandlung erfolgreich, werden die Funktionen ggt(a,b) und kgv(a,b) aufgerufen
# und die Ergebnoisse werden ausgegeben. Ist die Umwandlung nict erfolgreich, erscheint eine Fehlermeldung.


def ggt(a,b):
    while b!=0:
        #modulo operation, um rest zu berechnen
        a, b= b, a %  b
        
    return a

def kgv(a,b):
   
#kgv mithilfe des ggt berechnen. Zuerst Produkt von a und b berechnen, dann durh ggt von beiden geteilt.
    return abs(a*b)//ggt(a, b)


a=input('Eine Zahl a bitte: ')
b=input('Eine Zahl b bitte: ')
try:
    a=int(a)
    b=int(b)
    teiler=ggt(a,b)
    print('Der größte gemeinsame Teiler von',a,'und',b,'ist',teiler)
    vielfaches=kgv(a,b)
    print('Das kleinste gemeinsame Vielfache',a,'und',b,'ist',vielfaches)
except:
    print('a und b müssen natürliche Zahlen sein')

