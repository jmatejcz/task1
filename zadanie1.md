### Model systemu bankowego
![alt text](model.png "Title")

Model składa się z następujących elementów:
- Użytkownik
    - Imie - string
    - Nazwisko - string
    - PESEL - obiekt
      - ograniczenia: zawiera tyko cyfry, zawiera dokładnie 11 znaków
    - Adres - obiekt 
      - Miasto - string
      - Ulica - string
      - Kod pocztowy - obiekt
        - ograniczenia: ma 2 cyrfy potem myslnik i 3 cyfry
      - numer bloku/domu - string

- Konto Bankowe
    - stan konta - float
    - numer konta - obiekt
      - ograniczemoa: składa sie tylko z cyfr i ma dokładnie 26 cyfr
    - karty - Lista obiektów karta
    - historia przelewów - lista obiektów przelew
    - lokaty - lista obiektów lokata

- Lokata
  - stan lokaty - float
  - start lokaty - data
  - koniec lokaty - data
  - oprocentowanie - float

- Przelew
  - tytuł - string
  - nadawca - obiekt nadawca
  - kwota - float
  - data - data

- Serwis autoryzacyjny odwołuje sie do bazy danych weryfikując wprowadze
przez użytkownika dane, jeżeli są poprawne udziela dostępy do konta.