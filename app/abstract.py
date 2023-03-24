from abc import ABC, abstractmethod


class BaseStorage(ABC):
    def __init__(self, items: dict, capacity: int):
        self.items = items
        self.capacity = capacity

    @abstractmethod
    def add(self, name, quantity) -> None:
        ...

    @abstractmethod
    def remove(self, name, quantity) -> None:
        ...

    @abstractmethod
    def get_free_space(self) -> int:
        ...

    @abstractmethod
    def get_items(self) -> dict:
        ...

    @abstractmethod
    def get_unique_items_count(self) -> int:
        ...
