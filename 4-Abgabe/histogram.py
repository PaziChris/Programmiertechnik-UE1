# -*- coding: utf-8 -*-
"""

Dieses Programm zählt Buchstabem und Wörter in einem Text,
sieht aber ein zusätzliches Argument vor, nämlich eine Liste von Zeichen,
die ignoriert werden sollen. Somit können Satzzeichen aus der Zählung gestrichen werden.

Brauchen pyserial dafür, wie in erste stunde heruntergeladen. Siehe pypi.org -> pyserial. bei pythonpath mnager inkludieren.
ganz rechte symbol. 

"""

def count_letters(text,skip=''):
    """
    Zählt Buchstaben
    """
    histogram = {} 

    for letter in text:
        if letter in skip:
            continue
        if letter not in histogram:
            histogram[letter] = 1
            continue
        histogram[letter] += 1
    return histogram

def count_words(text,skip=''):
    """f
    Zählt Wörter
    """
    histogram = {}
    lastposition = 0
    for position,letter in enumerate(text):
        if not letter.isspace() and letter not in skip:
            continue
        if position == lastposition:
            lastposition += 1
            continue
        word = text[lastposition:position]
        lastposition = position + 1
        if word not in histogram:
            histogram[word] = 1
            continue
        histogram[word] += 1
    if len(text) > lastposition:
        word = text[lastposition:] 
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1

    return histogram

def sort_by_key(item):
    return item[0]

def sort_by_count(item):
    return item[1]

def print_histogram(histogram,kind,maxshow = None,descending = True,sort_by=sort_by_key):
    # zum selber überlegen: soll auf kongsole ausgeben und nix
    # zurück liefedrn
    print("{0} Histogram\n===============\n{0}:\t\tHäufigkeit:\n-------------------".format(kind))
    for key,wert in sorted(histogram.items(),key=sort_by,reverse=descending)[:maxshow]:
        print("{}:\t{}".format(key,wert))
    
def main():
    text = input("Geben sie bitte einene text ein:")
    if len(text) <= 1:
        print("empty text")
    else:
        letterhistogram = count_letters(text)
        print_histogram(letterhistogram,"Zeichen")
        wordhistogram = count_words(text)
        print_histogram(wordhistogram,"Wort",sort_by=sort_by_count)
            
if __name__ == "__main__":
    main()
