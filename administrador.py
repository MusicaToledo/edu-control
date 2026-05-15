# Esta clase crea y valida la clave del administrador
""" 
La clase sistema usará esta clase para validad la clave e ingresar al menú de administrador
"""
class Administrador:
    def __init__(self): 
        self.admin_key = "python" 
    def validar_clave(self,clave):
        if clave == self.admin_key:
            return True
        else:
            return False