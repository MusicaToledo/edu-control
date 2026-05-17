# ¿Qué hace el __init__ ?: es el método constructor de la clase 
# ¿Qué hace la clase de Colegio?
# es un diccionario que ya viene con los 12 cursos predefinidos (desdes 1ro básico hasta 4to medio).
# el metodo agregar_alumno recibe un objeto del alumno y lo agrega al curso correspondiente.
# el metodo obtener_registro_global devuelve el diccionario completo con todos los cursos y alumnos registrados.
# el metodo obtener_cursos devuelve una lista con los nombres de los cursos disponibles.
# el metodo buscar_alumno_por_rut recibe un rut y busca en todos los cursos si hay un alumno con el rut solicitado.


class Colegio:
    def __init__(self):
        self.registro_global = {
            "1ro Basico": {},
            "2do Basico": {},
            "3ro Basico": {},
            "4to Basico": {},
            "5to Basico": {},
            "6to Basico": {},
            "7mo Basico": {},
            "8vo Basico": {},
            "1ro Medio": {},
            "2do Medio": {},
            "3ro Medio": {},
            "4to Medio": {},
        }
    def agregar_alumno(self, alumno):
        self.registro_global[alumno.curso][alumno.rut] = alumno
    def obtener_registro_global(self):
        return self.registro_global
    def obtener_cursos(self):
        return list(self.registro_global.keys())
    def buscar_alumno_por_rut(self, rut):
        for alumno in self.registro_global.values():
            if rut in alumno:
                return alumno[rut]


