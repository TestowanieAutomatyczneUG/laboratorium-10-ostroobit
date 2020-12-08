class NotesStorage:
    def __init__(self):
        self.notes = []
    def add(self, note):
        pass
    def clear(self):
        pass
    def get_all_notes_of(self, name):
        pass

class NotesService:
    def __init__(self):
        self.storage = NotesStorage()
        
    def add(self, note):
        self.storage.add(note)
    
    def average_of(self, name):
        notes = self.storage.get_all_notes_of(name)
        if len(notes) != 0:
            res = 0
            for note in notes:
                res += note.note
            return res/len(notes)
        else:
            raise Exception
    
    def clear(self):
        self.storage.clear()
