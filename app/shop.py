from app.abstract import BaseStorage
from app.exceptions import NotEnoughSpace


class Shop(BaseStorage):
    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, quantity):
        if self.get_free_space() - self.items[name] <= 0 or not self.get_unique_items_count():
            raise NotEnoughSpace
        else:
            self.items[name] += quantity

    def remove(self, name, quantity):
        self.items[name] -= quantity

    def get_free_space(self) -> int:
        return self.capacity - sum(self.items.values())

    def get_items(self) -> dict:
        return self.items

    def get_unique_items_count(self):
        if len(self.items) < 5:
            return True
