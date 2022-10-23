string = ''
example = ''
result = 0

opSelect = {'*': lambda x, y: int(x) * int(y),
                '+': lambda x, y: int(x) + int(y),
                '-': lambda x, y: int(x) - int(y),
                '/': lambda x, y: int(x) / int(y)}

def set_string(exp: str):
    global string
    string = exp
    

def get_string():
    return string

string = string.replace(' ', '').strip()
string = string.replace('+', ' + ')\
    .replace('-', ' - ')\
    .replace('*', ' * ')\
    .replace('/', ' / ')
string = string.split()


def deleteElement(string, i):
    string.pop(i + 1)
    string.pop(i)


def operation(string, i, oper):
    if string[i] == oper:
        string[i - 1] = opSelect.get(oper)(int(string[i - 1]), int(string[i + 1]))
        deleteElement(string, i)
        return True

def set_example(string: str):
    global example
    example = ''.join(string)
    

def get_example():
    return example

def set_result(string: string):
    while len(string)>1:
        if '*' in string or '/' in string:
            for i in range(len(string)):
                if operation(string, i, '*'): break
                if operation(string, i, '/'): break
        elif '+' in string or '-' in string:
            for i in range(len(string)):
                if operation(string, i, '+'): break
                if operation(string, i, '-'): break
    global result
    result = string[0]

def get_result():
    global result
    return result