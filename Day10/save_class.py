class NoteTaker:
    def __init__(self, filename="notes.txt"):
        self.filename = filename
        self.notes = []
    def save_note(self, note):
        self.notes.append(note)
        with open(self.filename, "a") as f:
            f.write(note + "\n")
note_taker = NoteTaker()
note_taker.save_note("Meeting at 10 AM")
