import pygame, sys, random, math
import pygame.freetype
import cv2
from pruebaBTN import Button
import button
import button2
import button3
import pygame_gui
import comidaModel
import player2 as player
import friend
from lenguajes import Lenguajes
from HealthBar import HealthBar
from level1HB2 import level1HB

# from pyvidplayer import Video
from funciones import (
    hay_colision,
    draw_game_over_screen,
    draw_pause_screen,
    mostrar_puntaje,
    puntajeComida,
    draw_winner_screen,
    info,
    pociones,
)

pygame.init()
pygame.mixer.init()

width = 600
height = 750
SCREEN = pygame.display.set_mode((width, height))
button_x = 100
button_y = 100
BG = pygame.image.load("img/fondom.jpg")
BG1 = pygame.image.load("img/fondom.jpg")
BGAzul = "#2887BF"
BGAzulHB = pygame.image.load("img/bgAzulHB.png")
BGRosaM = pygame.image.load("img/bgRosaHB.png")
creadoresfondo = pygame.image.load("img/creatorsPage.png")

# Diccionario de Lenguajes()
idiomas_manager = Lenguajes()

# Coordenadas del mono
coord_x = 215
coord_y = 650
# Velocidad
x_speed = 0
y_speed = 0
sentido = 1
# barra= pygame.draw.rect(screen,'white',)

tipo_comida = 0
texto_puntaje = []
puntaje = 50
texto_x = 20
texto_y = 27
done = False
foods_and_junk = []
game_state = "startgame"

# Nos permite controlar los frame
clock = pygame.time.Clock()
# Ingresamos fondo
backgroundDay = pygame.image.load("./img/dia.png").convert()

logo_img = pygame.image.load("img/logo.png").convert_alpha()
# logo_img = pygame.transform.scale(logo_img, (550, 200))
logo_img = button2.Button(38, 170, logo_img, 0.31)
btnReturn = Button(
    40,
    40,
    pygame.image.load("./img/btn/btnReturn.png").convert_alpha(),
    pygame.image.load("./img/btn/btnReturnHover.png").convert_alpha(),
    0.2,
)

# Cargamos las imágenes cómo botones
btnEnter = pygame.image.load("img/btn/btnEnter.png").convert_alpha()
btnEnter = pygame.transform.scale(btnEnter, (100, 100))
btnEnter = button.Button(450, 540, btnEnter, 0.8)
# Creamos instancias del botón
showGirl = False
showBoy = False

color_claro = pygame.image.load("img/hombre/hombreBlanco.png").convert_alpha()
color_claro = pygame.transform.scale(color_claro, (300, 350))
color_claro = button.Button(180, 125, color_claro, 0.9)
color_oscuro = pygame.image.load("img/hombre/hombreMoreno.png").convert_alpha()
color_oscuro = pygame.transform.scale(color_oscuro, (300, 350))
color_oscuro = button.Button(180, 125, color_oscuro, 0.9)

color_claroM = pygame.image.load("img/mujer/mujerBlanca.png").convert_alpha()
color_claroM = pygame.transform.scale(color_claroM, (300, 350))
color_claroM = button.Button(180, 125, color_claroM, 0.9)
color_oscuroM = pygame.image.load("img/mujer/mujerMorena.png").convert_alpha()
color_oscuroM = pygame.transform.scale(color_oscuroM, (300, 350))
color_oscuroM = button.Button(180, 125, color_oscuroM, 0.9)

# b_wood = pygame.image.load("img/wood.png").convert_alpha()
# b_wood = pygame.transform.scale(b_wood, (590, 115))
# b_wood = button.Button(10, 639, b_wood, 0.99)

clock = pygame.time.Clock()
background = pygame.image.load("img/presionaAzul.png")
background = pygame.transform.scale(background, (600, 750))
backgroundRosa = pygame.image.load("img/presionaEnterR.png")
backgroundRosa = pygame.transform.scale(backgroundRosa, (600, 750))

bgIdiomas = pygame.image.load("img/bgIdiomas.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Fonts/PressStart2P.ttf", size)


def tecladoNinaMorena():
    ingNombre = idiomas_manager.obtener_traduccion("ingNombre")
    ingNombreTitle = get_font(ingNombre["size"]).render(
        ingNombre["texto"], True, "black"
    )
    ingNombreTitle_rect = ingNombreTitle.get_rect(center=(300, 465))
    presione = idiomas_manager.obtener_traduccion("presione")
    presioneTitle = get_font(presione["size"]).render(presione["texto"], True, "black")
    presioneTitle_rect = presioneTitle.get_rect(center=(150, 570))
    paCon = idiomas_manager.obtener_traduccion("paCon")
    paConTitle = get_font(paCon["size"]).render(paCon["texto"], True, "black")
    paConTitle_rect = paConTitle.get_rect(center=(400, 570))
    nombre_personaje = ""
    genero = ""
    piel = ""
    # Se crea un objeto manager que actúa como un administrador de interfaz de usuario para el juego.
    manager = pygame_gui.UIManager((width, height))
    # Se está creando un objeto btnReturn de la clase Button. Este botón se utiliza en la interfaz de usuario del juego.
    btnReturn = Button(
        40,
        40,
        pygame.image.load("./img/btn/btnReturn.png").convert_alpha(),
        pygame.image.load("./img/btn/btnReturnHover.png").convert_alpha(),
        0.2,
    )
    # Esta linea de codigo crea un campo de entrada de texto en la interfaz de juego con una posicion y un tamaño especificos y lo asignamos
    # al administrador de interfaz de usuario para su gestion
    text_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((100, 485), (400, 50)),
        manager=manager,
        object_id="#main_text_entry",
    )

    title_text_info = idiomas_manager.obtener_traduccion("nombre")
    title = title_text_info["texto"]
    pygame.display.set_caption(f"{title} - Alimenta Tu Barriga")
    # OPTIONS_TEXT = get_font(20).render("De favor, ingrese su nombre:", True, "white")
    # OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(310, 450))

    while True:
        UI_REFRESH_RATE = clock.tick(60) / 1000
        # Este bucle recorre todos los eventos en la cola de eventos de Pygame
        for event in pygame.event.get():
            # Comprueba si el usuario intento cerrar el juego, si es asi cierra el juego
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # Comprueba si el usuarion presionó una tecla, en este caso return la tecla return, verifica si la variable nombre esta
                # vacia, si es asi pone un nombre por defecto Liz y establece el tono de piel y finalmente comprueba los datos
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if nombre_personaje == "":
                        nombre_personaje = "Liz"
                    genero = "mujer"
                    piel = "moreno"
                    prueba(nombre_personaje, genero, piel)
                    # continue
                    # comprueba si fue presionada la tecla retroceso, si es asi permite al usuario borrar el ultimo caracter
                elif event.key == pygame.K_BACKSPACE:
                    nombre_personaje = nombre_personaje[
                        :-1
                    ]  # Borrar el último carácter
                else:
                    nombre_personaje += event.unicode
                    # Agregar el carácter ingresado al nombre
                    # comprueba si el usuario termino de ingresar texto
            if (
                event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED
                and event.ui_object_id == "#main_text_entry"
            ):
                # Mostrar el nombre ingresado en tiempo real
                NAME_TEXT = get_font(100).render(nombre_personaje, True, "white")
                NAME_RECT = NAME_TEXT.get_rect(center=(width // 2, 500))
                SCREEN.blit(NAME_TEXT, NAME_RECT)
                pygame.display.update()
                # start()
            manager.process_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if btnReturn.is_hover(mouse_x, mouse_y):
                    mostrarMujer()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if btnReturn.is_hover(mouse_x, mouse_y):
            btnReturn.change_image(btnReturn.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnReturn.change_image(btnReturn.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        manager.update(UI_REFRESH_RATE)

        # Limpiar la pantalla
        SCREEN.blit(BGRosaM, [0, 0])
        btnReturn.draw(SCREEN)

        # Dibujar el texto pixeleado
        # SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        text_input.focus()
        color_oscuroM.draw(SCREEN)
        manager.draw_ui(SCREEN)
        # btnEnter.draw(SCREEN)
        SCREEN.blit(ingNombreTitle, ingNombreTitle_rect)
        SCREEN.blit(presioneTitle, presioneTitle_rect)
        SCREEN.blit(paConTitle, paConTitle_rect)
        pygame.display.update()


def tecladoNinaBlanca():
    ingNombre = idiomas_manager.obtener_traduccion("ingNombre")
    ingNombreTitle = get_font(ingNombre["size"]).render(
        ingNombre["texto"], True, "black"
    )
    ingNombreTitle_rect = ingNombreTitle.get_rect(center=(300, 465))
    presione = idiomas_manager.obtener_traduccion("presione")
    presioneTitle = get_font(presione["size"]).render(presione["texto"], True, "black")
    presioneTitle_rect = presioneTitle.get_rect(center=(150, 570))
    paCon = idiomas_manager.obtener_traduccion("paCon")
    paConTitle = get_font(paCon["size"]).render(paCon["texto"], True, "black")
    paConTitle_rect = paConTitle.get_rect(center=(400, 570))
    nombre_personaje = ""
    genero = ""
    piel = ""
    manager = pygame_gui.UIManager((width, height))
    btnReturn = Button(
        40,
        40,
        pygame.image.load("./img/btn/btnReturn.png").convert_alpha(),
        pygame.image.load("./img/btn/btnReturnHover.png").convert_alpha(),
        0.2,
    )

    text_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((100, 485), (400, 50)),
        manager=manager,
        object_id="#main_text_entry",
    )

    while True:
        UI_REFRESH_RATE = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if nombre_personaje == "":
                        nombre_personaje = "Liz"
                    genero = "mujer"
                    piel = "blanco"
                    prueba(nombre_personaje, genero, piel)
                    # continue
                elif event.key == pygame.K_BACKSPACE:
                    nombre_personaje = nombre_personaje[
                        :-1
                    ]  # Borrar el último carácter
                else:
                    nombre_personaje += event.unicode
                    # Agregar el carácter ingresado al nombre
            if (
                event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED
                and event.ui_object_id == "#main_text_entry"
            ):
                # Mostrar el nombre ingresado en tiempo real
                NAME_TEXT = get_font(100).render(nombre_personaje, True, "white")
                NAME_RECT = NAME_TEXT.get_rect(center=(width // 2, 500))
                SCREEN.blit(NAME_TEXT, NAME_RECT)
                pygame.display.update()
                # start()
            manager.process_events(event)
            #: Esta línea verifica si se ha producido un evento de clic del ratón (mouse click)
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Aquí se obtienen las coordenadas del cursor del ratón en la ventana y se almacenan en las variables
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Esta línea verifica si el cursor del ratón está sobre el botón btnreturn
                if btnReturn.is_hover(mouse_x, mouse_y):
                    # si se hace clic entonces se ejecuta la funcion main menu, es decir te regresa al menu
                    mostrarMujer()
                    # Después de verificar si el cursor del ratón está sobre el botón, se vuelven a obtener
                    # las coordenadas del cursor del ratón
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Verifica si el raton esta sobre el btn return
        if btnReturn.is_hover(mouse_x, mouse_y):
            # Si el cursor está sobre el botón, se cambia la imagen del botón a su estado de "hover", esto indica que se puede interactuar
            btnReturn.change_image(btnReturn.hover_image)
            # Esto proporciona retroalimentación visual al usuario, indicando que el botón se puede hacer clic
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnReturn.change_image(btnReturn.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        manager.update(UI_REFRESH_RATE)

        # Limpiar la pantalla
        SCREEN.blit(BGRosaM, [0, 0])
        btnReturn.draw(SCREEN)

        # Dibujar el texto pixeleado
        # SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        text_input.focus()
        color_claroM.draw(SCREEN)
        manager.draw_ui(SCREEN)
        # btnEnter.draw(SCREEN)
        SCREEN.blit(ingNombreTitle, ingNombreTitle_rect)
        SCREEN.blit(presioneTitle, presioneTitle_rect)
        SCREEN.blit(paConTitle, paConTitle_rect)
        pygame.display.update()


def mostrarMujer():
    title_text_info = idiomas_manager.obtener_traduccion("niña2")
    title = title_text_info["texto"]
    pygame.display.set_caption(f"{title} - Alimenta Tu Barriga")

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        title_text_info = idiomas_manager.obtener_traduccion("seleccionaPersonaje")
        title = title_text_info["texto"]
        OPTIONS_TEXT = get_font(20).render(title, True, "black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(290, 630))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        btnReturn = Button(
            40,
            40,
            pygame.image.load("./img/btn/btnReturn.png").convert_alpha(),
            pygame.image.load("./img/btn/btnReturnHover.png").convert_alpha(),
            0.2,
        )
        btnBlanco = Button(
            5,
            200,
            pygame.image.load("./img/btn/btnBlanca.png").convert_alpha(),
            pygame.image.load("./img/btn/btnBlancaHover.png").convert_alpha(),
            0.8,
        )
        btnMoreno = Button(
            280,
            200,
            pygame.image.load("./img/btn/btMorena.png").convert_alpha(),
            pygame.image.load("./img/btn/btMorenaHover.png").convert_alpha(),
            0.8,
        )
        btnReturn.draw(SCREEN)
        btnBlanco.draw(SCREEN)
        btnMoreno.draw(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if btnReturn.is_hover(mouse_x, mouse_y):
                    play()
                if btnBlanco.is_hover(mouse_x, mouse_y):
                    tecladoNinaBlanca()
                if btnMoreno.is_hover(mouse_x, mouse_y):
                    tecladoNinaMorena()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if btnReturn.is_hover(mouse_x, mouse_y):
            btnReturn.change_image(btnReturn.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnReturn.change_image(btnReturn.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if btnBlanco.is_hover(mouse_x, mouse_y):
            btnBlanco.change_image(btnBlanco.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnBlanco.change_image(btnBlanco.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if btnMoreno.is_hover(mouse_x, mouse_y):
            btnMoreno.change_image(btnMoreno.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnMoreno.change_image(btnMoreno.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        btnBlanco.draw(SCREEN)
        btnMoreno.draw(SCREEN)
        btnReturn.draw(SCREEN)

        pygame.display.update()

    # Función para mostrar la ventana de selectColorH


def mostrarHombre():
    title_text_info = idiomas_manager.obtener_traduccion("niño2")
    title = title_text_info["texto"]
    pygame.display.set_caption(f"{title} - Alimenta Tu Barriga")
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")
        title_text_info = idiomas_manager.obtener_traduccion("seleccionaPersonaje")
        title = title_text_info["texto"]
        OPTIONS_TEXT = get_font(20).render(title, True, "black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(290, 630))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        btnReturn = Button(
            40,
            40,
            pygame.image.load("./img/btn/btnReturn.png").convert_alpha(),
            pygame.image.load("./img/btn/btnReturnHover.png").convert_alpha(),
            0.2,
        )
        btnBlanco = Button(
            5,
            200,
            pygame.image.load("./img/btn/btnBlanco.png").convert_alpha(),
            pygame.image.load("./img/btn/btnBlancoHover.png").convert_alpha(),
            0.8,
        )
        btnMoreno = Button(
            280,
            200,
            pygame.image.load("./img/btn/btnMoreno.png").convert_alpha(),
            pygame.image.load("./img/btn/btnMorenoHover.png").convert_alpha(),
            0.8,
        )
        btnReturn.draw(SCREEN)
        btnBlanco.draw(SCREEN)
        btnMoreno.draw(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if btnReturn.is_hover(mouse_x, mouse_y):
                    play()
                if btnBlanco.is_hover(mouse_x, mouse_y):
                    tecladoNinoBlanco()
                if btnMoreno.is_hover(mouse_x, mouse_y):
                    tecladoNinoMoreno()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if btnReturn.is_hover(mouse_x, mouse_y):
            btnReturn.change_image(btnReturn.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnReturn.change_image(btnReturn.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if btnBlanco.is_hover(mouse_x, mouse_y):
            btnBlanco.change_image(btnBlanco.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnBlanco.change_image(btnBlanco.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if btnMoreno.is_hover(mouse_x, mouse_y):
            btnMoreno.change_image(btnMoreno.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnMoreno.change_image(btnMoreno.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        btnBlanco.draw(SCREEN)
        btnMoreno.draw(SCREEN)
        btnReturn.draw(SCREEN)

        pygame.display.update()


def tecladoNinoBlanco():
    ingNombre = idiomas_manager.obtener_traduccion("ingNombre")
    ingNombreTitle = get_font(ingNombre["size"]).render(
        ingNombre["texto"], True, "white"
    )
    ingNombreTitle_rect = ingNombreTitle.get_rect(center=(300, 465))
    presione = idiomas_manager.obtener_traduccion("presione")
    presioneTitle = get_font(presione["size"]).render(presione["texto"], True, "white")
    presioneTitle_rect = presioneTitle.get_rect(center=(150, 570))
    paCon = idiomas_manager.obtener_traduccion("paCon")
    paConTitle = get_font(paCon["size"]).render(paCon["texto"], True, "white")
    paConTitle_rect = paConTitle.get_rect(center=(400, 570))
    nombre_personaje = ""
    genero = ""
    piel = ""
    manager = pygame_gui.UIManager((width, height))
    btnReturn = Button(
        40,
        40,
        pygame.image.load("./img/btn/btnReturn.png").convert_alpha(),
        pygame.image.load("./img/btn/btnReturnHover.png").convert_alpha(),
        0.2,
    )

    text_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((100, 485), (400, 50)),
        manager=manager,
        object_id="#main_text_entry",
    )

    title_text_info = idiomas_manager.obtener_traduccion("nombre")
    title = title_text_info["texto"]
    pygame.display.set_caption(f"{title} - Alimenta Tu Barriga")
    # OPTIONS_TEXT = get_font(20).render("De favor, ingrese su nombre:", True, "white")
    # OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(310, 450))

    while True:
        UI_REFRESH_RATE = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if nombre_personaje == "":
                        nombre_personaje = "Tadeo"
                    genero = "hombre"
                    piel = "blanco"
                    prueba(nombre_personaje, genero, piel)
                    # continue
                elif event.key == pygame.K_BACKSPACE:
                    nombre_personaje = nombre_personaje[
                        :-1
                    ]  # Borrar el último carácter
                else:
                    nombre_personaje += event.unicode
                    # Agregar el carácter ingresado al nombre
            if (
                event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED
                and event.ui_object_id == "#main_text_entry"
            ):
                # Mostrar el nombre ingresado en tiempo real
                NAME_TEXT = get_font(100).render(nombre_personaje, True, "white")
                NAME_RECT = NAME_TEXT.get_rect(center=(width // 2, 500))
                SCREEN.blit(NAME_TEXT, NAME_RECT)
                pygame.display.update()
                # start()
            manager.process_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if btnReturn.is_hover(mouse_x, mouse_y):
                    mostrarHombre()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if btnReturn.is_hover(mouse_x, mouse_y):
            btnReturn.change_image(btnReturn.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnReturn.change_image(btnReturn.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        manager.update(UI_REFRESH_RATE)

        # Limpiar la pantalla
        SCREEN.blit(BGAzulHB, [0, 0])
        btnReturn.draw(SCREEN)

        # Dibujar el texto pixeleado
        # SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        text_input.focus()
        color_claro.draw(SCREEN)
        manager.draw_ui(SCREEN)
        # btnEnter.draw(SCREEN)
        SCREEN.blit(ingNombreTitle, ingNombreTitle_rect)
        SCREEN.blit(presioneTitle, presioneTitle_rect)
        SCREEN.blit(paConTitle, paConTitle_rect)
        pygame.display.update()


def tecladoNinoMoreno():
    ingNombre = idiomas_manager.obtener_traduccion("ingNombre")
    ingNombreTitle = get_font(ingNombre["size"]).render(
        ingNombre["texto"], True, "white"
    )
    ingNombreTitle_rect = ingNombreTitle.get_rect(center=(300, 465))
    presione = idiomas_manager.obtener_traduccion("presione")
    presioneTitle = get_font(presione["size"]).render(presione["texto"], True, "white")
    presioneTitle_rect = presioneTitle.get_rect(center=(150, 570))
    paCon = idiomas_manager.obtener_traduccion("paCon")
    paConTitle = get_font(paCon["size"]).render(paCon["texto"], True, "white")
    paConTitle_rect = paConTitle.get_rect(center=(400, 570))
    nombre_personaje = ""
    genero = ""
    piel = ""
    manager = pygame_gui.UIManager((width, height))
    btnReturn = Button(
        40,
        40,
        pygame.image.load("./img/btn/btnReturn.png").convert_alpha(),
        pygame.image.load("./img/btn/btnReturnHover.png").convert_alpha(),
        0.2,
    )

    text_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((100, 485), (400, 50)),
        manager=manager,
        object_id="#main_text_entry",
    )

    title_text_info = idiomas_manager.obtener_traduccion("nombre")
    title = title_text_info["texto"]
    pygame.display.set_caption(f"{title} - Alimenta Tu Barriga")
    while True:
        UI_REFRESH_RATE = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if nombre_personaje == "":
                        nombre_personaje = "Tadeo"
                    genero = "hombre"
                    piel = "moreno"
                    prueba(nombre_personaje, genero, piel)
                    # continue
                elif event.key == pygame.K_BACKSPACE:
                    nombre_personaje = nombre_personaje[
                        :-1
                    ]  # Borrar el último carácter
                else:
                    nombre_personaje += event.unicode
                    # Agregar el carácter ingresado al nombre
            if (
                event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED
                and event.ui_object_id == "#main_text_entry"
            ):
                # Mostrar el nombre ingresado en tiempo real
                NAME_TEXT = get_font(100).render(nombre_personaje, True, "white")
                NAME_RECT = NAME_TEXT.get_rect(center=(width // 2, 500))
                SCREEN.blit(NAME_TEXT, NAME_RECT)
                pygame.display.update()
                # start()
            manager.process_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if btnReturn.is_hover(mouse_x, mouse_y):
                    mostrarHombre()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if btnReturn.is_hover(mouse_x, mouse_y):
            btnReturn.change_image(btnReturn.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnReturn.change_image(btnReturn.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        manager.update(UI_REFRESH_RATE)

        # Limpiar la pantalla
        SCREEN.blit(BGAzulHB, [0, 0])
        btnReturn.draw(SCREEN)

        # Dibujar el texto pixeleado
        # SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        text_input.focus()
        color_oscuro.draw(SCREEN)
        manager.draw_ui(SCREEN)
        # btnEnter.draw(SCREEN)
        SCREEN.blit(ingNombreTitle, ingNombreTitle_rect)
        SCREEN.blit(presioneTitle, presioneTitle_rect)
        SCREEN.blit(paConTitle, paConTitle_rect)
        pygame.display.update()


def instrucciones(nombre, genero, piel):
    title_text_info = idiomas_manager.obtener_traduccion("instrucciones")
    title = title_text_info["texto"]
    pygame.display.set_caption(f"{title} - Alimenta Tu Barriga")

    idioma_actual = idiomas_manager.obtener_idioma()
    instrucciones_path = f"img/instrucciones/1/{genero}_{piel}_{idioma_actual}.png"
    instruccionesHB = pygame.image.load(instrucciones_path).convert()
    instruccionesHB = pygame.transform.scale(instruccionesHB, (600, 750))
    # Agregar imagen superior en medio
    top_image = pygame.transform.scale(
        pygame.image.load(f"img/textoEnterN_{idioma_actual}.png"), (width - 230, 60)
    )
    top_image_rect = top_image.get_rect()
    if idioma_actual == "español":
        top_image_rect.center = (width // 2, 115)
    else:
        top_image_rect.center = (width // 2, 45)

    tiempo_fin = pygame.time.get_ticks() + 10000
    success = True
    while pygame.time.get_ticks() < tiempo_fin and success:
        SCREEN.blit(instruccionesHB, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    success = False
        SCREEN.blit(top_image, top_image_rect)
        pygame.display.update()
    level1(nombre, genero, piel, 1, 100, idiomas_manager.obtener_idioma())


def start(nombre, genero, piel):
    title_text_info = idiomas_manager.obtener_traduccion("historia")
    title = title_text_info["texto"]
    pygame.display.set_caption(f"{title} - Alimenta Tu Barriga")
    font = pygame.font.Font("Fonts/PressStart2P.ttf", 20)
    idioma = idiomas_manager.obtener_idioma()
    BLANCO = (255, 255, 255)
    imagenes = 17
    image_list = []
    # img/español/1/hombre/blanco/1.png
    for i in range(1, imagenes):
        # image_list.append(pygame.image.load(f"img/{idioma}/{genero}/{piel}/{i}.png"))
        image_list.append(pygame.image.load(f"img/{idioma}/1/{genero}/{piel}/{i}.png"))

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
        pygame.image.load("img/btn/btnArrowLeftHover.png"),
        (button_width, button_height),
    )
    next_button_hover_image = pygame.transform.scale(
        pygame.image.load("img/btn/btnArrowRightHover.png"),
        (button_width, button_height),
    )

    # Ajustar posiciones de los botones y textos
    button_margin = 10

    # Mantener las coordenadas originales de los botones
    prev_button_x = button_margin + 70
    prev_button_y = height - button_height - button_margin

    next_button_x = width - 70 - button_width - button_margin
    next_button_y = height - button_height - button_margin

    # Agregar botón central entre los dos botones inferiores
    center_button_image = pygame.transform.scale(
        pygame.image.load("img/btn/btnPrincipal.png"), (button_width, button_height)
    )
    center_button_hover_image = pygame.transform.scale(
        pygame.image.load("img/btn/btnPrincipalHover.png"),
        (button_width, button_height),
    )
    center_button_x = (width - button_width) // 2
    center_button_y = next_button_y  # Mismo nivel que los botones inferiores

    # Agregar imagen superior en medio
    top_image = pygame.transform.scale(
        pygame.image.load(f"img/textoEnter_{idioma}.png"), (width - 100, 80)
    )
    top_image_rect = top_image.get_rect()
    top_image_rect.center = (width // 2, 50)

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
                        if current_image_index == 0:
                            prueba(nombre, genero, piel)
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
                        if current_image_index == len(image_list) - 1:
                            instrucciones(nombre, genero, piel)
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
                        main_menu()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_image_index = max(current_image_index - 1, 0)
                    if current_image_index == 0:
                        prueba(nombre, genero, piel)
                elif event.key == pygame.K_RIGHT:
                    current_image_index = min(
                        current_image_index + 1, len(image_list) - 1
                    )
                    if current_image_index == len(image_list) - 1:
                        instrucciones(nombre, genero, piel)
                elif event.key == pygame.K_ESCAPE:
                    # Aquí deberías agregar el código para ir a la siguiente pantalla
                    print("Ir a la Siguiente Pantalla")
                    instrucciones(nombre, genero, piel)
        SCREEN.fill(BLANCO)
        current_image = image_list[current_image_index]
        image_rect = current_image.get_rect()
        image_rect.center = (width // 2, height // 2)
        SCREEN.blit(current_image, image_rect)
        # b_wood.draw(SCREEN)

        # Verificar si el ratón está sobre los botones y mostrar la imagen correspondiente
        if (
            prev_button_x <= pygame.mouse.get_pos()[0] <= prev_button_x + button_width
            and prev_button_y
            <= pygame.mouse.get_pos()[1]
            <= prev_button_y + button_height
        ):
            SCREEN.blit(prev_button_hover_image, (prev_button_x, prev_button_y + 2))
        else:
            SCREEN.blit(prev_button_image, (prev_button_x, prev_button_y + 2))

        if (
            next_button_x <= pygame.mouse.get_pos()[0] <= next_button_x + button_width
            and next_button_y
            <= pygame.mouse.get_pos()[1]
            <= next_button_y + button_height
        ):
            SCREEN.blit(next_button_hover_image, (next_button_x, next_button_y + 2))
        else:
            SCREEN.blit(next_button_image, (next_button_x, next_button_y + 2))

        # Renderizar texto "Anterior" y "Siguiente" con las nuevas coordenadas
        prev_text = font.render("Anterior", True, BLANCO)
        next_text = font.render("Siguiente", True, BLANCO)

        # SCREEN.blit(prev_text, (prev_text_x, prev_button_y - 25))
        # SCREEN.blit(next_text, (next_text_x, next_button_y - 25))

        # Renderizar botón "Centro" en la pantalla
        if (
            center_button_x
            <= pygame.mouse.get_pos()[0]
            <= center_button_x + button_width
            and center_button_y
            <= pygame.mouse.get_pos()[1]
            <= center_button_y + button_height
        ):
            SCREEN.blit(center_button_hover_image, (center_button_x, center_button_y))
        else:
            SCREEN.blit(center_button_image, (center_button_x, center_button_y))

        # Renderizar imagen superior en medio
        SCREEN.blit(top_image, top_image_rect)
        pygame.display.update()

    instrucciones(nombre, genero, piel)


def prueba(nombre, genero, piel):
    startLevel = False
    title_text_info = idiomas_manager.obtener_traduccion("bH")
    title = title_text_info["texto"]

    pygame.display.set_caption(f"{title} - Alimenta Tu Barriga")
    while True:
        NAME_TEXT = get_font(25).render(f"{title}, {nombre}", True, "white")
        NAME_RECT = NAME_TEXT.get_rect(center=(300, 350))
        if startLevel:
            start(nombre, genero, piel)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start(nombre, genero, piel)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if btnReturn.is_hover(mouse_x, mouse_y):
                    if genero == "mujer":
                        if piel == "blanco":
                            tecladoNinaBlanca()
                        else:
                            tecladoNinaMorena()
                    else:
                        if piel == "blanco":
                            tecladoNinoBlanco()
                        else:
                            tecladoNinoMoreno()
        if genero == "mujer":
            title_text_info = idiomas_manager.obtener_traduccion("bG")
            title = title_text_info["texto"]
            pygame.display.set_caption(f"{title} - Alimenta Tu Barriga")
            presione = idiomas_manager.obtener_traduccion("presione")
            presioneTitle = get_font(presione["size"]).render(
                presione["texto"], True, "black"
            )
            presioneTitle_rect = presioneTitle.get_rect(center=(150, 400))
            paCon = idiomas_manager.obtener_traduccion("paCon")
            paConTitle = get_font(paCon["size"]).render(paCon["texto"], True, "black")
            paConTitle_rect = paConTitle.get_rect(center=(380, 400))

            NAME_TEXT = get_font(25).render(f"{title}, {nombre}", True, "black")
            NAME_RECT = NAME_TEXT.get_rect(center=(300, 350))

            SCREEN.blit(backgroundRosa, [0, 0])
        else:
            presione = idiomas_manager.obtener_traduccion("presione")
            presioneTitle = get_font(presione["size"]).render(
                presione["texto"], True, "white"
            )
            presioneTitle_rect = presioneTitle.get_rect(center=(150, 400))
            paCon = idiomas_manager.obtener_traduccion("paCon")
            paConTitle = get_font(paCon["size"]).render(paCon["texto"], True, "white")
            paConTitle_rect = paConTitle.get_rect(center=(380, 400))

            SCREEN.blit(background, [0, 0])
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if btnReturn.is_hover(mouse_x, mouse_y):
            btnReturn.change_image(btnReturn.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnReturn.change_image(btnReturn.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        SCREEN.blit(NAME_TEXT, NAME_RECT)
        btnReturn.draw(SCREEN)
        SCREEN.blit(presioneTitle, presioneTitle_rect)
        SCREEN.blit(paConTitle, paConTitle_rect)
        pygame.display.update()


def play():
    while True:
        title_text_info = idiomas_manager.obtener_traduccion("personalizable")
        title = title_text_info["texto"]
        pygame.display.set_caption(f"{title} - Alimenta Tu Barriga")
        # mando a llamar el texto 'text' and'size'
        infoNina = idiomas_manager.obtener_traduccion("niña")
        nina = infoNina["texto"]
        # mando a llamar el texto 'text and 'size'
        infoNino = idiomas_manager.obtener_traduccion("niño")
        nino = infoNino["texto"]

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        btnNina = Button(
            -2,
            200,
            pygame.image.load("./img/btn/btnNina.png").convert_alpha(),
            pygame.image.load("./img/btn/btnNinaHover.png").convert_alpha(),
            0.8,
        )
        btnNino = Button(
            283,
            200,
            pygame.image.load("./img/btn/btnNino.png").convert_alpha(),
            pygame.image.load("./img/btn/btnNinoHover.png").convert_alpha(),
            0.8,
        )
        btnReturn = Button(
            40,
            40,
            pygame.image.load("./img/btn/btnReturn.png").convert_alpha(),
            pygame.image.load("./img/btn/btnReturnHover.png").convert_alpha(),
            0.2,
        )
        btnReturn.draw(SCREEN)
        btnNina.draw(SCREEN)
        btnNino.draw(SCREEN)

        G_BUTTON = button3.Button(
            image=None,
            pos=(150, 650),
            text_input=nina,
            font=get_font(39),
            base_color="#FF4076",
            hovering_color="black",
        )
        B_BUTTON = button3.Button(
            image=None,
            pos=(450, 650),
            text_input=nino,
            font=get_font(39),
            base_color="#2887BF",
            hovering_color="black",
        )

        SCREEN.blit(BG1, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if btnReturn.is_hover(mouse_x, mouse_y):
                    main_menu()
                if btnNino.is_hover(mouse_x, mouse_y):
                    mostrarHombre()
                if btnNina.is_hover(mouse_x, mouse_y):
                    mostrarMujer()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if btnReturn.is_hover(mouse_x, mouse_y):
            btnReturn.change_image(btnReturn.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnReturn.change_image(btnReturn.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if btnNina.is_hover(mouse_x, mouse_y):
            btnNina.change_image(btnNina.hover_image)
            G_BUTTON.changeColor(MENU_MOUSE_POS)
            G_BUTTON.update(SCREEN)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnNina.change_image(btnNina.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if btnNino.is_hover(mouse_x, mouse_y):
            btnNino.change_image(btnNino.hover_image)
            B_BUTTON.changeColor(MENU_MOUSE_POS)
            B_BUTTON.update(SCREEN)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnNino.change_image(btnNino.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        btnNino.draw(SCREEN)
        btnNina.draw(SCREEN)
        btnReturn.draw(SCREEN)

        pygame.display.update()


def level1(nombre_personaje, genero, piel, level_number, puntajeAnt, idioma):
    from level1HB2 import level1HB

    title_text_info = idiomas_manager.obtener_traduccion("nivel")
    title = title_text_info["texto"]
    pygame.display.set_caption(f"{title} {level_number} - Alimenta Tu Barriga")

    level = level1HB()
    level.Run(
        genero, "delgado", piel, nombre_personaje, level_number, puntajeAnt, idioma
    )


# Define dos nuevas variables para almacenar las imágenes de los botones seleccionados
btnMexSelected = pygame.image.load("img/btn/btnMexicoHover.png").convert_alpha()
btnUSASelected = pygame.image.load("img/btn/btnUSAHover.png").convert_alpha()


def options():
    while True:
        title_text_info = idiomas_manager.obtener_traduccion("configuracion")
        title = title_text_info["texto"]
        pygame.display.set_caption(f"{title} - Alimenta Tu Barriga")

        btnMex = Button(
            100,
            260,
            pygame.image.load("img/btn/btnMexico.png").convert_alpha(),
            pygame.image.load("img/btn/btnMexicoHover.png").convert_alpha(),
            1,
        )
        btnUSA = Button(
            100,
            460,
            pygame.image.load("img/btn/btnUSA.png").convert_alpha(),
            pygame.image.load("img/btn/btnUSAHover.png").convert_alpha(),
            1,
        )
        btnReturn = Button(
            40,
            40,
            pygame.image.load("./img/btn/btnReturn.png").convert_alpha(),
            pygame.image.load("./img/btn/btnReturnHover.png").convert_alpha(),
            0.2,
        )

        # Texto
        mx = idiomas_manager.obtener_traduccion("mx")
        mxTitle = get_font(mx["size"]).render(mx["texto"], True, "white")
        mxTitle_rect = mxTitle.get_rect(center=(350, 320))
        usa = idiomas_manager.obtener_traduccion("usa")
        usaTitle = get_font(usa["size"]).render(usa["texto"], True, "white")
        usaTitle_rect = usaTitle.get_rect(center=(350, 520))
        cap = idiomas_manager.obtener_traduccion("idioma")
        capTitle = get_font(cap["size"]).render(cap["texto"], True, "white")
        capTitle_rect = capTitle.get_rect(center=(320, 220))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if btnMex.is_hover(mouse_x, mouse_y):
                    idiomas_manager.cambiar_idioma("español")
                    btnMex.change_image(
                        btnMexSelected
                    )  # Cambia la imagen del botón seleccionado
                    btnUSA.change_image(
                        pygame.image.load("img/btn/btnUSA.png").convert_alpha()
                    )  # Restaura la imagen del otro botón
                if btnUSA.is_hover(mouse_x, mouse_y):
                    idiomas_manager.cambiar_idioma("inglés")
                    btnUSA.change_image(
                        btnUSASelected
                    )  # Cambia la imagen del botón seleccionado
                    btnMex.change_image(
                        pygame.image.load("img/btn/btnMexico.png").convert_alpha()
                    )  # Restaura la imagen del otro botón
                if btnReturn.is_hover(mouse_x, mouse_y):
                    main_menu()

        if idiomas_manager.obtener_idioma() == "español":
            usaTitle = get_font(usa["size"]).render(usa["texto"], True, "#607C8B")
            btnMex.change_image(btnMexSelected)
            btnUSA.change_image(pygame.image.load("img/btn/btnUSA.png").convert_alpha())
        elif idiomas_manager.obtener_idioma() == "inglés":
            mxTitle = get_font(mx["size"]).render(mx["texto"], True, "#607C8B")
            btnUSA.change_image(btnUSASelected)
            btnMex.change_image(
                pygame.image.load("img/btn/btnMexico.png").convert_alpha()
            )

        buttons = [btnMex, btnUSA, btnReturn]

        mouse_x, mouse_y = pygame.mouse.get_pos()
        for button in buttons:
            if button.is_hover(mouse_x, mouse_y):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        btnReturn.draw(SCREEN)
        btnMex.draw(SCREEN)
        btnUSA.draw(SCREEN)
        SCREEN.blit(capTitle, capTitle_rect)
        SCREEN.blit(mxTitle, mxTitle_rect)
        SCREEN.blit(usaTitle, usaTitle_rect)

        pygame.display.update()
        SCREEN.fill("#FF5722")


# Para creadores
def creators():
    while True:
        title_text_info = idiomas_manager.obtener_traduccion("creadores")
        title = title_text_info["texto"]
        pygame.display.set_caption(f"{title} - Alimenta Tu Barriga")

        SCREEN.blit(creadoresfondo, [0, 0])

        title_text_info = idiomas_manager.obtener_traduccion("creadores")
        title = get_font(title_text_info["size"]).render(
            title_text_info["texto"], True, "white"
        )
        title_rect = title.get_rect(center=(354, 88))
        SCREEN.blit(title, title_rect)

        btnReturn = Button(
            65,
            48,
            pygame.image.load("./img/btn/btnReturn.png").convert_alpha(),
            pygame.image.load("./img/btn/btnReturnHover.png").convert_alpha(),
            0.16,
        )
        btnReturn.draw(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if btnReturn.is_hover(mouse_x, mouse_y):
                    main_menu()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if btnReturn.is_hover(mouse_x, mouse_y):
            btnReturn.change_image(btnReturn.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnReturn.change_image(btnReturn.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        btnReturn.draw(SCREEN)
        pygame.display.update()


def cv2ImageToSurface(cv2Image):
    size = cv2Image.shape[1::-1]
    format = "RGBA" if cv2Image.shape[2] == 4 else "RGB"
    cv2Image[:, :, [0, 2]] = cv2Image[:, :, [2, 0]]
    surface = pygame.image.frombuffer(cv2Image.flatten(), size, format)
    return surface.convert_alpha() if format == "RGBA" else surface.convert()


def loadGIF(filename):
    gif = cv2.VideoCapture(filename)
    frames = []
    while True:
        ret, cv2Image = gif.read()
        if not ret:
            break
        pygameImage = cv2ImageToSurface(cv2Image)
        frames.append(pygameImage)
    return frames


def intro():
    pygame.display.set_caption("Alimenta Tu Barriga")
    gifFrameList = loadGIF(r"video/cargando.mp4")
    currentFrame = 0
    while currentFrame < len(gifFrameList) - 1:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        SCREEN.blit(gifFrameList[currentFrame], (0, 0))
        currentFrame = (currentFrame + 1) % len(gifFrameList)
        pygame.display.flip()
        pygame.display.update()
    main_menu()


def main_menu():
    pygame.mixer.music.load("Audio/ES_Tiger Tracks - Lexica.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    font_path = "Fonts/PressStart2P.ttf"
    font_size = 36
    # Load the font using pygame.freetype
    font = pygame.freetype.Font(font_path, font_size)
    text_color = (255, 255, 255)  # White
    outline_color = (0, 0, 0)  # Black

    def render_text_with_outline(
        text, font, pos, text_color, outline_color, outline_width
    ):
        x, y = pos
        for dx in range(-outline_width, outline_width + 1):
            for dy in range(-outline_width, outline_width + 1):
                if abs(dx) + abs(dy) >= outline_width:
                    image, _ = font.render(text, outline_color)
                    SCREEN.blit(image, (x + dx, y + dy))
        image, _ = font.render(text, text_color)
        SCREEN.blit(image, pos)

    # Define your screen size
    screen_width = 600
    screen_height = 750

    SCREEN = pygame.display.set_mode((screen_width, screen_height))

    btnIniciar = Button(
        25,
        380,
        pygame.image.load("img/btn/btnIniciar.png").convert_alpha(),
        pygame.image.load("img/btn/btnIniciarHover.png").convert_alpha(),
        0.28,
    )
    btnConfig = Button(
        160,
        380,
        pygame.image.load("img/btn/btnConfig.png").convert_alpha(),
        pygame.image.load("img/btn/btnConfigHover.png").convert_alpha(),
        0.28,
    )
    btnCreador = Button(
        294,
        380,
        pygame.image.load("img/btn/btnCreador.png").convert_alpha(),
        pygame.image.load("img/btn/btnCreadorHover.png").convert_alpha(),
        0.28,
    )
    btnSalir = Button(
        430,
        380,
        pygame.image.load("./img/btn/btnExit.png").convert_alpha(),
        pygame.image.load("./img/btn/btnExitHover.png").convert_alpha(),
        0.28,
    )
    clock = pygame.time.Clock()
    FPS = 60

    # Load image
    bg = pygame.image.load("img/fondom.jpg").convert()
    bg_width = bg.get_width()

    scroll = 0
    width = screen_width
    tiles = math.ceil(width / bg_width) + 1

    # Game loop
    run = True
    while run:
        title_text_info = idiomas_manager.obtener_traduccion("menu")
        title = title_text_info["texto"]
        pygame.display.set_caption(f"{title} - Alimenta Tu Barriga")

        SCREEN.blit(bg, (0, 0))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        clock.tick(FPS)

        # Draw scrolling background
        for i in range(0, tiles):
            SCREEN.blit(bg, (i * bg_width + scroll, 0))

        # Scroll background
        scroll -= 5

        # Reset scroll
        if abs(scroll) > bg_width:
            scroll = 0

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if btnIniciar.is_hover(mouse_x, mouse_y):
                    play()  # Call your play() function
                if btnConfig.is_hover(mouse_x, mouse_y):
                    options()  # Call your options() function
                if btnCreador.is_hover(mouse_x, mouse_y):
                    creators()  # Call your creators() function
                if btnSalir.is_hover(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Botones
        btns = [btnIniciar, btnConfig, btnCreador, btnSalir]
        for btn in btns:
            if btn.is_hover(mouse_x, mouse_y):
                btn.change_image(btn.hover_image)
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                text_key = ""
                if btn is btnIniciar:
                    text_key = "iniciar"
                    outline_color = "#2E7D32"
                elif btn is btnConfig:
                    text_key = "configuracion"
                    outline_color = "#EF6C00"
                elif btn is btnCreador:
                    text_key = "creadores"
                    outline_color = "#00B0FF"
                elif btn is btnSalir:
                    text_key = "salir"
                    outline_color = "#B71C1C"

                title_text_info = idiomas_manager.obtener_traduccion(text_key)
                # Renderiza el texto usando la fuente
                texto_renderizado, _ = font.render(title_text_info["texto"], text_color)

                # Obtiene el rectángulo que rodea el texto
                text_rect = texto_renderizado.get_rect()

                # Obtiene el ancho del texto
                ancho_texto = text_rect.width

                # Obtiene el ancho de la pantalla
                ancho_pantalla = SCREEN.get_width()

                # Calcula la posición x para centrar el texto horizontalmente
                pos_x = ancho_pantalla / 2 - ancho_texto / 2

                render_text_with_outline(
                    title_text_info["texto"],
                    font,
                    (pos_x, 560),
                    text_color,
                    outline_color,
                    outline_width=5,
                )
            else:
                btn.change_image(btn.normal_image)

        if logo_img.draw(SCREEN):
            print("LOGO")

        btnIniciar.draw(SCREEN)
        btnConfig.draw(SCREEN)
        btnCreador.draw(SCREEN)
        btnSalir.draw(SCREEN)
        pygame.display.update()


if __name__ == "__main__":
    intro()
