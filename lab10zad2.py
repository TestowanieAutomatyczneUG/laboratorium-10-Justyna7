# Niech klasa o nazwie NotesStorage odpowiada za przechowywanie danych o ocenach z poprzedniego zadania. Klasa ta ma następujące metody:
#
# add(note) - dodanie oceny
# clear() - czyszczenie danych
# getAllNotesOf(name) - pobieranie wszystkich ocen osoby o nazwie name
# Następnie niech klasa NotesService odpowiada za obsługę programu bazując na klasie NotesStorage, która:
#
# Ma pole z klasy NotesStorage
# Posiada metodę o nazwie add(note), która wywołuje add z NotesStorage
# Posiada metodę o nazwie averageOf(name), która pobiera oceny korzystając z getAllNotesOf(name) i zwraca średnią arytmetyczną ocen
# Posiada metodę clear(), która odpala metodę clear() z NotesStorage.
# Napisz implementacje klasy NotesService (nie NotesStorage) i przeprowadź testy na napisanej implementacji.
#
# Rozwiązanie umieść w repozytorium pod adresem: https://classroom.github.com/a/uFsTkkjD
#
# Jako odpowiedź prześlij printscreen z przechodzenia testów oraz link do testów oraz napisanej klasy.





from lab10zad1 import Note
from unittest import TestCase, main
from unittest.mock import *


class NotesStorage:
    def add(self, note):
        return None

    def clear(self):
        return None

    def getAllNotesOf(self, name):
        return []


class NotesService:
    def __init__(self):
        self.notesStorage = NotesStorage()

    def add(self, note):
        self.notesStorage.add(note)

    def averageOf(self, name):
        all = self.notesStorage.getAllNotesOf(name)
        return round(sum(all)/len(all), 1)

    def clear(self):
        self.notesStorage.clear()


class test_NotesService(TestCase):
    def setUp(self):
        self.test_object = NotesService()

    def test_add(self):
        def sideEffect(arg):
            self.added = arg.get_note()
        # prepare mock time
        self.test_object.notesStorage.add = Mock(name='add')
        self.test_object.notesStorage.add.side_effect = sideEffect

        # testing
        self.added = None
        self.test_object.add(Note("Test", 2.7))
        self.assertEqual(2.7, self.added, 'No Notes added')

    def test_avrageOf(self):
        # prepare mock time
        self.test_object.notesStorage.getAllNotesOf = Mock(name='get notes of')
        self.test_object.notesStorage.getAllNotesOf.return_value = [2.4, 3.8, 5.2]

        # testing
        result = self.test_object.averageOf("aaa")
        self.assertEqual(round(3.8, 1), result, 'return value from played incorrect')

    def test_clear(self):
        def sideEffect():
            self.cleared = True
        # prepare mock time
        self.test_object.notesStorage.clear = Mock(name='Clear')
        self.test_object.notesStorage.clear.side_effect = sideEffect

        # testing
        self.cleared = False
        self.test_object.notesStorage.clear()
        self.assertEqual(True, self.cleared, 'clear was not called')


    def tearDown(self):
        self.test_object = None


if __name__ == '__main__':
    main()
