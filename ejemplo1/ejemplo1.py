#/usr/bin/python3

class Number:
    unit = "Kilograms"  # Valor por defecto

    def __init__(self, value):
        self.value = value


n1=Number(10)
print str(n1.value)+" "+Number.unit
Number.unit="Grams"
n2=Number(20)
print str(n1.value)+" "+Number.unit
print str(n2.value)+" "+Number.unit

