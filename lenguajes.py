import pygame


class Lenguajes:
    def __init__(self):
        self.idioma = "español"
        self.traducciones = {
            "español": {
                # Captions
                "menu": {"texto": "Menú Principal", "size": 20},
                "personalizable": {"texto": "Menú Personalizable", "size": 20},
                "bG": {"texto": "Bienvenida", "size": 20},
                "bH": {"texto": "Bienvenido", "size": 20},
                "instrucciones": {"texto": "Instrucciones", "size": 20},
                "nombre": {"texto": "Nombre", "size": 20},
                "ingNombre": {"texto": "Ingrese nombre:", "size": 20},
                "nivel": {"texto": "Nivel", "size": 20},
                "historia": {"texto": "Historia", "size": 20},
                # Idioma
                "mx": {"texto": "Español", "size": 35},
                "usa": {"texto": "Inglés", "size": 35},
                "idioma": {"texto": "Elige su idioma: ", "size": 22},
                # MenúPrincipal (botones)
                "iniciar": {"texto": "Iniciar", "size": 40},
                "configuracion": {"texto": "Configuración", "size": 40},
                "creadores": {"texto": "Desarrolladores", "size": 24},
                "salir": {"texto": "Salir", "size": 40},
                # Agrega aquí más traducciones en español
                "niña": {"texto": "NIÑA", "size": 39},
                "niño": {"texto": "NIÑO", "size": 39},
                "niña2": {"texto": "Niña", "size": 39},
                "niño2": {"texto": "Niño", "size": 39},
                "seleccionaPersonaje": {"texto": "Seleccione su personaje", "size": 20},
                "presione": {"texto": "Presiona", "size": 15},
                "paCon": {"texto": "para continuar", "size": 15},
                "tiempo": {"texto": "Tiempo", "size": 15},
                # Cuando Pierde
                "pF": {"texto": "Puntaje final: ", "size": 15},
                #Slider
                "anterior": {"texto": "Anterior", "size": 15},
                "siguiente": {"texto": "Siguiente", "size": 15},

            },
            "inglés": {
                "menu": {"texto": "Main Menu", "size": 20},
                "personalizable": {"texto": "Customizable Menu", "size": 20},
                "bG": {"texto": "Welcome", "size": 20},
                "bH": {"texto": "Welcome", "size": 20},
                "instrucciones": {"texto": "Instructions", "size": 20},
                "nombre": {"texto": "Name", "size": 20},
                "mx": {"texto": "Spanish", "size": 35},
                "usa": {"texto": "English", "size": 35},
                "idioma": {"texto": "Choose your language: ", "size": 22},
                "iniciar": {"texto": "Start", "size": 40},
                "configuracion": {"texto": "Settings", "size": 40},
                "creadores": {"texto": "Developers", "size": 30},
                "salir": {"texto": "Exit", "size": 40},
                "nivel": {"texto": "Level", "size": 20},
                "historia": {"texto": "Story", "size": 20},
                # Agrega aquí más traducciones en inglés
                "niña": {"texto": "GIRL", "size": 39},
                "niño": {"texto": "BOY", "size": 39},
                "niña2": {"texto": "Girl", "size": 39},
                "niño2": {"texto": "Boy", "size": 39},
                "seleccionaPersonaje": {"texto": "Select your character", "size": 20},
                "ingNombre": {"texto": "Enter your name:", "size": 20},
                "presione": {"texto": "Press", "size": 15},
                "paCon": {"texto": "to continue", "size": 15},
                "tiempo": {"texto": "Time", "size": 15},
                # Cuando Pierde
                "pF": {"texto": "Final score: ", "size": 15},
                #Slider
                "anterior": {"texto": "Previous", "size": 15},
                "siguiente": {"texto": "Next", "size": 15},
            },
        }

    def cambiar_idioma(self, nuevo_idioma):
        if nuevo_idioma in self.traducciones:
            self.idioma = nuevo_idioma

    def obtener_idioma(self):
        return self.idioma

    def obtener_traduccion(self, clave):
        return self.traducciones[self.idioma].get(clave, {"texto": clave, "size": 20})


# Crear una instancia de la clase para gestionar el idioma
idiomas_manager = Lenguajes()
