def init_stack():
    return list()

def push(stack, value):
    stack.append(value)
    return stack

def pop(stack):
    if len(stack) > 0:
        stack.pop()
    return stack

def size(stack):
    return len(stack)

def empty(stack):
    return len(stack) == 0

def top(stack):
    if len(stack) > 0:
        return stack[-1]
    return None
