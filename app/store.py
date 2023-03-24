from app.abstract import BaseStorage
from app.exceptions import *


class Store(BaseStorage):
    def __init__(self, items: dict, capacity=100):
        super().__init__(items, capacity)

    def add(self, name, quantity):
        self.items[name] += quantity

    def remove(self, name, quantity):
        if self.items[name] < quantity:
            raise NotEnoughGoods
        else:
            self.items[name] -= quantity

    def get_free_space(self) -> int:
        return self.capacity - sum(self.items.values())

    def get_items(self) -> dict:
        return self.items

    def get_unique_items_count(self):
        return len(self.items)
