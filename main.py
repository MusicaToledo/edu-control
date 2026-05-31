import colegio as Colegio
import administrador as Administador
import alumno as Alumno

colegio = Colegio.Colegio()

#Aqui va la funcion para mostrar el panel principal

def panel_principal():
    while True:
        print("\n------------ EduControl ------------")
        print("1. ingresar como administrador")
        print("2. ingresar como alumno")
        print("3. Salir del sistema")
        opcion = input("Seleccione solo una opcion: ")
        if opcion == "1":
            panel_admin()
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


# Aquí preparamos todo antes de empezar, traemos al administrador, definimos 
# que el límite son 3 intentos, ponemos el contador a cero y dejamos el acceso 
# cerrado hasta que se demuestre lo contrario.
def validacion_clave():
    sistema= Administador.Administrador() #Instanciamos el objeto del administrador para poder verificarla o cambiarla
    intento = 3
    contador = 0
    autenticado = False #Dejamos el acceso cerrado (autenticado = False) hasta que se demuestre lo contrario.
    print("=======================================================")
    print("            SISTEMA DE VALIDACIÓN DE CLAVE")
    print("=======================================================")

# Este bucle le da al usuario 3 intentos para poner la clave. Si es correcto, 
# abrimos el candado (autenticado = True) y saltamos hacia adelante. Si le se equivoca, 
# le sumamos un error, calculamos cuántos intentos le quedan y lo dejamos reintentar.

    while contador < intento:
        clave = input("Ingrese clave: ")
        if sistema.clave(clave):
            print ("Acceso concedido.")
            autenticado = True
            return autenticado
        else:
            contador +=1
            intentos_restantes= intento - contador
            print(f"Clave incorrecta. Intentos restantes : { intentos_restantes}")

# Acá revisamos qué pasó arriba. Si el usuario falló los 3 intentos, el programa avisa que el sistema se bloqueó y tira un 
# 'return' para echarlo de la función inmediatamente, sin dejarlo ver el menú.
    if not autenticado:
        print("************************************************************")
        print("SISTEMA BLOQUEADO: has superado el límite de los 3 intentos.")
        print("************************************************************")
        return autenticado

#Aqui termina la funcion de validacion_clave()


#Aqui va la funcion de panel_admin()

def panel_admin():
    if not validacion_clave():
        return
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
                obtener_ficha()
                #opcion para poder salir del menu        
            case "3":
                print("Saliendo del panel de administrador")
                break
                #opcion por defecto para opcion invalida
            case _:
                print("Opción invalida")
                continue
#Aqui termina la funcion de panel_admin()


#Aqui va la funcion de agregar_alumno()

def registrar_alumno():
    while True:
        rut = input("Ingrese el rut del alumno: ")
        if len(rut) >= 8 and len(rut) <= 10:
            print("el rut ingresado es correcto")
            break
        else:
            print("rut incorrecto")
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    while True:
            #Despliegue de los cursos
        for i, nivel in enumerate(colegio.obtener_cursos(), start=1):
            print(f"{i}. {nivel}")
        seleccion = input("Seleccione el numero del curso: ")
            #Validacion para el curso
        if seleccion != "" and seleccion.isnumeric():
            indice = int(seleccion) - 1
            if indice < 0 or indice >= len(colegio.obtener_cursos()):
                print("Opcion no valida.")
                input("Pulsa ENTER para volver a intentar...")
                continue
            curso = colegio.obtener_cursos()[indice]
            break
        else:
            print("Opcion no valida.")
            input("Pulsa ENTER para volver a intentar...")
            continue
    alumno = Alumno.Alumno(rut, nombre, apellido, curso)
    colegio.agregar_alumno(alumno)
    print(f"El alumno {alumno.nombre} {alumno.apellido} ha sido registrado correctamente en el curso {alumno.curso}.")
    return alumno

#Aqui termina la funcion de agregar_alumno()


#Aqui va la funcion de panel_alumno()




#Aqui termina la funcion de panel_alumno()


#Aqui va la funcion de actualizar_credencial()validacion_clave
#Debe pedir la contraseña dos v




#Aqui termina la funcion de actualizar_credencial()

# Aqui va la funcion de obtener_ficha()

def obtener_ficha(): 
    print(" --- Obtener ficha Academica ---")
    rut = input("Ingrese el RUT del alumno a buscar: ")
    alumno = colegio.buscar_alumno_por_rut(rut)

    if alumno != None:
        print("=======================================")
        print("          DATOS DEL ALUMNO             ")
        print("=======================================")
        print(f"RUT:           {alumno.rut}")
        print(f"Nombre:        {alumno.nombre}")
        print(f"Apellido:      {alumno.apellido}")
        print(f"Curso:         {alumno.curso}")
        print("---------------------------------------")
        print("=======================================")
    else:
            print("El alumno con RUT ingresado no se encuentra registrado.")



# Aqui termina la funcion de obtener_ficha()


#Aqui va la funcion de generar_certificado()

def generar_certificado(alumno):
    intentos = 3
    try:
        while intentos > 0:
            clave = input(f"Hola {alumno.nombre}, ingresa tu clave: ")
            if alumno.validar_de_contraseña(clave):
                colegio.buscar_alumno_por_rut(alumno.rut)
                print(f"El alumno {alumno.nombre} {alumno.apellido} se encuentra matriculado en el nivel {alumno.curso}")
                break
            else:
                intentos -= 1
                print(f"Contraseña incorrecta te quedan {intentos} intentos.")
        print("Se te agotaron los intentos. No se imprimira el certificado.")
    except Exception as e:
        print(f"Error: {e}")


#Aqui termina la funcion de generar_certificado()