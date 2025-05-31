#/usr/bin/python3


class Movimiento:
  saldo = 0


  def __init__(self, cantidad):
    self.cantidad = cantidad
    self.aplicar()

  def aplicar(self):
    pass  # Será implementado en las subclases

  @classmethod
  def getSaldo(cls):
    return cls.saldo


class Ingreso(Movimiento):
    def aplicar(self):
        Movimiento.saldo += self.cantidad


class Gasto(Movimiento):
    def aplicar(self):
        Movimiento.saldo -= self.cantidad


ingreso1=Ingreso(1000)
gasto1=Gasto(100)
ingreso2=Ingreso(200)

print("El saldo es "+str(Movimiento.getSaldo()))
