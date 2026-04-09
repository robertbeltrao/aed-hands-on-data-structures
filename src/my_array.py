from src.array import Array


class MyArray(Array):

    def __init__(self) -> None:
        self.data = []

    def append(self, value: int) -> None:
        self.data.append(value)

    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.data):
            raise IndexError
        return self.data[index]

    def set(self, index: int, value: int) -> None:
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data[index] = value

    def remove(self, value: int) -> None:
        for i in range(len(self.data)):
            if self.data[i] == value:
                del self.data[i]
                return
        raise ValueError

    def insert(self, index: int, value: int) -> None:
        if index < 0 or index > len(self.data):
            raise IndexError
        self.data.insert(index, value)

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index: int) -> int:
        return self.get(index)

    def __setitem__(self, index: int, value: int) -> None:
        self.set(index, value)

    def __repr__(self) -> str:
        return str(self.data)