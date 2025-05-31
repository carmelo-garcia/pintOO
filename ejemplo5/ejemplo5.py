#/usr/bin/python3


from symbols.Variable import Variable
from values.Number import Number

class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"Variable {self.name} has value {self.value}"
      
v=Variable("a",Number(3))
print(v)
