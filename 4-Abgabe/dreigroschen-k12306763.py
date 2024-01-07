"""
Dateiname: dreigroschen-k12306763
Erstellungsdatum: 06.01.2024
Name: Christos Stamou
Matrikelnummer: k12306763
Beschreibung: Das Programm analysiert die Häufigkeit von Wörtern in einem Textdokument. Zunächst werden die Häufigkeit der 
Wörter in der Funktion def_häufigkeit gezählt. Sonderzeichen werden entfernt und alle Buchstaben werden in Kleinbuchstaben 
umgewandelt. in def main wird der Text ausgelesen. Dann wird die erste Funktion angewandt, die Wörter gezählt und die 20 
häufigsten werden ausgegeben. Zudem wird noch die Gesamtwortanzahl des Textes ausgegeben. 
"""

def wort_haeufigkeit(text):
    # Entferne Sonderzeichen und konvertiere zu Kleinbuchstaben
    text = ''.join([c.lower() if c.isalnum() or c.isspace() else ' ' for c in text])
    # Teile den Text in Wörter auf
    woerter = text.split()
    # Zähle die Häufigkeit der Wörter
    haeufigkeiten = {}
    for wort in woerter:
        haeufigkeiten[wort] = haeufigkeiten.get(wort, 0) + 1
    return haeufigkeiten

def main():
    # Lese den Text aus der Datei
    with open('dreigroschenoper.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # Bestimme die Häufigkeit der Wörter
    haeufigkeiten = wort_haeufigkeit(text)

    # Sortiere die Wörter nach ihrer Häufigkeit
    sortierte_haeufigkeiten = sorted(haeufigkeiten.items(), key=lambda x: x[1], reverse=True)
    
    # Gesamtwörterzahl im Text
    gesamt_woerter = len(text.split())
    print(f"Gesamtwortzahl im Text: {gesamt_woerter}")

    print("Die 20 häufigsten Wörter:")
    for wort, haeufigkeit in sortierte_haeufigkeiten[:20]:
        prozentsatz = (haeufigkeit / gesamt_woerter) * 100
        print(f"{wort}: {haeufigkeit} Mal, {prozentsatz:.2f}%")
        

if __name__ == "__main__":
    main()
