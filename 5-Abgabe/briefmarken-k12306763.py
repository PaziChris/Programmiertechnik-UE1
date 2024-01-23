"""
Dateiname: briefmarken-k12306763
Erstellungsdatum: 23.01.2024
Name: Christos Stamou
Matrikelnummer: k12306763
Beschreibung: 

Das Programm bestimmt rekursiv und iterativ alle möglichen Euro-Werte, 
die mit einer bestimmten Anzahl von Briefmarken (bis zu einer festgelegten maximalen Anzahl) dargestellt werden können. 
Die Euro-Werte sind als Summe von Briefmarkenwerten aus einer globalen Liste vorgegeben. Das Ergebnis sind eindeutige 
Kombinationen der Briefmarkenwerte, die die gewünschten Euro-Werte repräsentieren. In der Ausgabe werden diese Euro-Werte
für Kombinationen von 1 bis zur maximalen Anzahl von Briefmarken dargestellt, wobei Duplikate entfernt werden.
        
"""

def find_stamp_combinations(N, stamp_values):
    def find_combinations_recursive(target_value, remaining_stamps, current_combination, all_combinations):
        if target_value == 0:
            # Zielwert erreicht, füge aktuelle Kombination zur Ergebnisliste hinzu
            all_combinations.append(tuple(sorted(current_combination)))
            return
        if target_value < 0 or not remaining_stamps:
            # Zielwert nicht erreichbar oder keine Briefmarken mehr verfügbar
            return

        # Zielwert mit der aktuellen Briefmarke zu erreichen
        find_combinations_recursive(target_value - remaining_stamps[0], remaining_stamps,
                                    current_combination + [remaining_stamps[0]], all_combinations)

        # Zielwert ohne die aktuelle Briefmarke zu erreichen
        find_combinations_recursive(target_value, remaining_stamps[1:],
                                    current_combination, all_combinations)

    all_combinations = []
    for i in range(1, N + 1):
        find_combinations_recursive(i, stamp_values, [], all_combinations)

    return list(set(all_combinations))


if __name__ == '__main__':
    stamp_values = [0.3, 0.5, 0.8, 1, 1.5, 2, 5, 12]
    max_number_of_stamps = 5

    result = find_stamp_combinations(max_number_of_stamps, stamp_values)

    # set, um Duplikate zu entfernen
    unique_combinations = set(result)

    # Ausgabe Kombinationen
    print("Mit 1 bis {} Briefmarken darstellbare Werte:".format(max_number_of_stamps))
    for combination in unique_combinations:
        print(sum(combination), "Euro:", combination)

