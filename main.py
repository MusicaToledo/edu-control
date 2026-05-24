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
    try:
        registro.buscar_alumno_por_rut(alumno.rut)
        print(f"El alumno {alumno.nombre} {alumno.apellido} se encuentra matriculado en el nivel {alumno.curso}")
    except:
        print("Error: Alumno no encontrado")


#Aqui termina la funcion de generar_certificado()
alumno = Alumno.Alumno("205045678", "Martin", "Ardiles", "1ro Medio")
if __name__ == "__main__":
    generar_certificado(alumno)