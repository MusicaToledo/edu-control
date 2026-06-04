# Esta clase crea y valida la clave del administrador
""" 
Esta clase se usara para validar la clave e ingresar al menú de administrador
"""
class Administrador:
    def __init__(self): 
        self.admin_key = "Edu2026" 
    def validar_clave(self,clave):
        if clave == self.admin_key:
            return True
        else:
            return False