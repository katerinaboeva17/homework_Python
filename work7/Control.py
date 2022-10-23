import View, Model

def start():
    exp = View.InputData()
    Model.set_string(exp)
    string = Model.get_string()
    string = string.replace(' ', '').strip()
    string = string.replace('+', ' + ')\
    .replace('-', ' - ')\
    .replace('*', ' * ')\
    .replace('/', ' / ')
    string = string.split()
    Model.set_example(string)
    example = Model.get_example()
    Model.set_result(string)
    result = Model.get_result()
    View.OutputResult(example, result)
    