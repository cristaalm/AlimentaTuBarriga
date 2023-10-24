import math,pygame
from pygame import font
screen_width, screen_height = 600, 750
screen = pygame.display.set_mode((screen_width, screen_height))
font.init()
fuente = pygame.font.Font('./Fonts/GeneraleStationGX.ttf', 20)
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 50:
        return True
    else:
        return False

def mostrar_puntaje(x, y,puntaje):
    texto = fuente.render(f"Salud: {puntaje}", True, (255, 255, 255))
    screen.blit(texto, (x, y))
    
def draw_game_over_screen():
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont('arial', 40)
   title = font.render('Game Over', True, (255, 255, 255))
#    restart_button = font.render('R - Restart', True, (255, 255, 255))
   quit_button = font.render('Q - Quit', True, (255, 255, 255))
   screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/3))
#    screen.blit(restart_button, (screen_width/2 - restart_button.get_width()/2, screen_height/1.9 + restart_button.get_height()))
   screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2))
   pygame.display.update()