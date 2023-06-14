Data wykonania: 14.06.2023 r.
Autor: Julia Antoniak

## A ##
Uruchomienie skryptu po stronie użytkownika A daje do wyboru opcje:
- wygenerowania nowego klucza RSA
- podpisania i wysłania plików (jedna akcja)
- zakończenia programu

Opcja wysłania plików otwiera drugie menu gdzie wybieramy plik do podpisu i wysłania (lub też kończymy program).

## B ##
Uruchomienie skryptu po stronie B daje do wyboru opcje:
- sprawdzenie poprawności, autentyczności wybranego pliku (z tych, które już istnieją w folderze z otrzymanymi plikami)
- zakończenie programu

#######
Przed rozpoczęciem programu możliwe jest usunięcie ZAWARTOŚCI folderów:
- A/keys (ale następnie należy wygenerować nowe !!)
- A/signatures
- B/received_files
- B/received_signatures


######## DZIAŁANIE PROGRAMU ########
Generowanie kluczy RSA:
- na podstawie ciągu bitów trng tworzone są liczby pierwsze p i q; 
- na podsatwie p i q tworzone są inne liczby (e, d, n) potrzebne do wygenerowania pary kluczy
- klucze zapiyswane są w odpowiednich plikach z rozszrzeniem .pem

Użytkownik A:
- do wyboru opcje wspomniane wcześniej
- generacja nowego klucza odświeża klucz takze dla użytkownika B (ten dostaje klucz publiczny)
- wybór pliku do wysłania powoduje:
    - generacje hasha pliku
    - generacje podpisu na podstawie hasha i klucza prywatnego
    - wysłanie pliku, podpisu do użytkownika B

Użytkownik B:
- do wyboru opcje wspomniane wcześniej
- wybór pliku do otwarcia powoduje:
    - generacje hasha pliku
    - odkodowanie podpisu kluczem publicznym użytkownika A
    - porównanie hashy tych dwóch plików; 
        - jeżeli są równe to plik jest zweryfikowany i otwiera się
        - jeśli plik został podmieniony to nie otwiera się i wyświetlony jest odpowiedni komunikat