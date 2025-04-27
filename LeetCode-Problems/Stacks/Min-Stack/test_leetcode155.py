import pytest
from leetcode155 import MinStack  # Replace 'your_module' with the actual module name

def test_min_stack_operations():
    # Initialize the MinStack
    min_stack = MinStack()
    
    # Test pushing elements
    min_stack.push(3)
    assert min_stack.top() == 3
    assert min_stack.getMin() == 3
    
    min_stack.push(5)
    assert min_stack.top() == 5
    assert min_stack.getMin() == 3
    
    min_stack.push(2)
    assert min_stack.top() == 2
    assert min_stack.getMin() == 2
    
    min_stack.push(1)
    assert min_stack.top() == 1
    assert min_stack.getMin() == 1
    
    min_stack.push(4)
    assert min_stack.top() == 4
    assert min_stack.getMin() == 1
    
    # Test popping elements
    min_stack.pop()
    assert min_stack.top() == 1
    assert min_stack.getMin() == 1
    
    min_stack.pop()
    assert min_stack.top() == 2
    assert min_stack.getMin() == 2
    
    min_stack.pop()
    assert min_stack.top() == 5
    assert min_stack.getMin() == 3
    
    min_stack.pop()
    assert min_stack.top() == 3
    assert min_stack.getMin() == 3

def test_min_stack_edge_cases():
    # Initialize the MinStack
    min_stack = MinStack()
    
    # Test pushing duplicate elements
    min_stack.push(2)
    min_stack.push(2)
    assert min_stack.getMin() == 2
    min_stack.pop()
    assert min_stack.getMin() == 2
    
    # Test pushing negative elements
    min_stack.push(-1)
    assert min_stack.getMin() == -1
    min_stack.push(-3)
    assert min_stack.getMin() == -3
    min_stack.pop()
    assert min_stack.getMin() == -1

def test_min_stack_empty_pop():
    # Initialize the MinStack
    min_stack = MinStack()
    
    # Test popping from an empty stack
    with pytest.raises(IndexError):
        min_stack.pop()

def test_min_stack_empty_top():
    # Initialize the MinStack
    min_stack = MinStack()
    
    # Test getting top from an empty stack
    with pytest.raises(IndexError):
        min_stack.top()

def test_min_stack_empty_getMin():
    # Initialize the MinStack
    min_stack = MinStack()
    
    # Test getting minimum from an empty stack
    with pytest.raises(IndexError):
        min_stack.getMin()
