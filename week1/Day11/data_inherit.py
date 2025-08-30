class BaseManager:
    def __init__(self, filename="base.txt"):
        self.filename = filename
    def save(self, data):
        with open(self.filename, "w") as f:
            f.write(str(data))

class ExtendedManager(BaseManager):
    def load(self):
        try:
            with open(self.filename, "r") as f:
                return f.read()
        except FileNotFoundError:
            return "No data"
ext = ExtendedManager()
ext.save("Test data")
print(ext.load())