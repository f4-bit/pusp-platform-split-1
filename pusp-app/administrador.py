from listadobleenlazada import ListaDobleEnlazada

class Administrador:

  def __init__(self):
    self.estudiantes = ListaDobleEnlazada()
    self.num_estudiantes_computadoras_reservadas = 0
    self.num_estudiantes_bicicletas_reservadas = 0
    self.num_comidas_compradas = 0
  
  def agregar_estudiante(self, estudiante):
    self.estudiantes.insertar_fin(estudiante)
  
  def generar_estadisticas(self):
    print("\nEstadísticas del sistema:")
    print(
        f"Número de estudiantes con computadoras reservadas: {self.num_estudiantes_computadoras_reservadas}"
    )
    print(
        f"Número de estudiantes con bicicletas reservadas: {self.num_estudiantes_bicicletas_reservadas}"
    )
    print(f"Número de comidas compradas: {self.num_comidas_compradas}")