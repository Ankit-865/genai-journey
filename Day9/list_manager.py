# day9_list_manager.py
class ListManager:
    def __init__(self):
        self.my_list = []
    def add_item(self, item):
        self.my_list.append(item)
    def get_list(self):
        return self.my_list
manager = ListManager()
manager.add_item("apple")
print(manager.get_list())  