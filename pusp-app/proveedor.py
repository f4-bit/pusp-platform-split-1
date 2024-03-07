class Proveedor:

  def __init__(self, nombre):
    self.nombre = nombre
    self.usuario = "proveedor"
    self.contraseña = "proveedor"
    self.productos_disponibles = {
        "computadoras": 10,
        "bicicletas": 20,
        "comida": 50
    }
  
  def reservar_producto(self, producto):
    if self.productos_disponibles[producto] > 0:
      self.productos_disponibles[producto] -= 1
      return True
    else:
      return False
  
  def agregar_stock(self, producto, cantidad):
    self.productos_disponibles[producto] += cantidad