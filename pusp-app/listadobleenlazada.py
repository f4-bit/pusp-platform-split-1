from nodo import Nodo

class ListaDobleEnlazada:

  def __init__(self):
    self.inicio = None
    self.fin = None
  
  def insertar_inicio(self, valor):
    nuevo_nodo = Nodo(valor)
    if self.inicio is None:
      self.inicio = nuevo_nodo
      self.fin = nuevo_nodo
    else:
      nuevo_nodo.siguiente = self.inicio
      self.inicio.anterior = nuevo_nodo
      self.inicio = nuevo_nodo
  
  def insertar_fin(self, valor):
    nuevo_nodo = Nodo(valor)
    if self.fin is None:
      self.inicio = nuevo_nodo
      self.fin = nuevo_nodo
    else:
      nuevo_nodo.anterior = self.fin
      self.fin.siguiente = nuevo_nodo
      self.fin = nuevo_nodo