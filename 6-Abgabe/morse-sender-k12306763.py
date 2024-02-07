"""
Dateiname: morse-sender-k12306763
Erstellungsdatum: 07.02.2024
Name: Christos Stamou
Matrikelnummer: k12306763
Beschreibung: Das Python-Programm ermöglicht die bidirektionale Kommunikation von Text und Morse-Code über die 
serielle Schnittstelle (COM3, 115200 Baud) mit einem Arduino. Es verwendet eine Morse-Code-Tabelle für die Umwandlung
und enthält Funktionen für die Umwandlung von Text in Morse-Code (text_to_morse), Morse-Code in Text (morse_to_text) und
den Versand von Morse-Code über die serielle Schnittstelle (send_morse_code_via_serial). Der Benutzer kann zwischen diesen
Optionen wählen und das Programm endet durch Eingabe von 'q'. Bei Fehlern wird eine Fehlermeldung angezeigt, und das Programm wird fortgesetzt. 
"""

import serial
import time

# Morse-Code Tabelle (gleich wie vorher)
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

def send_morse_code_via_serial(morse_code):
    with serial.Serial('COM3', 115200, timeout=1) as ser:
        for char in morse_code:
            if char == '.':
                ser.write(b'.')
                time.sleep(0.25)
            elif char == '-':
                ser.write(b'-')
                time.sleep(0.75)
            elif char == ' ':
                time.sleep(0.25)

        time.sleep(2)  # Wait time for the Arduino execution
                

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
                send_morse_code_via_serial(morse_result)

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
