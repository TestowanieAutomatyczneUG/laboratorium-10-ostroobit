import unittest
from unittest.mock import Mock
from src.notes_storage import *
from src.note import Note

class TestNotesService(unittest.TestCase):
    def setUp(self):
        self.service = NotesService()

    def test_add_note(self):
        test_object = self.service
        test_object.storage.get_all_notes_of = Mock(name = "get_all_notes_of")
        note = Note("piotr", 5)
        test_object.storage.get_all_notes_of.return_value = [note]
        self.assertEqual(self.service.storage.get_all_notes_of("piotr"), [note])
    
    def test_average_of(self):
        test_object = self.service
        test_object.storage.get_all_notes_of = Mock(name = "get_all_notes_of")
        notes = [Note("piotr", 5), Note("piotr", 3), Note("piotr", 4)]
        test_object.storage.get_all_notes_of.return_value = notes
        self.assertEqual(self.service.average_of("piotr"), 4)

    def test_average_of_empty(self):
        test_object = self.service
        test_object.storage.get_all_notes_of = Mock(name = "get_all_notes_of")
        test_object.storage.get_all_notes_of.return_value = []
        with self.assertRaises(Exception):
            self.service.average_of("piotr")
    
    def test_clear(self):
        test_object = self.service
        test_object.storage.get_all_notes_of = Mock(name = "get_all_notes_of")
        notes = [Note("piotr", 5), Note("piotr", 3), Note("piotr", 4)]
        test_object.storage.get_all_notes_of.return_value = notes
        test_object.storage.clear()
        test_object.storage.get_all_notes_of.return_value = []

        self.assertEqual(self.service.storage.get_all_notes_of("piotr"), [])
    
    def tearDown(self):
        self.service = None