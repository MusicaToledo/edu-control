import colegio as Colegio
import administrador as Administador
from alumno import Alumno

registro = Colegio.Colegio()

#Aqui va la funcion para mostrar el panel principal




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
            break
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
        return
    
#MENÚ INTERACTIVO 
# Si el usuario pasó el filtro, llega acá. Es un menú que se repite todo el 
# tiempo en pantalla para que elija: la Opción 1 para cambiar la contraseña,
# la Opción 2 para cerrar sesión y salir del programa.

    while True:
        print("-------------------------------------------")
        print("               MENÚ CLAVE")
        print("-------------------------------------------")
        print("1. Cambiar clave")
        print("2. Salir")
        print("-------------------------------------------")

        opcion = input("Selecciona la opcion: ")
        if opcion == "1":
            nueva = input("Introduce clave nueva: ")
            sistema.cambio_clave(nueva)
        elif opcion == "2":
            print("Cerrando sesion. Hasta luego!")
            break
        else:
            print("Opcion inválida.")


#Aqui termina la funcion de validacion_clave()


#Aqui va la funcion de panel_admin()




#Aqui termina la funcion de panel_admin()


#Aqui va la funcion de agregar_alumno()




#Aqui termina la funcion de agregar_alumno()


#Aqui va la funcion de panel_alumno()
def panel_alumno(alumno):
    while True:
        print(f" Menu de estudiantes, bienvenido {alumno.nombre.upper()} ")
        print("1. Hacer tarea")
        print("2. Estudiar")
        print("3. Generar certificado")
        print("4. Cambiar mi contraseña")
        print("5. Salir")
        
        estudiante_op = input("Seleccione una opción: ").strip()
        
        #no ingresó nada
        if estudiante_op == "":
            print("No ingresó nada")
            input("Presione enter para continuar...")
            continue
            
        match estudiante_op:
            case "1":
                print("haz tarea vago/a")
                input("Presione enter para continuar")
                
            case "2":
                print("que esperas bobo/a")
                input("Presione enter para continuar")
                
            case "3":
                print("SOLICITUD DE CERTIFICADO")
                c3 = input("Ingrese contraseña para generar certificado: ")
                
                if c3 == alumno.password:
                    print(f"Certificado de {alumno.nombre} {alumno.apellido}, curso {alumno.curso}.")
                else:
                    print("Contraseña incorrecta")
                input("Presione enter para continuar...")
                    
            case "4":
                gestionar_clave_alumno(alumno)
                input("Presionar enter para continuar") # cambio de contraseña
                
            case "5":
                print("Regresando al menú principal") 
                break
                
            case _:
                print("Opción no válida")



#Aqui termina la funcion de panel_alumno()


#Aqui va la funcion de actualizar_credencial()validacion_clave
#Debe pedir la contraseña dos v

def gestionar_clave_alumno(alumno):
    # GESTIONAR CONTRASEÑA
        #Si no encontramos su clave

            if not alumno.password:

                #La crearemos

                while True:

                    #El alumno ingresa su clave y la validamos dos veces con .strip() le quitamos los espacios al texto

                    clave_alumno = input(f"Debes crear tu clave sin espacios: ").strip()

                    clave_alumno2 = input("Repite la clave: ").strip()

                    #Validamos si las claves no estan vacias y si coinciden

                    if clave_alumno == clave_alumno2 and clave_alumno != "":

                        #Establecemos la clave del alumno

                        alumno.establecer_clave(clave_alumno)

                        print("Operacion completada con exito.")

                        input("Pulsa ENTER para continuar...")

                        return

                    else:

                        #Le indicamos al alumno que hubo un error

                        print("Las claves no coinciden o estan vacias.")

                        input("Pulsa ENTER para continuar...")

                        

            #Por otro lado si encontramos que el alumno si cuenta con clave

            else:

                #La validaremos

                if not alumno.password(alumno):

                    return

                #Si valida su clave con exito la modificaremos

                while True:

                    #El alumno ingresa su clave y la validamos dos veces con .strip() le quitamos los espacios al texto

                    clave_alumno = input(f"Debes modificar tu clave sin espacios: ").strip()

                    clave_alumno2 = input("Repite la clave: ").strip()

                    #Validamos si las claves no estan vacias y si coinciden

                    if clave_alumno == clave_alumno2 and clave_alumno != "":

                        #Establecemos la clave del alumno

                        alumno.establecer_clave(clave_alumno)

                        print("Operacion completada con exito.")

                        input("Pulsa ENTER para continuar...")

                        return

                    else:

                        #Le indicamos al alumno que hubo un error

                        print("Las claves no coinciden o estan vacias.")

                        input("Pulsa ENTER para continuar...")

                        continue      


#Aqui termina la funcion de actualizar_credencial()

# Aqui va la funcion de obtener_ficha()

def obtener_ficha(): 
    print(" --- Obtener ficha Academica ---")
    rut = input("Ingrese el RUT del alumno a buscar: ")
    alumno = registro.buscar_alumno_por_rut(rut)

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
                registro.buscar_alumno_por_rut(alumno.rut)
                print(f"El alumno {alumno.nombre} {alumno.apellido} se encuentra matriculado en el nivel {alumno.curso}")
                break
            else:
                intentos -= 1
                print(f"Contraseña incorrecta te quedan {intentos} intentos.")
        print("Se te agotaron los intentos. No se imprimira el certificado.")
    except Exception as e:
        print(f"Error: {e}")


#Aqui termina la funcion de generar_certificado()

