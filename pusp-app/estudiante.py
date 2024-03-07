class Estudiante:

  def __init__(self, nombre, id_estudiante, saldo=1000):
    self.nombre = nombre
    self.id_estudiante = id_estudiante
    self.saldo = saldo
    self.computadora_reservada = False
    self.bicicleta_reservada = False
  
  def reservar_computadora(self, lista_productos):
    if not self.computadora_reservada:
      self.computadora_reservada = True
      lista_productos.insertar_fin(self)
      return True
    else:
      return False
  
  def reservar_bicicleta(self, lista_productos):
    if not self.bicicleta_reservada:
      self.bicicleta_reservada = True
      lista_productos.insertar_fin(self)
      return True
    else:
      return False
  
  def comprar_comida(self, cantidad, lista_productos):
    if self.saldo >= cantidad:
      self.saldo -= cantidad
      lista_productos.insertar_fin(self)
      return True
    else:
      return False