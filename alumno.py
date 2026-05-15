#Creacion de la clase alumno y sus propiedades
class Alumno:
    def __init__(self, rut, nombre, apellido, curso):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        Self.password= None
        #metodo de creacion de contraseña este metodo permite crear la contraseña del alumno y poder guardarla  
    def contraseña(self,clave):
          self.password= clave
          return True
#metodo de validacion de contraseña este metodo va de la mano del anterior con la diferencia 
# de que este valida la contraseña con el dato de la clase alumno    
    def validar_contraseña(self,clave):
          if clave== self.password:
               return True
          else:
                return False
#metodo de certificado de alumno esto permite crear y obtener el certificado del alumno
# con los datos nesesarios del alumno                          
    def obtener_certificado(self):
             print(f"""\nCertificado de alumno:{self.rut}
             {self.nombre} 
             {self.apellido}, 
             Curso: {self.curso}""")
#metodo de la ficha del alumno este metdo permite crear la ficha del alumno con los mismos datos o 
#parecidos del certificado del alumno pero en un formato diferente
    def ficha_alumno(self):
      print(f"el alumno {self.nombre}, {self.apellido} a sido registrado en el curso {self.curso}")

        self.password = None
