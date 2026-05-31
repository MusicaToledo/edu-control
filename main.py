import colegio as Colegio
import administrador as Administador
from alumno import Alumno

registro = Colegio.Colegio()

#Aqui va la funcion para mostrar el panel principal
def panel_principal():
    while True:
        print("\n------------ EduControl ------------")
        print("1. ingresar como administrador")
        print("2. ingresar como alumno")
        print("3. Salir del sistema")
        opcion = input("Seleccione solo una opcion: ")
        if opcion == "1":
            print("ingresando al panel de administrador....")
            validacion_clave()
        elif opcion == "2":
            print("ingresando al panel de alumno.....")
            panel_alumno()  #la voy a dejar asi aunque  todavia no este echo el panel de alumno 
        elif opcion == "3":
            print("saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.") 
            continue




#Aqui termina la funcion para mostrar el panel principal
