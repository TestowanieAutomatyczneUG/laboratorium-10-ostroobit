
class Note:
    def __init__(self, name, note):
        if not name or note < 2 or note > 6:
            raise Exception
        self.name = name
        self.note = note


