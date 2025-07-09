class Stack:
    def __init__(self, stack_string: str):
        self.stack_string = stack_string
        return

    def is_empty(self):
        return True if len(self.stack_string) == 0 else False

    def push(self, element: str):
        self.stack_string += element
        return

    def pop(self):
        last_element = self.stack_string[-1]
        self.stack_string = self.stack_string[0:-1]
        return last_element

    def peek(self):
        last_element = self.stack_string[-1]
        return last_element

    def size(self):
        return len(self.stack_string)

def is_balanced(example_string):
    stack = Stack('')
    for element in example_string:
        if stack.size() == 0 and element in ')]}':
            return 'Несбалансированно'
        if element in '([{':
            stack.push(element)
        if stack.size() > 0:
            if element == ')':
                if stack.peek() == '(':
                    stack.pop()
                else:
                    return 'Несбалансированно'
            elif element == ']':
                if stack.peek() == '[':
                    stack.pop()
                else:
                    return 'Несбалансированно'
            elif element == '}':
                if stack.peek() == '{':
                    stack.pop()
                else:
                    return 'Несбалансированно'
    if stack.size() == 0:
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'



if __name__ == '__main__':
    input_string = input('Введите строку: ')
    print(is_balanced(input_string))