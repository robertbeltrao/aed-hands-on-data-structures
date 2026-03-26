from src.array import Array


class MyArray(Array):
    """
    Implementação concreta do TAD Array.
    """

    def __init__(self) -> None:
        self.data: list[int] = []

    def append(self, value: int) -> None:
        raise NotImplementedError

    def get(self, index: int) -> int:
        raise NotImplementedError

    def set(self, index: int, value: int) -> None:
        raise NotImplementedError

    def remove(self, value: int) -> None:
        raise NotImplementedError

    def insert(self, index: int, value: int) -> None:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __getitem__(self, index: int) -> int:
        raise NotImplementedError

    def __setitem__(self, index: int, value: int) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError
