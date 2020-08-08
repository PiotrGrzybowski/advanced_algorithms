from typing import TypeVar, Generic, List

T = TypeVar('T')


class EmptyQueueError(Exception):
    def __init__(self):
        super().__init__('You cannot pop from empty queue')


class Queue(Generic[T]):
    def __init__(self):
        self.values: List[T] = []

    def push(self, value: T):
        pass

    def pop(self) -> T:
        pass

    def front(self) -> T:
        pass

    def __str__(self) -> str:
        pass

    def __len__(self) -> int:
        pass
