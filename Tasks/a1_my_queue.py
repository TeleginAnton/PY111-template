"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        self._list = []  # todo для очереди можно использовать python list

    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self._list.append(elem)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        return self._list.pop(0) if self._list else None

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        return self._list[ind] if ind < len(self._list) else None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self._list.clear()
