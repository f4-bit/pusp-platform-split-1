from listadobleenlazada import ListaDobleEnlazada

class Producto:

  def __init__(self, nombre):
    self.nombre = nombre
    self.reservas = ListaDobleEnlazada()
  
  def registrar_reserva(self, estudiante):
    self.reservas.insertar_fin(estudiante)