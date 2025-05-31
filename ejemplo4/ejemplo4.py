#/usr/bin/python3


class Number:
    def __init__(self, value):
        self.value = value
        self.type = type(value)

n1=Number(10)
n2=Number(10.0)
print n1.type
print n2.type

