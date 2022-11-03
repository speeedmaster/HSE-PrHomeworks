import stack_func
from stack_oop import Stack

import pytest

def test_init():
    fstack = stack_func.init_stack()
    ostack = Stack()
    assert stack_func.empty(fstack)
    assert ostack.empty()

def test_pop_empty():
    fstack = stack_func.init_stack()
    ostack = Stack()
    assert stack_func.size(fstack) == 0
    assert ostack.size() == 0
    assert stack_func.empty(fstack)
    assert ostack.empty()
    for _ in range(10):
        assert stack_func.top(fstack) == None
        assert ostack.top() == None
        fstack = stack_func.pop(fstack)
        ostack.pop()
        assert stack_func.size(fstack) == 0
        assert ostack.size() == 0

def test_push():
    fstack = stack_func.init_stack()
    ostack = Stack()
    for i in range(10):
        assert stack_func.size(fstack) == i
        assert ostack.size() == i
        fstack = stack_func.push(fstack, i)
        ostack.push(i)
        assert stack_func.top(fstack) == i
        assert ostack.top() == i

def test_pop():
    fstack = stack_func.init_stack()
    ostack = Stack()
    for i in range(10):
        fstack = stack_func.push(fstack, i)
        ostack.push(i)

    for i in range(9, -1, -1):
        assert stack_func.top(fstack) == i
        assert ostack.top() == i
        fstack = stack_func.pop(fstack)
        ostack.pop()
        assert stack_func.size(fstack) == i
        assert ostack.size() == i

    assert stack_func.size(fstack) == 0
    assert ostack.size() == 0
    assert stack_func.empty(fstack)
    assert ostack.empty()

