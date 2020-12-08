import unittest
from src.note import Note

class TestNote(unittest.TestCase):
    def test_name_None(self):
        with self.assertRaises(Exception):
            Note(None, 3)
    def test_name_empty(self):
        with self.assertRaises(Exception):
            Note("", 3)
    def test_note_less_than_2(self):
        with self.assertRaises(Exception):
            Note("witam", 1)
    def test_note_more_than_6(self):
        with self.assertRaises(Exception):
            Note("witam", 7)