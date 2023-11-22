import pygame

class Poderes:
    def __init__(self,puntaje_anterior):
        # Inicializar Pygame
        pygame.init()
        # Cargar imágenes de los botones
        self.btnPoder1 = pygame.image.load("img/btn/btnPoder1.png")
        self.btnPoder1 = pygame.transform.scale(self.btnPoder1, (300, 300))
        self.btnPoder2 = pygame.image.load("img/btn/btnPoder2.png")
        self.btnPoder2 = pygame.transform.scale(self.btnPoder2, (300, 300))
        self.btnPoder3 = pygame.image.load("img/btn/btnPoder3.png")
        self.btnPoder3 = pygame.transform.scale(self.btnPoder3, (300, 300))

        # Crear imágenes "hover" para los botones
        self.btnPoder1_hover = pygame.image.load("img/btn/btnPoder1Hover.png")
        self.btnPoder1_hover = pygame.transform.scale(self.btnPoder1_hover, (300, 300))
        self.btnPoder2_hover = pygame.image.load("img/btn/btnPoder2Hover.png")
        self.btnPoder2_hover = pygame.transform.scale(self.btnPoder2_hover, (300, 300))
        self.btnPoder3_hover = pygame.image.load("img/btn/btnPoder3Hover.png")
        self.btnPoder3_hover = pygame.transform.scale(self.btnPoder3_hover, (300, 300))

        # Definir las posiciones de los botones
        self.button1_position = (-100, 100)
        self.button2_position = (-100, 200)
        self.button3_position = (-100, 300)
        self.puntaje_anterior=puntaje_anterior
        # Estado inicial de los botones
        self.current_button1 = self.btnPoder1
        self.current_button2 = self.btnPoder2
        self.current_button3 = self.btnPoder3
        self.es_inmune=False
        self.tiene_alcanzame=False
        self.tiene_volveralavida=False
        self.inmune=False
        self.alcanzame=False
        self.volveralavida=False
        
        if 55 <= self.puntaje_anterior <= 69:
            self.current_button1 = self.btnPoder1_hover
            self.current_button2 = self.btnPoder2_hover
            self.current_button3 = self.btnPoder3_hover
        if 70 <= self.puntaje_anterior <= 79:
            self.current_button1 = self.btnPoder1
            self.current_button2 = self.btnPoder2_hover
            self.current_button3 = self.btnPoder3_hover
            self.inmune=True
            self.alcanzame=False
            self.volveralavida=False
        elif 80 <= self.puntaje_anterior <= 89:
            self.current_button1 = self.btnPoder1
            self.current_button2 = self.btnPoder2
            self.current_button3 = self.btnPoder3_hover
            self.inmune=True
            self.alcanzame=False
            self.volveralavida=True
        elif 90 <= self.puntaje_anterior <= 100:
            self.current_button1 = self.btnPoder1
            self.current_button2 = self.btnPoder2
            self.current_button3 = self.btnPoder3
            self.inmune=True
            self.alcanzame=True
            self.volveralavida=True
        # Variables para rastrear si las teclas se han presionado
    def run(self, screen,puntaje):
            # Verificar las teclas presionadas
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1] and pygame.K_1 and self.inmune:
                self.current_button1 = self.btnPoder1_hover
                self.inmune=False
                self.es_inmune=True
                sonido_colision = pygame.mixer.Sound(
                            "Audio/manzanaInmune.mp3"
                        )
                sonido_colision.play()
            if keys[pygame.K_2] and pygame.K_2 and self.volveralavida:
                if (puntaje<50):
                    self.current_button2 = self.btnPoder2_hover
                    self.volveralavida=False
                    self.tiene_volveralavida=True
                    sonido_colision = pygame.mixer.Sound(
                            "Audio/volverVida.mp3"
                        )
                    sonido_colision.play()
            if keys[pygame.K_3] and pygame.K_3 and self.alcanzame:
                self.current_button3 = self.btnPoder3_hover
                self.alcanzame=False
                self.tiene_alcanzame=True
                sonido_colision = pygame.mixer.Sound(
                            "Audio/alcanzame.mp3"
                        )
                sonido_colision.play()
            # Dibujar los botones en la pantalla
            screen.blit(self.current_button1, self.button1_position)
            screen.blit(self.current_button2, self.button2_position)
            screen.blit(self.current_button3, self.button3_position)
            # return {"es_inmune": self.es_inmune, "tiene_alcanzame": self.tiene_alcanzame,"tiene_volveralavida": self.tiene_volveralavida}