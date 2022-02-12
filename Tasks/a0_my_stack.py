"""
My little Stack
"""
from typing import Any


class Stack:
    def __init__(self):
        self._stack = []  # todo для стека можно использовать python list

    def push(self, elem: Any) -> None:
        """
        Operation that add element to stack

        :param elem: element to be pushed
        :return: Nothing
        """
        self._stack.append(elem)
        print(elem)

    def pop(self) -> Any:
        """
        Pop element from the top of the stack. If not elements - should return None.

        :return: popped element
        """
        if self._stack:
            return self._stack.pop()

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the stack without popping it.

        :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
        :return: peeked element or None if no element in this place
        """
        if ind < len(self._stack):
            return self._stack[-ind - 1]

    def clear(self) -> None:
        """
        Clear my stack

        :return: None
        """
        self._stack.clear()
