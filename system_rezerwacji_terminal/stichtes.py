from meat import *

if __name__ == '__main__':
    print('stitches.py script runs')


def input_anuluj_rezerwacje():
    print('-' * 35)
    numer_do_anulowania = input('Podaj numer rezerwacji do anulowania:\n')
    return numer_do_anulowania

def zostan_menu():
    czy_zostac = True
    while czy_zostac:
        print(opcje)
        print('-' * 35)
        wybor = (input('Wybierz opcję z menu wpisując numer 1 - 6 i klikając \"Enter": \n'))
        if wybor in menu_indexes:
            sprawdz_wybor(wybor)

# GŁÓWNA FUNKCJA
def sprawdz_wybor(wybor):
    #ZALOGUJ:
    if  wybor == '1':
        if teatr.czy_klient_zalogowany:
                print('-' * 35)
                print(f'Już jesteś zalogowany jako {teatr.zalogowany_klient.nazwa_uzytkownika}!')
                print('-' * 35)
                zostan_menu()
        else:
            print('-' * 35)
            nazwa_uzytkownika = input('Podaj nazwę użytkownika:\n')
            print('-' * 35)
            haslo = input('Podaj hasło:\n')
            teatr.zaloguj(nazwa_uzytkownika, haslo)
            if teatr.czy_klient_zalogowany:
                print('-' * 35)
                print(f'\nKlient zalogowany:\nImię: {teatr.zalogowany_klient.imie}\nNazwa użytkownika: {teatr.zalogowany_klient.nazwa_uzytkownika}')
                print('-' * 35)
            zostan_menu()
    #ZAREJESTRUJ
    elif wybor == '2':
        if teatr.czy_klient_zalogowany:
            print('-' * 35)
            print('Jesteś zalogowany. Aby zarejestrować nowego klienta wyloguj się lub zresetuj program!')
            print('-' * 35)
            zostan_menu()
        else:
            while True:
                print('-' * 35)
                imie = input('Podaj imię:\n').strip(' ')
                if 2 <= len(imie) < 25 and imie.isalpha():
                    break
                else:
                    print('-' * 35)
                    print("Imię musi mieć co najmniej 2 i maks 25 znaków:")
            while True:
                print('-' * 35)
                nazwisko = input('Podaj nazwisko:\n').strip(' ')
                if 2 <= len(nazwisko) <= 25 and imie.isalpha():
                    break
                else:
                    print('-' * 35)
                    print("Nazwisko musi mieć co najmniej 2 i maks 25 znaków:")
            while True:
                print('-' * 35)
                nazwa_uzytkownika = input('Stwórz swoją nazwę użytkownika:\n').strip(' ')
                if 2 <= len(nazwa_uzytkownika) <= 25:
                    break
                else:
                    print('-' * 35)
                    print("Nazwa użytkownika musi mieć co najmniej 2 i maks 25 znaków:")
            while True:
                print('-' * 35)
                haslo = input('Stwórz swoje hasło:\n')
                if 6 <= len(haslo) <= 25:
                    break
                else:
                    print('-' * 35)
                    print("Hasło musi być dluższe niż 5 znaków i krótsze niż 50:")
            if teatr.rejestruj(imie, nazwisko, nazwa_uzytkownika, haslo) == 10:
                print('-' * 35)
                print('Nazwa użykownika już zajęta. Wymyśl inną!')
                print('-' * 35)
                zostan_menu()
            print('-' * 35)
            print('Klient zarejestrowany!')
            print('-' * 35)
            zostan_menu()
    #POKAŻ WOLNE MIEJSCA
    elif wybor == '3':
        teatr.pokaz_wolne()
        print('-' * 35)
    #REZERWACJA MIEJSCA
    elif wybor == '4':
        if not teatr.czy_klient_zalogowany:
            print('-' * 35)
            print('Zanim zarezerwujesz miejsce musisz się zalogować.')
            print('-' * 35)
            zostan_menu()
        else:
            print('-' * 35)
            print('\nPodaj numer miejsca, które chcesz zarezerwować:\n')

            print('')
            while True:
                try:
                    nr_miejsca_do_rezerwwacji = int(input())
                    assert 1 <= nr_miejsca_do_rezerwwacji <= teatr.liczba_miejsc_w_pliku
                    break
                except (AssertionError, ValueError):
                    print('-' * 35)
                    print(f'Podaj prawidłowy numer miejsca: 1 - {teatr.liczba_miejsc_w_pliku}')
            teatr.rezerwacja(nr_miejsca_do_rezerwwacji)
            zostan_menu()
    #POKAZ MOJE REZERWACJE
    elif wybor == '5':
        print('-' * 35)
        print('       Oto twoje rezerwacje:')
        teatr.pokaz_rezerwacje()
    #ANULUJ REZERWACJE
    elif wybor == '6':
        if not teatr.czy_klient_zalogowany:
            print('-' * 35)
            print('Zanim anulujesz rezerwacje musisz się zalogować.')
            print('-' * 35)
            zostan_menu()
        else:
            print('-' * 35)
            print('\nPodaj numer rezerwacji, którą chcesz anulować:\n')
            while True:
                try:
                    nr_rezerwacji_do_anulacji = int(input())
                    assert 0 <= nr_rezerwacji_do_anulacji <= int(len(teatr.rezerwacje)) + 1
                    break
                except (AssertionError, ValueError):
                    print('-' * 35)
                    print(f'Nieprawidłowy numer rezerwacji.\n Numer rezerwacji powinien składać się z samych cyfr.\n Sprawdź swój numer i spróbuj ponownie:')
            teatr.anuluj_rezerwacje(nr_rezerwacji_do_anulacji)
            zostan_menu()
    # WYLOGUJ
    elif wybor == '7':
        if not teatr.czy_klient_zalogowany:
            print('-' * 35)
            print('Nie jesteś zalogowany.')
            print('-' * 35)
            zostan_menu()
        else:
            teatr.wyloguj()
            print('-' * 35)
            print('Wylogowano.')
            print('-' * 35)
            zostan_menu()
    # WYLOGUJ
    elif wybor == '8':
        print('-' * 35)
        print('Dziękuję za skorzystanie z narzędzia do rezerwacji napisanego w wielkich trudach.')
        print('-' * 35)
        exit()

# teatr
teatr = Teatr()

# Początek interakcji
print('Witam w systemie rezerwacji - Teatr Nadbrzeże')
print('-' * 35)
menu = ['Menu:',
         '1.Zaloguj',
         '2.Zarejestruj',
         '3.Pokaż wolne miejsca',
         '4.Rezerwuj miejsce',
         '5.Pokaż moje rezerwacje',
         '6.Anuluj rezerwacje',
         '7.Wyloguj',
         '8.Zamknij']

opcje = str(menu).strip('[').strip(']').replace(',', '\n').replace('\'', '')
menu_indexes = ['1','2','3','4','5','6','7','8'] # musi byc w str ponieważ pozniej sprawdza input

zostan_menu()