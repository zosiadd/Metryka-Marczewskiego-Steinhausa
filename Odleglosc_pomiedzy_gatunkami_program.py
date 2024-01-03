'''
Zadanie dotyczy metryki Marczewskiego-Steinhausa, wykorzystywanej w naukach
przyrodniczych. Wykonany program ma polegać na obliczaniu macierzy odległości między
kolekcjami, odszukanie najbardziej oddalonych par kolekcji i mających tą samą zawartość.
Do obliczenia odległości wykorzystujemy ułamek, w którego mianowniku jest łączna suma
zbiorów, a w liczniku różnica tych zbiorów. Danymi są między innymi : rodzaje murz oraz gatunki
roślin danych ekosystemów.
'''
data = []
# Otwarcie pliku tekstowego, odczytanie go, linijka po linicjce
with open ('Morza.txt', 'r') as file:
    for line in file:
        collection = []
        species = line.split(',') #kazdy gatunek (element) jest od siebie odzielony przecinkiem
        for s in species:
            s = s.strip()
            collection.append(s)
        data.append(collection)

results = []
biggest_difference = 0
biggest_difference_list = []
same_collections = []

#Przechodzimy teraz do stworzenia macierzy odległości - w niej znajdują się odległości między kolekcjami
for i in range(len(data)):
    row = [] #ilość rzędów w macierzy będzie odpowiadała ilości zbiorów w pliku z danymi wejściowymi
    for j in range(len(data)):
        set_i = set(data[i])
        set_j = set(data[j])
        factor = len(set_i ^ set_j)/len(set_i | set_j)
        row.append(f'{round(factor, 3):.3f}')#Zaokrąglenie wyników odległości do 3 miejsc po przecinku, wyświetlenie wyników w macierzy do 3 miejsc po przecinków

#Odszukanie par kolekcji o największym zróżnicowaniu( największej odległości)
        if factor > biggest_difference:
            biggest_difference_list = [(i + 1, j + 1)]
            biggest_difference = factor
        elif factor == biggest_difference:
            if (j + 1, i + 1) not in biggest_difference_list:
                biggest_difference_list.append((i + 1, j + 1))

#Odszukanie par kolekcji o tej samej zawartości
        if factor == 0:
            if i != j and not (j + 1, i + 1) in same_collections:
                same_collections.append((i + 1, j + 1))
    results.append(row)

#Wydrukowanie komunikatów o rezultatach, największym zróżnicowaniu między kolekcjami, oraz jeśli istnieją zbiory o tych samych koleckcjach
for r in results:
    print(r)

print('')
for elem in biggest_difference_list:
    print(f'Największe zróżnicowanie występuje pomiędzy zbiorami: {elem[0]} i {elem[1]}')

if same_collections:
    print('')
    for elem in same_collections:
        print(f'Zbiory {elem[0]} oraz {elem[1]} są takie same')