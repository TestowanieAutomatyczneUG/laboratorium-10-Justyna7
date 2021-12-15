# Zadanie 1 (0.5 pkt)
#
# Napisz klasę Note, która będzie miała następujące właściwości:
#
# Będzie zawierała pola name (ciąg tekstowy) oraz note (liczba zmiennoprzecinkowa)
# Będzie posiadała konstruktor, w którym:
# Pole name nie może być null, w przeciwnym wypadku wyrzucić ma wyjątek;
# Pole name nie może być puste, w przeciwnym wypadku wyrzucić ma wyjątek;
# Pole note ma być w przedziale zamkniętym od 2 do 6, w przeciwnym przypadku ma wyrzucić wyjątek;
# Będzie posiadała tzw. gettery na pole name oraz note.
# Przetestuj wyżej napisaną klasę.
#
# Rozwiązanie umieść w repozytorium pod adresem: https://classroom.github.com/a/uFsTkkjD

from unittest import TestCase, main
from unittest.mock import *


class Note:
    def __init__(self, name, note):
        self.name = None
        self.note = None
        self.set_name(name)
        self.set_note(note)

    def set_name(self, name):
        if name is None:
            raise Exception
        elif isinstance(name, str):
            if name == "":
                raise Exception
            else:
                self.name = name
        else:
            raise Exception

    def set_note(self, note):
        if note is None:
            raise Exception
        elif isinstance(note, float):
            if 2 <= note <= 6:
                self.note = note
            else:
                raise Exception
        else:
            raise Exception

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note


class test_Note(TestCase):
    def test_getName(self):
        n = Note("Nazwa", 3.7)
        self.assertEqual(n.get_name(), "Nazwa")

    def test_getNote(self):
        n = Note("Nazwa", 3.7)
        self.assertEqual(n.get_note(), 3.7)

    def test_None(self):
        self.assertRaises(Exception, Note, None, None)

    def test_name_None(self):
        self.assertRaises(Exception, Note, None, 2.9)

    def test_note_None(self):
        self.assertRaises(Exception, Note, "None", None)

    def test_name_empty(self):
        self.assertRaises(Exception, Note, "", 2.9)

    def test_note_too_small(self):
        self.assertRaises(Exception, Note, "None", 0.7)

    def test_note_too_big(self):
        self.assertRaises(Exception, Note, "None", 40.9)

    def test_note_int(self):
        self.assertRaises(Exception, Note, "None", 3)

    def test_name_array(self):
        self.assertRaises(Exception, Note, [], 2.9)




if __name__ == '__main__':
    main()
