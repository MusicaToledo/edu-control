import colegio as Colegio
import administrador as Administador
import alumno as Alumno

registro = Colegio.Colegio()

#Aqui va la funcion para mostrar el panel principal




#Aqui termina la funcion para mostrar el panel principal


#Aqui va la funcion para validacion_clave()
#Debe permitir validar la identidad tanto al Alumno como al Administrador
#Debe permitir solo 3 intentos




#Aqui termina la funcion de validacion_clave()


#Aqui va la funcion de panel_admin()




#Aqui termina la funcion de panel_admin()


#Aqui va la funcion de agregar_alumno()




#Aqui termina la funcion de agregar_alumno()


#Aqui va la funcion de panel_alumno()




#Aqui termina la funcion de panel_alumno()


#Aqui va la funcion de actualizar_credencial()validacion_clave
#Debe pedir la contraseña dos v




#Aqui termina la funcion de actualizar_credencial()


#Aqui va la funcion de obtener_ficha()




#Aqui termina la funcion de obtener_ficha()


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