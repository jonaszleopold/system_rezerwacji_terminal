import datetime as datetime
import json

if __name__ == '__main__':
    print('meat.py script runs')


class MiejsceTeatralne:
    def __init__(self, nr_miejsca, rzad, czy_wolne, cena, czy_dla_niepelnosprawnych, czy_vip, id_klienta):
        self.nr_miejsca = nr_miejsca
        self.rzad = rzad
        self.czy_wolne = czy_wolne
        self.cena = cena
        self.czy_dla_niepelnosprawnych = czy_dla_niepelnosprawnych
        self.czy_vip = czy_vip
        self.id_klienta = id_klienta

    def informacje(self):
        print('-'*35)
        print(f'Numer miejsca: {self.nr_miejsca},\nRząd: {self.rzad},\nCena: {self.cena}PLN')
        if not self.czy_wolne:
            print('Miejsce zajęte\n')
        if self.czy_vip:
            print('Ekskluzywne miejsce VIP w pierwszym rzędzie!\n')
        if self.czy_dla_niepelnosprawnych:
            print('Miejsce z dodatkowymi udogodnieniami dla osób niepełnosprawnych.\n')


class MiejsceZwykle(MiejsceTeatralne):
    def __init__(self, nr_miejsca, rzad, czy_wolne, cena, czy_dla_niepelnosprawnych, czy_vip, id_klienta):
        MiejsceTeatralne.__init__(self, nr_miejsca, rzad, czy_wolne, cena, czy_dla_niepelnosprawnych, czy_vip,
                                  id_klienta)


class MiejsceVip(MiejsceTeatralne):
    def __init__(self, nr_miejsca, rzad, czy_wolne, cena, dodatkowa_oplata, czy_dla_niepelnosprawnych, czy_vip,
                 id_klienta):
        MiejsceTeatralne.__init__(self, nr_miejsca, rzad, czy_wolne, cena, czy_dla_niepelnosprawnych, czy_vip, id_klienta)
        self.dodatkowa_oplata = 80
        self.cena = cena + self.dodatkowa_oplata

    def zamow_podwozke(self):
        answer = input('Zarezerwowałeś miejsce VIP. Czy chcesz aby przyjechał po ciebie transport, który zabierze cię na spektakl? Y/N\n')
        expected_answers_yes = ['Y','y','Yes','YES','yes','YEs','YeS','yEs','yeS']
        expected_answers_no = ['N','n','No','NO','no']
        while answer not in expected_answers_yes and answer not in expected_answers_no:
            answer = input('Odpowiedz Y lub N:\n')
        if answer in expected_answers_yes:
            podjazd = r'''
                                          _.-="_-         _
                             _.-="   _-          | ||"""""""---._______     __..
                 ___.===""""-.______-,,,,,,,,,,,,`-''----" """""       """""  __'
          __.--""     __        ,'                   o \           __        [__|
     __-""=======.--""  ""--.=================================.--""  ""--.=======:
    ]       [///] : /        \ : |========================|    : /        \ :  [w] :
    V___________:|          |: |========================|    :|          |:   _-"
     V__________: \        / :_|=======================/_____: \        / :__-"
     -----------'  "-____-"  `-------------------------------'  "-____-"
    
            '''
            print(podjazd)
            print('-' * 35)
            print(f'Miejsce zarezerwowane. Pamiętaj też o dodatkowej opłacie wliczonej w cenę biletu:\n{self.dodatkowa_oplata}PLN')
            print('-' * 35)
        if answer in expected_answers_no:
            print('-' * 35)
            print('ok')
            print(f'Miejsce zarezerwowane. Pamiętaj o dodatkowej opłacie wliczonej w cenę biletu:\n{self.dodatkowa_oplata}PLN')
            print('-' * 35)



class MiejsceDlaNiepelnosprawnych(MiejsceTeatralne):
    def __init__(self, nr_miejsca, rzad, czy_wolne, cena, czy_dla_niepelnosprawnych, czy_vip, id_klienta,
                 dodatkowe_udogodnienia):
        MiejsceTeatralne.__init__(self, nr_miejsca, rzad, czy_wolne, cena, czy_dla_niepelnosprawnych, czy_vip, id_klienta)
        self.dodatkowe_udogodnienia = dodatkowe_udogodnienia

    def zamow_udogodnienia(self):
        answer = input(
            'Zarezerwowałeś miejsce z udogodnieniami dla osób niepełnosprawnych. Czy potrzebujesz zarezerwować miejsce parkingowe z łatwym dostępem? Y/N')
        expected_answers_yes = ['Y', 'y', 'Yes', 'YES', 'yes', 'YEs', 'YeS', 'yEs', 'yeS']
        expected_answers_no = ['N', 'n', 'No', 'NO', 'no']
        while answer not in expected_answers_yes and answer not in expected_answers_no:
            answer = input('Odpowiedz Y lub N')
        if answer in expected_answers_yes:
            print('-' * 35)
            print('Parking zarezerwowany! Numer miejsca parkingowego to A24.')
            print('-' * 35)
        if answer in expected_answers_no:
            print('-' * 35)

        answer2 = input('Czy potrzebujesz asystenta, który pomoże ci się poruszać po teatrze? Y/N')
        while answer2 not in expected_answers_yes and answer2 not in expected_answers_no:
            answer2 = input('Odpowiedz Y lub N')
        if answer2 in expected_answers_yes:
            print('-' * 35)
            print('Asystent będzie czekał na ciebie w recepcji teatru.')
            print('-' * 35)
        if answer2 in expected_answers_no:
            print('-' * 35)
        print(f'Miejsce zarezerwowane!')
        print('-' * 35)


class Klient:
    def __init__(self, id_klienta, nazwa_uzytkownika, _haslo, imie, nazwisko):
        self.id_klienta = id_klienta
        self.nazwa_uzytkownika = nazwa_uzytkownika
        self.haslo = _haslo
        self.imie = imie
        self.nazwisko = nazwisko

class Rezerwacja:
    def __init__(self, nr_rezerwacji, nr_miejsca, id_klienta, data_rezerwacji, czy_anulowana, data_anulacji):
        self.nr_rezerwacji = nr_rezerwacji
        self.nr_miejsca = nr_miejsca
        self.id_klienta = id_klienta
        self.data_rezerwacji = data_rezerwacji
        self.czy_anulowana = czy_anulowana
        self.data_anulacji = data_anulacji


class Teatr:
    def __init__(self):
        self.zalogowany_klient = None

    # ładowanie danych:
    # ładuje pliki do zmiennych
    dane_z_pliku_klienci = open('klienci.json', 'r')
    dane_z_pliku_miejsca = open('miejsca.json', 'r')
    dane_z_pliku_rezerwacje = open('rezerwacje.json', 'r')

    # ładuje dane z plików do list
    wszyscy_klienci_z_pliku = json.load(dane_z_pliku_klienci)
    wszystkie_miejsca_z_pliku = json.load(dane_z_pliku_miejsca)
    wszystkie_rezerwacje_z_pliku = json.load(dane_z_pliku_rezerwacje)

    # tworzy zmienna ktora mówi ile jest zapisów w danym pliku - nie zamieniać na range bo jest używane do nadawania id
    liczba_klientow_w_pliku = len(wszyscy_klienci_z_pliku)
    liczba_miejsc_w_pliku = len(wszystkie_miejsca_z_pliku)
    liczba_rezerwacji_w_pliku = len(wszystkie_rezerwacje_z_pliku)

    # miejsca:
    # tworze liste z obiektami klasy 'MiejsceTeatralne' i dziedziczących klas
    miejsca_w_teatrze = []
    for i in range(liczba_miejsc_w_pliku):
        if wszystkie_miejsca_z_pliku[i]['czy_vip']:
            miejsca_w_teatrze.append(MiejsceVip(**wszystkie_miejsca_z_pliku[i]))
        elif wszystkie_miejsca_z_pliku[i]['czy_dla_niepelnosprawnych']:
            miejsca_w_teatrze.append(MiejsceDlaNiepelnosprawnych(**wszystkie_miejsca_z_pliku[i]))
        elif wszystkie_miejsca_z_pliku[i]['czy_dla_niepelnosprawnych'] == False and wszystkie_miejsca_z_pliku[i][
            'czy_vip'] == False:
            miejsca_w_teatrze.append(MiejsceZwykle(**wszystkie_miejsca_z_pliku[i]))

    # klient:
    # tworząc obiekt teatr tworze liste z obiektami klasy 'Klient' na podstawie danych z listy stworzonej z pliku klienci
    klienci = []
    for i in range(liczba_klientow_w_pliku):
        klienci.append(Klient(**wszyscy_klienci_z_pliku[i]))
    # ustawiamy klienta jako nie zalogowanego
    czy_klient_zalogowany = False
    # id dla nowych klientow to dlugosc listy klienci.json + 1
    id_nowy_klient = liczba_klientow_w_pliku
    # id dla nowych rezerwacji podobnie jak wyżej
    id_nowa_rezerwacja = liczba_rezerwacji_w_pliku

    rezerwacje = []
    for i in range(liczba_rezerwacji_w_pliku):
        rezerwacje.append(Rezerwacja(**wszystkie_rezerwacje_z_pliku[i]))


    def pokaz_wolne(self):
        for i in range(self.liczba_miejsc_w_pliku):
            if self.miejsca_w_teatrze[i].czy_wolne:
                self.miejsca_w_teatrze[i].informacje()

    def zaloguj(self, nazwa_uzytkownika, _haslo):
        for i in range(len(self.klienci)):
            if nazwa_uzytkownika == self.klienci[i].nazwa_uzytkownika and _haslo == self.klienci[i].haslo:
                # updejtuje obiekt zalogowanego klienta
                self.zalogowany_klient = Klient(self.klienci[i].id_klienta,
                                                self.klienci[i].nazwa_uzytkownika,
                                                self.klienci[i].haslo,
                                                self.klienci[i].imie,
                                                self.klienci[i].nazwisko)
                self.czy_klient_zalogowany = True
                break
        else:
            print('-' * 35)
            print('Błędna nazwa uzytkownika lub hasło.')
            print('-' * 35)

    def wyloguj(self):
        self.czy_klient_zalogowany = False


    def rejestruj(self, imie, nazwisko, stworz_nazwa_uzytkownika, stworz_haslo):
        for i in range(self.liczba_klientow_w_pliku):
            if stworz_nazwa_uzytkownika == self.klienci[i].nazwa_uzytkownika:
                return 10
        if not self.czy_klient_zalogowany:
            # tworzy zalogowanego klienta i dodaje go do listy obiektów klienci. Zmienia też status logowania na True
            self.zalogowany_klient = Klient(self.id_nowy_klient, stworz_nazwa_uzytkownika, stworz_haslo, imie,
                                            nazwisko)
            self.czy_klient_zalogowany = True
            self.klienci.append(self.zalogowany_klient)
            # tworzy dict object klienta
            dict_nowy_klient = {
                "id_klienta": self.id_nowy_klient,
                "nazwa_uzytkownika": stworz_nazwa_uzytkownika,
                "_haslo": stworz_haslo,
                "imie": imie,
                "nazwisko": nazwisko
            }

            # dodaje dict klienta do listy wszystkich klientów i zapisuje klientów wraz z nowym klientem:
            with open('klienci.json', 'w', encoding='UTF8') as outfile_klienci:
                self.wszyscy_klienci_z_pliku.append(dict_nowy_klient)
                outfile_klienci.write(json.dumps(self.wszyscy_klienci_z_pliku, indent=3))

    def rezerwacja(self, nr_wpisany_miejsca):
        czas_rejestracji = get_date_and_time()
        if self.czy_klient_zalogowany:
            # sprawdza czy nr miejsce jest wolne
            if self.miejsca_w_teatrze[nr_wpisany_miejsca - 1].czy_wolne: # trzeba odjąć ze względu na elementy zaczynajace się od indeksu 0 do 39
                # tworzy dict object rezerwacji
                dict_nowa_rezerwacja = {
                    "nr_rezerwacji": self.id_nowa_rezerwacja,
                    "nr_miejsca": nr_wpisany_miejsca,
                    "id_klienta": self.zalogowany_klient.id_klienta,
                    "data_rezerwacji": czas_rejestracji,
                    "czy_anulowana": False,
                    "data_anulacji": ""
                }
                self.rezerwacje.append(Rezerwacja(self.id_nowa_rezerwacja, nr_wpisany_miejsca, self.zalogowany_klient.id_klienta, czas_rejestracji, False, ""))
                # dodaje dict rezerwacji do listy listy wszystkich_rezerwacji i zapisuje go do pliku:
                with open('rezerwacje.json', 'w', encoding='UTF8') as outfile_rezerwacje:
                    self.wszystkie_rezerwacje_z_pliku.append(dict_nowa_rezerwacja)
                    outfile_rezerwacje.write(json.dumps(self.wszystkie_rezerwacje_z_pliku, indent=3, default=str))

                # zaznacza, że miejsce nie jest wolne w pliku miejsca.json - teatr musi być reloadowany ponieważ zaciąga pliki w momencie tworzenia???
                with open('miejsca.json', 'w', encoding='UTF8') as outfile_miejsca:
                    self.wszystkie_miejsca_z_pliku[nr_wpisany_miejsca - 1]['czy_wolne'] = False
                    self.wszystkie_miejsca_z_pliku[nr_wpisany_miejsca - 1][
                        'id_klienta'] = self.zalogowany_klient.id_klienta
                    outfile_miejsca.write(json.dumps(self.wszystkie_miejsca_z_pliku, indent=3, default=str))

                self.id_nowa_rezerwacja += 1  # zeby tworzyc wiele rezerwacji na raz i nadawać im odpowiednie id
                self.miejsca_w_teatrze[nr_wpisany_miejsca - 1].czy_wolne = False

                if self.miejsca_w_teatrze[nr_wpisany_miejsca - 1].czy_vip:
                    self.miejsca_w_teatrze[nr_wpisany_miejsca - 1].zamow_podwozke()
                elif self.miejsca_w_teatrze[nr_wpisany_miejsca - 1].czy_dla_niepelnosprawnych:
                    self.miejsca_w_teatrze[nr_wpisany_miejsca - 1].zamow_udogodnienia()
                else:
                    print('-' * 35)
                    print(f'\nMiejsce {nr_wpisany_miejsca} zarezerwowane!\n')
                    print('-' * 35)
                    return 0
            else:
                print('-' * 35)
                print(f'\nMiejsce {nr_wpisany_miejsca} już zajęte!\n')
                print('-' * 35)
                return 20
        else:
            print('-' * 35)
            print('\nZanim zarezerwujesz miejsce musisz się zalogować.\n')
            print('-' * 35)


    def pokaz_rezerwacje(self):
        if self.czy_klient_zalogowany:
            for i in range(len(self.rezerwacje)):
                if self.zalogowany_klient.id_klienta == self.rezerwacje[i].id_klienta:
                    print(f'\nNumer rezerwacji: {self.rezerwacje[i].nr_rezerwacji}')
                    print(f'Numer miejsca: {self.rezerwacje[i].nr_miejsca}')
                    print(f'Data rezerwacji: {self.rezerwacje[i].data_rezerwacji}')
                    if self.rezerwacje[i].czy_anulowana:
                        print('Status: Anulowana')
                        print(f'Data anulowania: {self.rezerwacje[i].data_anulacji}')
                    if self.miejsca_w_teatrze[self.rezerwacje[i].nr_miejsca - 1].czy_vip:
                        print(f'Miejsce VIP w pierwszym rzędzie.')
                    elif self.miejsca_w_teatrze[self.rezerwacje[i].nr_miejsca - 1].czy_dla_niepelnosprawnych:
                        print(f'Miejsce z udogodnieniami dla osób z niepełnosprawnościami.')
                    print('-'*35)
        else:
            print('-' * 35)
            print('Zanim zobaczysz swoje rezerwacje musisz się zalogować!')
            print('-' * 35)


    def anuluj_rezerwacje(self, numer_rezerwacji_do_anulowania):
        czas_anulacji = get_date_and_time()
        if self.czy_klient_zalogowany:
            # porównuje id obiektu klienta z id klienta w liscie z numerami rezerwacji, jesli sie zgadza to nadpisuje element 'czy_anulowane'
            try:
                for i in range(len(self.wszystkie_rezerwacje_z_pliku)):
                    if self.zalogowany_klient.id_klienta == self.rezerwacje[i].id_klienta and numer_rezerwacji_do_anulowania == self.rezerwacje[i].nr_rezerwacji:
                        self.wszystkie_rezerwacje_z_pliku[i]['czy_anulowana'] = True
                        self.wszystkie_rezerwacje_z_pliku[i]['data_anulacji'] = czas_anulacji

                        with open('rezerwacje.json', 'w', encoding='UTF8') as outfile_rezerwacje:
                            outfile_rezerwacje.write(json.dumps(self.wszystkie_rezerwacje_z_pliku, indent=3, default=str))

                        with open('miejsca.json', 'w', encoding='UTF8') as outfile_miejsca:
                            miejsce_do_zmiany = self.wszystkie_miejsca_z_pliku[self.wszystkie_rezerwacje_z_pliku[i]['nr_miejsca'] - 1]
                            miejsce_do_zmiany['czy_wolne'] = True
                            miejsce_do_zmiany['id_klienta'] = 0
                            outfile_miejsca.write(json.dumps(self.wszystkie_miejsca_z_pliku, indent=3, default=str))

                        self.rezerwacje[i].czy_anulowana = True
                        self.rezerwacje[i].data_anulacji = czas_anulacji
                        print('-' * 35)
                        print('Rezerwacja anulowana!')
                        print('-' * 35)
                        return 0
            except:
                print('-' * 35)
                print('Bledny numer rezerwacji!')
                print('-' * 35)
                return 31
        else:
            print('-' * 35)
            print('Użytkownik nie zalogowany z ID (ANULACJA)')
            print('-' * 35)
            return 32


def get_date_and_time():
    data_czas = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
    return data_czas