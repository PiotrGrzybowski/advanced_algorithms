from unittest import TestCase, main

from structures import Queue, EmptyQueueError, Stack, EmptyStackError


class TestStack(TestCase):
    def test_push(self):
        stack = Stack[int]()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(len(stack.values), 3)
        self.assertEqual(stack.values[0], 1)
        self.assertEqual(stack.values[1], 2)
        self.assertEqual(stack.values[2], 3)

    def test_pop(self):
        stack = Stack[int]()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        popped = stack.pop()

        self.assertEqual(popped, 3)
        self.assertEqual(stack.values, [1, 2])

        stack.pop()
        stack.pop()

        self.assertRaises(EmptyStackError, stack.pop)

    def test_front(self):
        stack = Stack[int]()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.front(), 3)
        stack.pop()
        self.assertEqual(stack.front(), 2)

    def test_len(self):
        queue = Queue[int]()

        queue.push(1)
        queue.push(2)
        queue.push(3)

        self.assertEqual(len(queue), 3)

    def test_str(self):
        queue = Queue[int]()

        self.assertEqual(str(queue), '[]')

        queue.push(1)
        queue.push(2)
        queue.push(3)

        self.assertEqual(str(queue), '[1, 2, 3]')


if __name__ == '__main__':
    main()
