import colegio as Colegio
import administrador as Administador
import alumno as Alumno

colegio = Colegio.Colegio()
sistema = Administador.Administrador()

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
def validacion_clave(usuario, rol=""):
    intento = 3
    contador = 0
    autenticado = False #Dejamos el acceso cerrado (autenticado = False) hasta que se demuestre lo contrario.
    print("=======================================================")
    print("            SISTEMA DE VALIDACIÓN DE CLAVE             ")
    print("=======================================================")
# Este bucle le da al usuario 3 intentos para poner la clave. Si es correcto, 
# abrimos el candado (autenticado = True) y saltamos hacia adelante. Si le se equivoca, 
# le sumamos un error, calculamos cuántos intentos le quedan y lo dejamos reintentar.
    if rol == "admin":
        while contador < intento:
            clave = input("Ingrese clave: ")
            if usuario.clave(clave):
                print ("Acceso concedido.")
                autenticado = True
                return autenticado
            else:
                contador +=1
                intentos_restantes= intento - contador
                print(f"Clave incorrecta. Intentos restantes : { intentos_restantes}")
    else:
        if not usuario.password:
            gestionar_clave_alumno(usuario)
        while contador < intento:
            clave = input("Ingrese clave: ")
            if usuario.validar_de_contraseña(clave):
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
    #Validamos la clave del administrador.
    if not validacion_clave(sistema, "admin"):
        return
    #Ingresamos al menu de administrador.
    while True:
        print("""\nPanel de Administrador
            1. Registrar Alumno
            2. Buscar alumno(rut)
            3. Salir""")
        opcion = input("Seleccione una opción: ")
        match opcion:
                #Registro de alumno.
            case "1":
                registrar_alumno()
                #Busqueda del alumno en base del rut.
            case "2":
                obtener_ficha()
                #Opcion para poder salir del menu.  
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
    #Validamos el campo del rut
    while True:
        rut = input("Ingrese el rut del alumno: ").strip()
        #Validamos que el rut tenga entre 8 a 9 caracteres.
        if len(rut) > 9 or len(rut) < 8:
            print("El rut ingresado no es correcto.")
            continue
        #Validamos que el rut no exista en el registro.
        if colegio.buscar_alumno_por_rut(rut):
            print("Ese rut ya existe, intentalo de nuevo.")
            continue
        #Si pasamos ambas validaciones avanzamos
        break
    #Validamos el campo del nombre y apellido.
    while True:
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        #Validamos si el nombre O el apellido estan vacios.
        if not nombre or not apellido:
            print("El nombre y el apellido no pueden quedar vacios.")
            continue
        #Si pasamos la validacion avanzamos.
        break
    #Validamos el campo de curso.
    while True:
        #Despliegue de los cursos.
        for i, nivel in enumerate(colegio.obtener_cursos(), start=1):
            print(f"{i}. {nivel}")
        seleccion = input("Seleccione el numero del curso: ")
        #Validamos el indice seleccionado.
        try:
            indice = int(seleccion) - 1
            #Validamos que el indice este dentro del rango de los cursos.
            if indice >= 0 and indice < len(colegio.obtener_cursos()):
                curso = colegio.obtener_cursos()[indice]
                break
            #Si no, mandamos mensaje de que el curso no existe.
            else:
                print("Error: El curso no existe.")
                input("Pulsa ENTER para volver a intentar...")
                continue
        #Manejamos el error del valor si ingresa una opcion vacia o si ingresa una letra.
        except ValueError:
            print("Error: El campo no puede estar vacio y solo admite numeros.")
            input("Pulsa ENTER para volver a intentar...")
    #Si pasamos todas las validaciones, creamos al alumno.
    alumno = Alumno.Alumno(rut, nombre, apellido, curso)
    #Agregamos el alumno a nuestro registro.
    colegio.agregar_alumno(alumno)
    print(f"El alumno {alumno.nombre} {alumno.apellido} ha sido registrado correctamente en el curso {alumno.curso}.")
#Aqui termina la funcion de agregar_alumno()


#Aqui va la funcion de panel_alumno()
def panel_alumno():
    rut = input("Ingrese su RUT: ").strip()
    alumno = colegio.buscar_alumno_por_rut(rut)
    if not alumno:
        print("Error: El alumno no fue encontrado.")
        input("Pulsa ENTER para continuar...")
        return
    if not validacion_clave(alumno):
        print("Error: Clave incorrecta.")
        input("Pulsa ENTER para continuar...")
        return
    while True:
        print(f"Menu de estudiantes, bienvenido {alumno.nombre.capitalize()}")
        print("1. Generar certificado.")
        print("2. Ficha academica.")
        print("3. Cambiar mi contraseña.")
        print("4. Salir")
        estudiante_op = input("Seleccione una opción: ").strip()
        match estudiante_op:
            case "1":
                generar_certificado(alumno)
            case "2":
                obtener_ficha(alumno)
            case "3":
                gestionar_clave_alumno(alumno)
            case "4":
                print("Regresando al menú principal") 
                break
            case "":
                print("No ingresaste nada.")
            case _:
                print("Opción no válida")
#Aqui termina la funcion de panel_alumno()

#Aqui va la funcion de actualizar_credencial()validacion_clave
#Debe pedir la contraseña dos v
def gestionar_clave_alumno(alumno):
    # GESTIONAR CONTRASEÑA
    # No encontramos su clave, la crearemos
    if not alumno.password:
        while True:
            # El alumno ingresa su clave y quitamos espacios a los extremos con .strip()
            clave_alumno = input("Debes crear tu clave sin espacios: ").strip()
            clave_alumno2 = input("Repite la clave: ").strip()
            # Validamos si las claves no están vacías y si coinciden
            if clave_alumno == clave_alumno2 and clave_alumno != "":
                alumno.creacion_de_contraseña(clave_alumno)
                print("Operación completada con éxito. Clave creada.")
                input("Pulsa ENTER para continuar...")
                return
            else:
                print("Las claves no coinciden o están vacías.")
                input("Pulsa ENTER para continuar...")
    # Si encontramos que el alumno sí cuenta con clave
    else:
        # Le pedimos la clave actual antes de cambiarla
        print("Para cambiar tu clave, ingresa la actual")
        clave_actual = input("Introduce tu contraseña actual: ").strip()
        
        # Usamos el método correcto de tu clase Alumno para verificar
        if not alumno.validar_de_contraseña(clave_actual):
            print("Contraseña incorrecta. Operación cancelada.")
            input("Pulsa ENTER para continuar...")
            return  # Lo saca por si se equivoca
        
        # Si valida su clave con éxito, ahora lo dejamos modificarla
        while True:
            clave_alumno = input("Debes modificar tu clave sin espacios: ").strip()
            clave_alumno2 = input("Repite la clave: ").strip()

            if clave_alumno == clave_alumno2 and clave_alumno != "":
                alumno.creacion_de_contraseña(clave_alumno)
                print("Operación completada con éxito. Clave modificada.")
                input("Pulsa ENTER para continuar...")
                return
            else:
                print("Las claves no coinciden o están vacías.")
                input("Pulsa ENTER para continuar...")
#Aqui termina la funcion de actualizar_credencial()

# Aqui va la funcion de obtener_ficha()

def obtener_ficha(alumno=""):
    print(" --- Obtener ficha Academica ---")
    if not alumno: 
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
#Aqui se podran realizar pruebas
# alumno = Alumno.Alumno("205045678", "Martin", "Ardiles", "1ro Basico")
# alumno.creacion_de_contraseña("1208")
# gestionar_clave_alumno(alumno)
# validacion_clave(sistema, "admin")
panel_principal()