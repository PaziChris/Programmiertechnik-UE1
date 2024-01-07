"""
Dateiname: morse-k12306763
Erstellungsdatum: 05.01.2024
Name: Christos Stamou
Matrikelnummer: k12306763
Beschreibung: Der Benutzer gibt eine Eingabe an, entweder in Textform oder Morse-Code-Form. Je nachdem, welche Eingabe er verwendet, 
wird entweder die Text-in-Morse-Code-Umwandlung oder die Morse-Code-in-Text-Umwandlung durchgeführt. Alle Übersetzungen basieren auf der gegebenemn Code-Tabelle. 
"""

# Morse-Code Tabelle
code_table = {
    '.-':'a',
    '-...':'b',
    '-.-.':'c',
    '-..':'d',
    '.':'e',
    '..-.':'f',
    '--.':'g',
    '....':'h',
    '..':'i',
    '.---':'j',
    '-.-':'k',
    '.-..':'l',
    '--':'m',
    '-.':'n',
    '---':'o',
    '.--.':'p',
    '--.-':'q',
    '.-.':'r',
    '...':'s',
    '-':'t',
    '..-':'u',
    '...-':'v',
    '.--':'w',
    '-..-':'x',
    '-.--':'y',
    '--..':'z',
    '.-.-':'ä',
    '---.':'ö',
    '..--':'ü',
    '.-.-.-':'.',
    '----':'ch',
    '-.-.--':'!',
    '.-..-.':'"',
    '.----':'1',
    '..---':'2',
    '...--':'3',
    '....-':'4',
    '.....':'5',
    '-....':'6',
    '--...':'7',
    '---..':'8',
    '----.':'9',
    '-----':'0',
    '---...':':',
    '--..--':',',
    '/':' ',  # Wortabstand
    '':''     # kein Text
}

#Text basierend auf der gegebenen Tabelle in Morse-Code umgewandelt.
def text_to_morse(text):
    morse_code = ''
    for char in text.lower():
        if char == ' ':
            morse_code += '/ '  # Wortabstand
        elif char in code_table.values():
            morse_code += [code for code, letter in code_table.items() if letter == char][0] + ' '
        else:
            morse_code += char  # Füge unbekannte Zeichen unverändert hinzu
    return morse_code.strip()

#Morse-Code wieder in einen lesbaren Text umgewandelt. 
def morse_to_text(morse_code):
    words = morse_code.split(' / ')
    decoded_text = ''
    for word in words:
        morse_chars = word.split(' ')
        for morse_char in morse_chars:
            if morse_char in code_table:
                decoded_text += code_table[morse_char]
            else:
                decoded_text += morse_char  # Füge unbekannte Zeichen unverändert hinzu
        decoded_text += ' '
    return decoded_text.strip()

#Hauptprogramm verlangt kontinuierlich nach weiteren Eingaben, bis es vom Benutzer beendet wird. 
def main():
    while True:
        try:
            choice = input("Möchten Sie Text in Morse-Code umwandeln (1) oder Morse-Code in Text (2) eingeben? (q zum Beenden): ")

            if choice.lower() == 'q':
                print("Programm beendet.")
                break

            if choice == '1':
                user_input = input("Geben Sie einen Text ein: ")
                morse_result = text_to_morse(user_input)
                print(f"Morse-Code: {morse_result}")

            elif choice == '2':
                user_input_morse = input("Geben Sie den Morse-Code ein: ")
                text_result = morse_to_text(user_input_morse)
                print(f"Decodierter Text: {text_result}")

            else:
                print("Ungültige Auswahl. Bitte wählen Sie 1, 2 oder q.")

        except Exception as e:
            print(f"Fehler: {e}. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()
