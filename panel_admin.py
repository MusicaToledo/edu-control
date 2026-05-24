#importacion de la clase alumno y colegio
from alumno import Alumno
from colegio import Colegio
colegio=Colegio()
#creacion de clave del admin 
clave_admin = input("Ingrese la clave del administrador: ")
clave_admin2 = input("Confirme la clave del administrador: ")
#metodo de registro de alumno para el panel del administrador
def  registrar_alumno():
    rut = input("Ingrese el rut del alumno: ")
    while True:
        if len(rut) >= 8 and len(rut) <= 10:
            print("el rut ingresado es correcto")
            break
        else:
            print("rut incorrecto")
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    curso = input("Ingrese el curso del alumno: ")
    alumno = Alumno(rut, nombre, apellido, curso)
    colegio.agregar_alumno(alumno)
    print(f"El alumno {alumno.nombre} {alumno.apellido} ha sido registrado correctamente.")
    return alumno
#inicio del menu del adminstrador con condicional de if y else  y el uso del bucle while True
def panel_admin():
    if clave_admin == clave_admin2:
         #menu
         while True:
            print("""\nPanel de Administrador
              1. Registrar Alumno
              2. Buscar alumno(rut)
              3. Salir""")
            opcion = input("Seleccione una opción: ")
            match opcion:
                #registro de alumno
               case "1":
                  registrar_alumno()
                #busqueda del alumno en base del rut  
               case "2":
                    buscar_alumno_rut=input("Ingrese el rut del alumno a buscar: ")
                    #llamado del metodo buscar_alumno_por_rut de la clase colegio 
                    # atraves de su variable creada aca para poder instanciarla 
                    encontrado=colegio.buscar_alumno_por_rut(buscar_alumno_rut)
                    if encontrado:
                        print(f"El alumno: {encontrado.nombre} {encontrado.apellido} se encuentre en el curso: {encontrado.curso}")
                    else:
                        print("No se a encontrado a ningun alumno con ese rut")
                        
                #opcion para poder salir del menu        
               case "3":
                    print("Saliendo del panel de administrador")
                    break
                #opcion por defecto para opcion invalida
               case _:
                    print("Opción invalida")
                    continue
#cierre del programa si es que las claves del administrador no coinciden                
    else:
        print("Las claves no coinciden. No se puede acceder al panel de administrador.")
panel_admin()