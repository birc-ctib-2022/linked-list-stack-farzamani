"""A linked list implementation of a stack."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar('T')


@dataclass
class Link(Generic[T]):
    """A link in a linked list."""

    head: T
    tail: List[T]

    def __init__(self, head):
        self.head = head
        self.next = None


List = Optional[Link[T]]


class Stack(Generic[T]):
    """A stack of elements of (generic) type T."""

    def __init__(self) -> None:
        """Create a new stack of values of type T."""
        # FIXME: code here
        self.stack = None

    def push(self, x: T) -> None:
        """Push x on the top of this stack."""
        # FIXME: code here
        if self.stack == None:
            self.stack = Link(x)
        else:
            new_node = Link(x)
            new_node.next = self.stack
            self.stack = new_node

    def top(self) -> T:
        """Return the top of the stack."""
        # FIXME: code here
        if self.is_empty():
            return None
        else:
            return self.stack.head

    def pop(self) -> T:
        """Pop the top element off the stack and return it."""
        # FIXME: code here
        if self.is_empty():
            return None
        else:
            pop_node = self.stack.head
            self.stack = self.stack.next
            return pop_node

    def is_empty(self) -> bool:
        """Test if the stack is empty."""
        # FIXME: code here
        return True if self.stack == None else False

    def __str__(self):
        if self.is_empty():
            print("None")
        else:
            out = ""
            stack = self.stack
            while stack:
                out += str(stack.head)
                stack = stack.next
                if stack:
                    out += "->"
            return out

def main():
    my_stack = Stack()
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    my_stack.push(40)
    my_stack.push(50)

    print(str(my_stack))

if __name__ == "__main__":
    main()