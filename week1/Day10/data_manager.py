class DataManager:
    def __init__(self, filename="data.txt"):
        self.filename = filename
        self.data = []
    def save_data(self):
        with open(self.filename, "w") as f:
            for item in self.data:
                f.write(str(item) + "\n")
    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                self.data = [line.strip() for line in f]
        except FileNotFoundError:
            pass
manager = DataManager()
manager.load_data()
print(manager.data)
