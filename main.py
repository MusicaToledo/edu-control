import colegio as Colegio
import administrador as Administador
import alumno as Alumno

#Aqui va la funcion para mostrar el panel principal




#Aqui termina la funcion para mostrar el panel principal


#Aqui va la funcion para validacion_clave()
#Debe permitir validar la identidad tanto al Alumno como al Administrador
#Debe permitir solo 3 intentos
def main():
    sistema= Administador()
    intento = 3
    contador = 0
    autenticado = False

    print("Validacion clave")
    while contador < intento:
        clave = ("Ingrese clave")
        if sistema.clave:
            print ("Acceso concedido")
            autenticado = True
            break
        else:
            contador +=1
            intentos_restantes= intento - contador
            print(f"clave incorrecta. Intento restante : { intentos_restantes}")
    if not autenticado:
        print("sistema bloqueado: has superado el limite de los 3 intentos")
        return
    while True:
        print("Menu de clave")
        print("1.Cambiar clave")
        print("2.Salir")

        opcion = input("Selecciona la opcion: ")
        if opcion == "1":
            nueva = input("Introduce clave nueva")
        elif opcion == "2":
            print("Cerrando sesion.")
            break
        else:print("Opcion inválida")




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




#Aqui termina la funcion de generar_certificado()