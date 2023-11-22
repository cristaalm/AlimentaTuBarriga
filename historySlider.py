import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)

screen_width = 600
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image Slider")

# Cargar una fuente pixelada (reemplaza "pixel_font.ttf" con el nombre de tu archivo de fuente)
font = pygame.font.Font("Fonts/PressStart2P.ttf", 20)

# Definir las opciones
genero = "mujer"
idioma = "esp"
piel = "blanco"
# level_number = 2
imagenes = 17
image_list = []
for i in range(1, imagenes):
    image_list.append(pygame.image.load(f"img/{idioma}/{genero}/{piel}/{i}.png"))
    # image_list.append(pygame.image.load(f"img/{idioma}/{level_number}/{genero}/{piel}/{i}.png"))

current_image_index = 0

# Ajustar el tamaño de los botones
button_width = 80
button_height = 80

# Cargar imágenes de botones y ajustar su tamaño
prev_button_image = pygame.transform.scale(
    pygame.image.load("img/btn/btnArrowLeft.png"), (button_width, button_height)
)
next_button_image = pygame.transform.scale(
    pygame.image.load("img/btn/btnArrowRight.png"), (button_width, button_height)
)
prev_button_hover_image = pygame.transform.scale(
    pygame.image.load("img/btn/btnArrowLeftHover.png"), (button_width, button_height)
)
next_button_hover_image = pygame.transform.scale(
    pygame.image.load("img/btn/btnArrowRightHover.png"), (button_width, button_height)
)

# Ajustar posiciones de los botones y textos
button_margin = 10

# Mantener las coordenadas originales de los botones
prev_button_x = button_margin
prev_button_y = screen_height - button_height - button_margin

next_button_x = screen_width - button_width - button_margin
next_button_y = screen_height - button_height - button_margin

# Calcular nuevas coordenadas para el texto
prev_text_x = prev_button_x + (button_width - font.size("Anterior")[0]) // 2
next_text_x = next_button_x + (button_width - font.size("Siguiente")[0]) // 2

# Agregar botón central entre los dos botones inferiores
center_button_image = pygame.transform.scale(
    pygame.image.load("img/btn/btnPrincipal.png"), (button_width, button_height)
)
center_button_hover_image = pygame.transform.scale(
    pygame.image.load("img/btn/btnPrincipalHover.png"), (button_width, button_height)
)
center_button_x = (screen_width - button_width) // 2
center_button_y = next_button_y  # Mismo nivel que los botones inferiores

# Agregar imagen superior en medio
top_image = pygame.transform.scale(
    pygame.image.load("img/textoEnter.png"), (screen_width, 100)
)
top_image_rect = top_image.get_rect()
top_image_rect.center = (screen_width // 2, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Verificar si se hizo clic en el botón "Anterior"
                if (
                    prev_button_x
                    <= pygame.mouse.get_pos()[0]
                    <= prev_button_x + button_width
                    and prev_button_y
                    <= pygame.mouse.get_pos()[1]
                    <= prev_button_y + button_height
                ):
                    current_image_index = max(current_image_index - 1, 0)
                # Verificar si se hizo clic en el botón "Siguiente"
                elif (
                    next_button_x
                    <= pygame.mouse.get_pos()[0]
                    <= next_button_x + button_width
                    and next_button_y
                    <= pygame.mouse.get_pos()[1]
                    <= next_button_y + button_height
                ):
                    current_image_index = min(
                        current_image_index + 1, len(image_list) - 1
                    )
                # Verificar si se hizo clic en el botón "Centro"
                elif (
                    center_button_x
                    <= pygame.mouse.get_pos()[0]
                    <= center_button_x + button_width
                    and center_button_y
                    <= pygame.mouse.get_pos()[1]
                    <= center_button_y + button_height
                ):
                    # Aquí deberías agregar el código para ir a la pantalla de menú principal
                    print("Ir a Menú Principal")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_image_index = max(current_image_index - 1, 0)
            elif event.key == pygame.K_RIGHT:
                current_image_index = min(current_image_index + 1, len(image_list) - 1)
            elif event.key == pygame.K_ESCAPE:
                # Aquí deberías agregar el código para ir a la siguiente pantalla
                print("Ir a la Siguiente Pantalla")

    screen.fill(BLANCO)
    current_image = image_list[current_image_index]
    image_rect = current_image.get_rect()
    image_rect.center = (screen_width // 2, screen_height // 2)
    screen.blit(current_image, image_rect)

    # Verificar si el ratón está sobre los botones y mostrar la imagen correspondiente
    if (
        prev_button_x <= pygame.mouse.get_pos()[0] <= prev_button_x + button_width
        and prev_button_y <= pygame.mouse.get_pos()[1] <= prev_button_y + button_height
    ):
        screen.blit(prev_button_hover_image, (prev_button_x, prev_button_y))
    else:
        screen.blit(prev_button_image, (prev_button_x, prev_button_y))

    if (
        next_button_x <= pygame.mouse.get_pos()[0] <= next_button_x + button_width
        and next_button_y <= pygame.mouse.get_pos()[1] <= next_button_y + button_height
    ):
        screen.blit(next_button_hover_image, (next_button_x, next_button_y))
    else:
        screen.blit(next_button_image, (next_button_x, next_button_y))

    # Renderizar texto "Anterior" y "Siguiente" con las nuevas coordenadas
    prev_text = font.render("Anterior", True, BLANCO)
    next_text = font.render("Siguiente", True, BLANCO)

    screen.blit(prev_text, (prev_text_x, prev_button_y - 25))
    screen.blit(next_text, (next_text_x, next_button_y - 25))

    # Renderizar botón "Centro" en la pantalla
    if (
        center_button_x <= pygame.mouse.get_pos()[0] <= center_button_x + button_width
        and center_button_y
        <= pygame.mouse.get_pos()[1]
        <= center_button_y + button_height
    ):
        screen.blit(center_button_hover_image, (center_button_x, center_button_y))
    else:
        screen.blit(center_button_image, (center_button_x, center_button_y))

    # Renderizar imagen superior en medio
    screen.blit(top_image, top_image_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
