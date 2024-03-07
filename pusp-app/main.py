from sistema import Sistema
from estudiante import Estudiante

if __name__ == "__main__":
  sistema = Sistema()

  while True:
    usuario = ""

    while usuario.lower() not in ["e", "p", "a"]:
      usuario = input(
          "¿Eres un estudiante, un proveedor o un administrador? (E/P/A) \nSi quieres acceder como proveedor, usuario y contraseña: proveedor \nSi quieres acceder como administrador, usuario y contraseña: admin \n\n Escoja su opción: ")

    while True:
      if usuario.lower() == "e":
        # Funciones para estudiantes
        print("\n1. Reservar computadora")
        print("2. Reservar bicicleta")
        print("3. Comprar comida")
        print("4. Cerrar sesión")
        opcion = int(input("Selecciona una opción: "))
        if opcion == 4:
          break
        id_estudiante = input("Ingresa tu ID de estudiante: ")
        nombre_estudiante = input("Ingresa tu nombre: ")

        nuevo_estudiante = Estudiante(nombre_estudiante, id_estudiante)

        # Insertar estudiante en la lista doblemente enlazada de estudiantes
        sistema.estudiantes.insertar_fin(nuevo_estudiante)

        # Si el estudiante elige reservar una computadora, bicicleta o comprar comida,
        # se registra la reserva o compra en la lista correspondiente de productos
        if opcion == 1:
          if nuevo_estudiante.reservar_computadora(
              sistema.computadoras.reservas):
            sistema.administrador.num_estudiantes_computadoras_reservadas += 1
            print("Reserva de computadora realizada con éxito.")
          else:
            print("No se pudo reservar la computadora.")
        elif opcion == 2:
          if nuevo_estudiante.reservar_bicicleta(sistema.bicicletas.reservas):
            sistema.administrador.num_estudiantes_bicicletas_reservadas += 1
            print("Reserva de bicicleta realizada con éxito.")
          else:
            print("No se pudo reservar la bicicleta.")
        elif opcion == 3:
          cantidad_comida = int(
              input("Ingresa la cantidad de comida que deseas comprar: "))
          if nuevo_estudiante.comprar_comida(cantidad_comida,
                                             sistema.comida.reservas):
            sistema.administrador.num_comidas_compradas += cantidad_comida
            print("Compra de comida realizada con éxito.")
          else:
            print("Saldo insuficiente.")

      elif usuario.lower() == "p":
        # Funciones para proveedores
        usuario_proveedor = input("Usuario: ")
        contraseña_proveedor = input("Contraseña: ")

        if sistema.login(usuario_proveedor,
                         contraseña_proveedor) == "proveedor":
          print("\n1. Agregar stock")
          print("2. Cerrar sesión")
          opcion = int(input("Selecciona una opción: "))

          if opcion == 1:
            producto = input(
                "Producto a agregar stock (computadoras/bicicletas/comida): ")
            cantidad = int(input("Cantidad a agregar: "))
            sistema.proveedor.agregar_stock(producto, cantidad)
            print("Stock agregado con éxito.")
          elif opcion == 2:
            break
        else:
          print("Usuario o contraseña incorrectos.")

      elif usuario.lower() == "a":
        # Funciones para administradores
        usuario_admin = input("Usuario: ")
        contraseña_admin = input("Contraseña: ")

        if sistema.login(usuario_admin, contraseña_admin) == "admin":
          print("\n1. Generar estadísticas")
          print("2. Cerrar sesión")
          opcion = int(input("Selecciona una opción: "))

          if opcion == 1:
            sistema.administrador.generar_estadisticas()
          elif opcion == 2:
            break
        else:
          print("Usuario o contraseña incorrectos.")

    salir_programa = input("\n¿Desea salir del programa? (s/n): ")
    if salir_programa.lower() == "s":
      break
