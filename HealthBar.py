import pygame
from lenguajes import Lenguajes


class HealthBar:
    def __init__(self, x, y, w, h, max_hp, level_number):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp
        self.level_number = level_number
        # Cargar la fuente utilizada para "Salud" (reemplaza "nombre_de_tu_fuente.ttf" con el nombre de tu fuente)
        self.font = pygame.font.Font("Fonts/font.ttf", 16)
        if self.level_number == 1:
            self.remaining_time = 60
        elif self.level_number == 2:
            self.remaining_time = 60
        else:
            self.remaining_time = 60
        # Inicializar el tiempo restante a 60 segundos (1 minuto)
        # Establecer el tiempo de inicio
        self.start_time = pygame.time.get_ticks()
        self.saved_time = 0

    def pause(self):
        if self.saved_time == 0:
            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - self.start_time) / 1000
            self.saved_time = elapsed_time

    def restore(self):
        current_time = pygame.time.get_ticks()
        self.start_time = current_time - (self.saved_time * 1000)
        self.saved_time = 0

    def reset(self):
        self.remaining_time = 60
        self.start_time = pygame.time.get_ticks()

    def draw(self, surface, idioma):
        # Calcular la relación de salud
        ratio = self.hp / self.max_hp
        if ratio < 0:
            ratio = 0
        color2 = calcular_color(100 * ratio)

        if self.max_hp >= 100:
            self.max_hp = 100

        # Dibujar la barra de salud
        pygame.draw.rect(surface, "black", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, color2, (self.x, self.y, self.w * ratio, self.h))

        # Calcular el tiempo transcurrido
        current_time = pygame.time.get_ticks()
        elapsed_time = (
            current_time - self.start_time
        ) / 1000  # Tiempo transcurrido en segundos
        # Calcular el tiempo restante
        self.remaining_time = max(0, 60 - elapsed_time)  # 60 segundos es 1 minuto

        # Dibujar el contador de tiempo abajo a la derecha y un poco más a la derecha
        text_color = (255, 255, 255)  # Color inicial: blanco

        if self.remaining_time <= 10:
            text_color = (255, 0, 0)  # Cambiar a rojo cuando quedan 10 segundos

        idiomas_manager = Lenguajes()
        idiomas_manager.cambiar_idioma(idioma)
        title_text_info = idiomas_manager.obtener_traduccion("tiempo")
        title = title_text_info["texto"]

        text = self.font.render(
            f"{title}: {int(self.remaining_time)}s", True, text_color
        )
        text_rect = text.get_rect()
        # Ajusta las coordenadas x e y para la posición deseada
        text_rect.right = (
            self.x + self.w - 4.4
        )  # Ajustar la posición a la derecha de la barra de salud con un desplazamiento de 20 píxeles
        text_rect.bottom = (
            self.y + self.h - 6.5
        )  # Ajustar la posición en la parte inferior
        surface.blit(text, text_rect)


def calcular_color(porcentaje):
    verde = (0, 255, 0)
    rojo = (255, 0, 0)
    r = verde[0] - int((verde[0] - rojo[0]) * (1 - porcentaje / 100))
    g = verde[1] - int((verde[1] - rojo[1]) * (1 - porcentaje / 100))
    b = verde[2] - int((verde[2] - rojo[2]) * (1 - porcentaje / 100))
    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    return (r, g, b)
