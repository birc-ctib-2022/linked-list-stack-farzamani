"""Testing our stack implementation."""
from stack import Stack

def test_me() -> None:
    """I really hope you test your code."""
    assert 2 + 2 == 4

    my_stack = Stack()
    assert my_stack.is_empty() == True

    my_stack.push(10)
    assert my_stack.is_empty() == False
    assert my_stack.top() == 10

    my_stack.push(20)
    assert my_stack.top() == 20

    my_stack.push(30)
    assert my_stack.top() == 30

    assert my_stack.pop() == 30
    assert my_stack.top() == 20

    my_stack.push(40)
    my_stack.push(50)
    my_stack.push(60)

    assert "60->50->40->20->10" == str(my_stack)

    assert my_stack.pop() == 60
    assert my_stack.pop() == 50
    assert my_stack.pop() == 40
    assert my_stack.top() == 20

    assert my_stack.is_empty() == False

    my_stack.pop()
    my_stack.pop()
    assert my_stack.top() == None
    assert my_stack.is_empty() == True
