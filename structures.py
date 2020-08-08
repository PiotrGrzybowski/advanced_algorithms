from typing import TypeVar, Generic, List

T = TypeVar('T')


class EmptyQueueError(Exception):
    def __init__(self):
        super().__init__('You cannot pop from empty queue')


class Queue(Generic[T]):
    def __init__(self):
        self.values: List[T] = []

    def push(self, value: T):
        self.values.append(value)

    def pop(self) -> T:
        if self.values:
            return self.values.pop(0)
        else:
            raise EmptyQueueError()

    def front(self) -> T:
        return self.values[0]

    def __str__(self) -> str:
        return f"[{', '.join([str(value) for value in self.values])}]"

    def __len__(self) -> int:
        return len(self.values)
