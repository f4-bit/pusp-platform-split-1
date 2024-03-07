from listadobleenlazada import ListaDobleEnlazada
from administrador import Administrador
from proveedor import Proveedor
from producto import Producto

class Sistema:

  def __init__(self):
    self.estudiantes = ListaDobleEnlazada()
    self.administrador = Administrador()
    self.proveedor = Proveedor("ProveedorPrincipal")
    self.computadoras = Producto("computadoras")
    self.bicicletas = Producto("bicicletas")
    self.comida = Producto("comida")
  
  def login(self, usuario, contraseña):
    if usuario == "proveedor" and contraseña == "proveedor":
      return "proveedor"
    elif usuario == "admin" and contraseña == "admin":
      return "admin"
    else:
      return "estudiante"
  
  def registro_estudiante(self, estudiante):
    # No se necesita registro de estudiantes en este momento
    pass