# E.3.1.IN2
from os import system
system("cls")


class Usuario ():
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self. apellido = apellido
        self.intentos_de_login=0

    def descriptor(self):
        print(self.nombre,",es muy  simpatico")

    def saludar_usuario(self):
        print ("Saludos   ",self.nombre, self.apellido)

    def incrementar_inicios_de_sesion(self):
        self.intentos_de_login += 1
        print ("Número de intentos   :",self.intentos_de_login)
    

    def reset_intentos_de_login(self):
        self.intentos_de_login = 0
        print ("Intento de incio de sesión   :",self.intentos_de_login)
    


luis = Usuario("Luis", "Debia")
pedro= Usuario ("Pedro", "Molina")
print()
print (luis.nombre, luis.apellido)
luis.descriptor()
luis.saludar_usuario()
luis.incrementar_inicios_de_sesion()
luis.incrementar_inicios_de_sesion()
luis.incrementar_inicios_de_sesion()
luis.incrementar_inicios_de_sesion()

luis.reset_intentos_de_login()






