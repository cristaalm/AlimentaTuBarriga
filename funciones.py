import fnmatch
import math,pygame,sys
import os
from pygame import font
from pruebaBTN import Button
import button3
from lenguajes import Lenguajes
import cv2

from pyvidplayer import Video

screen_width, screen_height = 600, 750
screen = pygame.display.set_mode((screen_width, screen_height))
font.init()
fuente = pygame.font.Font('./Fonts/font.ttf', 16)
fuentePuntaje = pygame.font.Font('./Fonts/font.ttf', 25)
btnReturn = Button(50, 40, pygame.image.load('./img/btn/btnReturn.png').convert_alpha(), pygame.image.load('./img/btn/btnReturnHover.png').convert_alpha(), 0.15)

def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 50:
        return True
    else:
        return False
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font('Fonts/font.ttf', size)
def mostrar_puntaje(x, y,puntaje):
    texto = fuente.render(f"{puntaje}", True, (0, 0, 0))
    screen.blit(texto, (x-12, y))
    
def puntajeComida(x, y,puntaje, time):
    current_time = pygame.time.get_ticks()
    diferencia=int((time-current_time)/20)
    y= y-(100-diferencia)
    if puntaje==0:
        texto = fuentePuntaje.render(f"{puntaje}", True, (255, 233, 0))
    elif puntaje>0:
        texto = fuentePuntaje.render(f"+{puntaje}", True, (0, 255, 0))
    else:
        texto = fuentePuntaje.render(f"{puntaje}", True, (255, 0, 0))
    texto.set_alpha(254-(150-diferencia))
    screen.blit(texto, (x, y))
sonido_colision=True

def draw_game_over_screen(event, idioma,nombre): 
    idiomas_manager = Lenguajes()
    idiomas_manager.cambiar_idioma(idioma)
    # img/screen/fin_español.png
    bgGO = pygame.image.load(f"img/screen/fin_{idioma}.png").convert() 
    bgGO = pygame.transform.scale(bgGO, (600, 750))
    if idioma=="español":
        btnRestart = Button(70, 470, pygame.image.load('./img/btn/btnRestart.png').convert_alpha(), pygame.image.load('./img/btn/btnRestartHover.png').convert_alpha(), 0.3) 
        btnHome = Button(225, 470, pygame.image.load('./img/btn/btnPrincipal.png').convert_alpha(), pygame.image.load('./img/btn/btnPrincipalHover.png').convert_alpha(), 0.3) 
        btnExit = Button(380, 470, pygame.image.load('./img/btn/btnExit.png').convert_alpha(), pygame.image.load('./img/btn/btnExitHover.png').convert_alpha(), 0.3)
        nombre = get_font(30).render(nombre, True, "white")
        nombre_rect = nombre.get_rect(center=(screen_width//2, 418))
    else:
        btnRestart = Button(70, 505, pygame.image.load('./img/btn/btnRestart.png').convert_alpha(), pygame.image.load('./img/btn/btnRestartHover.png').convert_alpha(), 0.3) 
        btnHome = Button(225, 505, pygame.image.load('./img/btn/btnPrincipal.png').convert_alpha(), pygame.image.load('./img/btn/btnPrincipalHover.png').convert_alpha(), 0.3) 
        btnExit = Button(380, 505, pygame.image.load('./img/btn/btnExit.png').convert_alpha(), pygame.image.load('./img/btn/btnExitHover.png').convert_alpha(), 0.3)
        nombre = get_font(30).render(nombre, True, "white")
        nombre_rect = nombre.get_rect(center=(screen_width//2, 470))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit() 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            if btnRestart.is_hover(mouse_x, mouse_y): 
                return "REINICIAR" 
            if btnExit.is_hover(mouse_x, mouse_y): 
                return "SALIR" 
            if btnHome.is_hover(mouse_x, mouse_y): 
                return "PRINCIPAL" 
                             
    mouse_x, mouse_y = pygame.mouse.get_pos() 
    if btnRestart.is_hover(mouse_x, mouse_y): 
        btnRestart.change_image(btnRestart.hover_image) 
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) 
    else: 
        btnRestart.change_image(btnRestart.normal_image) 
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 
         
    if btnExit.is_hover(mouse_x, mouse_y): 
        btnExit.change_image(btnExit.hover_image) 
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) 
    else: 
        btnExit.change_image(btnExit.normal_image) 
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 
    if btnHome.is_hover(mouse_x, mouse_y): 
        btnHome.change_image(btnHome.hover_image) 
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) 
    else: 
        btnHome.change_image(btnHome.normal_image) 
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)     
    screen.blit(bgGO, (0, 0)) 
    screen.blit(nombre, nombre_rect)
    btnRestart.draw(screen) 
    btnExit.draw(screen) 
    btnHome.draw(screen) 
    pygame.display.update()
    
def draw_pause_screen(event):
    bgPause = pygame.image.load("img/bgPause.png").convert()
    
    # Botones cuanado gane
    btnContinue = Button(70, 485, pygame.image.load('./img/btn/btnSkip.png').convert_alpha(), pygame.image.load('./img/btn/btnSkipHover.png').convert_alpha(), 0.3)
    btnRestart = Button(225, 485, pygame.image.load('./img/btn/btnRestart.png').convert_alpha(), pygame.image.load('./img/btn/btnRestartHover.png').convert_alpha(), 0.3)
    btnHome = Button(380, 485, pygame.image.load('./img/btn/btnPrincipal.png').convert_alpha(), pygame.image.load('./img/btn/btnPrincipalHover.png').convert_alpha(), 0.3)
    # btnExit = Button(440, 485, pygame.image.load('./img/btn/btnExit.png').convert_alpha(), pygame.image.load('./img/btn/btnExitHover.png').convert_alpha(), 0.2)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if btnRestart.is_hover(mouse_x, mouse_y):
                return "REINICIAR"
            if btnContinue.is_hover(mouse_x, mouse_y):
                return "CONTINUAR"
            # if btnExit.is_hover(mouse_x, mouse_y):
            #     return "SALIR"
            if btnHome.is_hover(mouse_x, mouse_y):
                return "PRINCIPAL"
                            
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if btnRestart.is_hover(mouse_x, mouse_y):
        btnRestart.change_image(btnRestart.hover_image)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        btnRestart.change_image(btnRestart.normal_image)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
    if btnContinue.is_hover(mouse_x, mouse_y):
        btnContinue.change_image(btnContinue.hover_image)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        btnContinue.change_image(btnContinue.normal_image)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    # if btnExit.is_hover(mouse_x, mouse_y):
    #     btnExit.change_image(btnExit.hover_image)
    #     pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    # else:
    #     btnExit.change_image(btnExit.normal_image)
    #     pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
    if btnHome.is_hover(mouse_x, mouse_y):
        btnHome.change_image(btnHome.hover_image)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        btnHome.change_image(btnHome.normal_image)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    
    screen.blit(bgPause, (0, 0))
    btnRestart.draw(screen)
    btnContinue.draw(screen)
    # btnExit.draw(screen)
    btnHome.draw(screen)
    pygame.display.update()

# Pantalla de cuando gana
def obtener_winner(genero,piel):
    personaje = pygame.image.load(f"./img/{genero}/{genero}_{piel}_winner.png").convert_alpha()
    personaje = pygame.transform.scale(personaje, (150, 150))
    return personaje
def obtener_loser(genero,piel):
    personaje = pygame.image.load(f"./img/{genero}/{genero}_{piel}_loser.png").convert_alpha()
    personaje = pygame.transform.scale(personaje, (150, 150))
    return personaje       
sonido_colision_W=True
def draw_winner_screen(puntaje,genero,piel,event,idioma,level,audio,nombre):
    idiomas_manager = Lenguajes()
    idiomas_manager.cambiar_idioma(idioma)
    backgroundDay = pygame.image.load("./img/diaarranque.jpg").convert()
    backgroundDay = pygame.transform.scale(backgroundDay, (600, 750))
    winner90 = pygame.image.load(f"./img/screen/{idioma}_90.png").convert_alpha()
    winner90 = pygame.transform.scale(winner90, (600, 750))
    winner80 = pygame.image.load(f"./img/screen/{idioma}_80.png").convert_alpha()
    winner80 = pygame.transform.scale(winner80, (600, 750))
    winner70 = pygame.image.load(f"./img/screen/{idioma}_70.png").convert_alpha()
    winner70 = pygame.transform.scale(winner70, (600, 750))
    winner50 = pygame.image.load(f"./img/screen/{idioma}_50.png").convert_alpha()
    winner50 = pygame.transform.scale(winner50, (600, 750))
    loser = pygame.image.load(f"img/screen/tiempo_{idioma}.png").convert_alpha()
    loser = pygame.transform.scale(loser, (600, 750))

    # Botones cuanado gane
    btnContinue = Button(70, 477, pygame.image.load('./img/btn/btnSkip.png').convert_alpha(), pygame.image.load('./img/btn/btnSkipHover.png').convert_alpha(), 0.23)
    btnRestart = Button(190, 477, pygame.image.load('./img/btn/btnRestart.png').convert_alpha(), pygame.image.load('./img/btn/btnRestartHover.png').convert_alpha(), 0.23)
    btnHome = Button(310, 477, pygame.image.load('./img/btn/btnPrincipal.png').convert_alpha(), pygame.image.load('./img/btn/btnPrincipalHover.png').convert_alpha(), 0.23)
    btnExit = Button(430, 477, pygame.image.load('./img/btn/btnExit.png').convert_alpha(), pygame.image.load('./img/btn/btnExitHover.png').convert_alpha(), 0.23)
    # Botones cuanado pierde
    btnRestart1 = Button(70, 480, pygame.image.load('./img/btn/btnRestart.png').convert_alpha(), pygame.image.load('./img/btn/btnRestartHover.png').convert_alpha(), 0.25)
    btnHome1 = Button(225, 480, pygame.image.load('./img/btn/btnPrincipal.png').convert_alpha(), pygame.image.load('./img/btn/btnPrincipalHover.png').convert_alpha(), 0.25)
    btnExit1 = Button(380, 480, pygame.image.load('./img/btn/btnExit.png').convert_alpha(), pygame.image.load('./img/btn/btnExitHover.png').convert_alpha(), 0.25)
    fontpuntaje = pygame.font.Font("./Fonts/font.ttf", 25)
    title_text_info = idiomas_manager.obtener_traduccion("pF")
    title_Puntaje = title_text_info["texto"]
    texto_puntaje=fontpuntaje.render(f"{title_Puntaje}{puntaje}", True, "green")
    # texto_puntaje1=fontpuntaje.render(f"{title_Puntaje}{puntaje}", True, "red") 
    # Define que en caso de cierto puntaje se muestre diferente pantalla
    screen.blit(backgroundDay,[0,0])
    if puntaje<=50:
        screen.blit(loser,[0,0])
    elif (puntaje<70):
        screen.blit(winner50,[0,0])
    elif (puntaje<80):
        screen.blit(winner70,[0,0])
    elif (puntaje<90):
        screen.blit(winner80,[0,0])
    elif (puntaje<=100):
        screen.blit(winner90,[0,0])
    
    if puntaje<=50:
        #NOMBRE#
        nombre = get_font(30).render(nombre, True, "white")
        nombre_rect = nombre.get_rect(center=(420, 280))
        screen.blit(nombre, nombre_rect)
        if audio:
            sonido_colision = pygame.mixer.Sound(
                                "./Audio/lose.mp3"
                            )
            sonido_colision.play()
        screen.blit(obtener_loser(genero,piel),(220,600))
        # screen.blit(texto_puntaje1,[94, 415])
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if btnRestart1.is_hover(mouse_x, mouse_y):
                        return "REINICIAR"
                if btnExit1.is_hover(mouse_x, mouse_y):
                        return "SALIR"
                if btnHome1.is_hover(mouse_x, mouse_y):
                        return "PRINCIPAL"
                        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if btnRestart1.is_hover(mouse_x, mouse_y):
            btnRestart1.change_image(btnRestart1.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnRestart1.change_image(btnRestart1.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            
        if btnExit1.is_hover(mouse_x, mouse_y):
            btnExit1.change_image(btnExit1.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnExit1.change_image(btnExit1.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            
        if btnHome1.is_hover(mouse_x, mouse_y):
            btnHome1.change_image(btnHome1.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnHome1.change_image(btnHome1.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        btnRestart1.draw(screen)
        btnExit1.draw(screen)
        btnHome1.draw(screen)
    elif puntaje>=55:
        if audio:
            sonido_colision = pygame.mixer.Sound(
                                "./Audio/winner.mp3"
                            )
            sonido_colision.play()
        screen.blit(obtener_winner(genero,piel),(220,600))
        screen.blit(texto_puntaje,[102, 165])
        
        if level==1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if btnRestart.is_hover(mouse_x, mouse_y):
                            return "REINICIAR"
                    if btnContinue.is_hover(mouse_x, mouse_y):
                            return "LEVEL2"
                    if btnExit.is_hover(mouse_x, mouse_y):
                            return "SALIR"
                    if btnHome.is_hover(mouse_x, mouse_y):
                            return "PRINCIPAL"
        if level==2:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if btnRestart.is_hover(mouse_x, mouse_y):
                            return "REINICIAR"
                    if btnContinue.is_hover(mouse_x, mouse_y):
                            return "LEVEL3"
                    if btnExit.is_hover(mouse_x, mouse_y):
                            return "SALIR"
                    if btnHome.is_hover(mouse_x, mouse_y):
                            return "PRINCIPAL"
        if level==3:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if btnRestart.is_hover(mouse_x, mouse_y):
                            return "REINICIAR"
                    if btnContinue.is_hover(mouse_x, mouse_y):
                            return "ENDGAME"
                    if btnExit.is_hover(mouse_x, mouse_y):
                            return "SALIR"
                    if btnHome.is_hover(mouse_x, mouse_y):
                            return "PRINCIPAL"
                        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if btnRestart.is_hover(mouse_x, mouse_y):
            btnRestart.change_image(btnRestart.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnRestart.change_image(btnRestart.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            
        if btnContinue.is_hover(mouse_x, mouse_y):
            btnContinue.change_image(btnContinue.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnContinue.change_image(btnContinue.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if btnExit.is_hover(mouse_x, mouse_y):
            btnExit.change_image(btnExit.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnExit.change_image(btnExit.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            
        if btnHome.is_hover(mouse_x, mouse_y):
            btnHome.change_image(btnHome.hover_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            btnHome.change_image(btnHome.normal_image)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
        btnRestart.draw(screen)
        btnContinue.draw(screen)
        btnExit.draw(screen)
        btnHome.draw(screen)
    pygame.display.update()
    
nivel2bg = pygame.image.load("./img/bgNivel2.png").convert_alpha()
nivel2bg = pygame.transform.scale(nivel2bg, (600, 750))

def nivel2():
    pygame.display.set_caption('Nivel 2 - Alimenta Tu Barriga')
    
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(nivel2bg, [0, 0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        
def draw_winner70_screen(puntaje):
    winner90 = pygame.image.load("./img/felicidades90.png").convert()
    screen.fill("black")
    screen.blit(winner90,[0,0])
    # screen.blit(winner,(200,100))
    fontpuntaje = pygame.font.Font("./Fonts/font.ttf", 60)
    font = pygame.font.Font("./Fonts/font.ttf", 60)
    texto_puntaje=fontpuntaje.render(f"Puntaje: {puntaje}", True, "green")
    title = font.render('WINNER', True, (255, 255, 255))
    quit_button = font.render('Q - Quit', True, (255, 255, 255))
    start_button = font.render('S - Restart', True, (255, 255, 255))
    screen.blit(texto_puntaje, (300, 111))
    
    screen.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/2 + start_button.get_height()/2+100))
    screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2*3+100))
    pygame.display.update()

def draw_winner80_screen(puntaje):
    backgroundDay = pygame.image.load("./img/diaarranque.jpg").convert()
    backgroundDay = pygame.transform.scale(backgroundDay, (600, 750))
    winner90 = pygame.image.load("./img/felicidades90.png").convert()
    winner = pygame.image.load("./img/Winner.png").convert_alpha()
    winner = pygame.transform.scale(winner, (200, 200))
    # saltando = pygame.transform.scale(saltando, (200, 200))
    screen.fill("black")
    screen.blit(winner90,[0,0])
    # screen.blit(winner,(200,100))
    fontpuntaje = pygame.font.Font("./Fonts/font.ttf", 60)
    font = pygame.font.Font("./Fonts/font.ttf", 60)
    texto_puntaje=fontpuntaje.render(f"Puntaje: {puntaje}", True, "green")
    title = font.render('WINNER', True, (255, 255, 255))
    quit_button = font.render('Q - Quit', True, (255, 255, 255))
    start_button = font.render('S - Restart', True, (255, 255, 255))
    screen.blit(texto_puntaje, (screen_width/2 - title.get_width()/2-100, screen_height/2 - title.get_height()/2*2))
    screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/2+100))
    
    screen.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/2 + start_button.get_height()/2+100))
    screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2*3+100))
    pygame.display.update()
    
def info(event,genero,piel,idioma,level_number):
    instrucciones_path = f"img/instrucciones/{level_number}/{genero}_{piel}_{idioma}.png"
    instruccionesHB = pygame.image.load(instrucciones_path).convert()
    instruccionesHB = pygame.transform.scale(instruccionesHB, (600, 750))
    screen.blit(instruccionesHB,[0,0])
    
    if hasattr(event, 'type'):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if btnReturn.is_hover(mouse_x, mouse_y):
                return "game"
    
    btnReturn.draw(screen)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if btnReturn.is_hover(mouse_x, mouse_y):
        btnReturn.change_image(btnReturn.hover_image)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        btnReturn.change_image(btnReturn.normal_image)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    return btnReturn

        
pygame.display.update()

def cv2ImageToSurface(cv2Image):
    size = cv2Image.shape[1::-1]
    format = 'RGBA' if cv2Image.shape[2] == 4 else 'RGB'
    cv2Image[:, :, [0, 2]] = cv2Image[:, :, [2, 0]]
    surface = pygame.image.frombuffer(cv2Image.flatten(), size, format)
    return surface.convert_alpha() if format == 'RGBA' else surface.convert()

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
def endgame(genero,piel):
    pygame.display.set_caption("Alimenta Tu Barriga")
    gifFrameList = loadGIF(f"video/{genero}_{piel}.mp4")
    currentFrame = 0
    clock = pygame.time.Clock()
    while currentFrame<len(gifFrameList)-1:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(gifFrameList[currentFrame], (0,0))
        currentFrame = (currentFrame + 1) % len(gifFrameList)
        pygame.display.flip()
        pygame.display.update()
    from menuPrincipal import main_menu
    main_menu()
def endgame2(genero,piel,idioma):
    pygame.display.set_caption("Alimenta Tu Barriga")
    clock = pygame.time.Clock()
    vid = Video(f"video/{genero}_{piel}_{idioma}.mp4")
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vid.close()
                pygame.quit()
                exit()
        clock.tick(60)
        run=vid.draw(screen, (0, 0))
        pygame.display.update()
    vid.close()
    currentFrame = 0
    gifFrameList = loadGIF(f"video/mujer_moreno.mp4")
    # while currentFrame<len(gifFrameList)-1:
    #     clock.tick(30)
    #     screen.blit(gifFrameList[currentFrame], (0,0))
    #     currentFrame = (currentFrame + 1) % len(gifFrameList)
    #     pygame.display.flip()
    #     pygame.display.update()
    from menuPrincipal import main_menu
    main_menu()
    
def historia(nombre, genero, piel,idioma,level,puntuacion):
    idiomas_manager = Lenguajes()
    idiomas_manager.cambiar_idioma(idioma)
    title_text_info = idiomas_manager.obtener_traduccion("historia")
    title = title_text_info["texto"]
    pygame.display.set_caption(f"{title} - Alimenta Tu Barriga")
    font = pygame.font.Font("Fonts/PressStart2P.ttf", 20)
    idioma = idiomas_manager.obtener_idioma()
    BLANCO = (255, 255, 255)
    folder= f"img/{idioma}/{level}/{genero}/{piel}/"
    imagenes = len(fnmatch.filter(os.listdir(folder), '*.*'))
    image_list = []
    for i in range(1, imagenes):
        # image_list.append(pygame.image.load(f"img/{idioma}/{genero}/{piel}/{i}.png"))
        image_list.append(
            pygame.image.load(
                f"img/{idioma}/{level}/{genero}/{piel}/{i}.png"
            )
        )

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
    prev_button_y = screen_height - button_height - button_margin

    next_button_x = screen_width - 70 - button_width - button_margin
    next_button_y = screen_height - button_height - button_margin

    # Agregar botón central entre los dos botones inferiores
    center_button_image = pygame.transform.scale(
        pygame.image.load("img/btn/btnPrincipal.png"), (button_width, button_height)
    )
    center_button_hover_image = pygame.transform.scale(
        pygame.image.load("img/btn/btnPrincipalHover.png"),
        (button_width, button_height),
    )
    center_button_x = (screen_width - button_width) // 2
    center_button_y = next_button_y  # Mismo nivel que los botones inferiores

    # Agregar imagen superior en medio
    top_image = pygame.transform.scale(
        pygame.image.load(f"img/textoEnter_{idioma}.png"), (screen_width-100, 80)
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
                        if current_image_index == len(image_list) - 1:
                            instrucciones(nombre, genero, piel,idioma,level,puntuacion)
                    # Verificar si se hizo clic en el botón "Centro"
                    elif (
                        center_button_x
                        <= pygame.mouse.get_pos()[0]
                        <= center_button_x + button_width
                        and center_button_y
                        <= pygame.mouse.get_pos()[1]
                        <= center_button_y + button_height
                    ):
                        from menuPrincipal import main_menu
                        main_menu()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_image_index = max(current_image_index - 1, 0)
                elif event.key == pygame.K_RIGHT:
                    current_image_index = min(
                        current_image_index + 1, len(image_list) - 1
                    )
                    if current_image_index == len(image_list) - 1:
                        instrucciones(nombre, genero, piel,idioma,level,puntuacion)
                elif event.key == pygame.K_ESCAPE:
                    # Aquí deberías agregar el código para ir a la siguiente pantalla
                    print("Ir a la Siguiente Pantalla")
                    instrucciones(nombre, genero, piel,idioma,level,puntuacion)
        screen.fill(BLANCO)
        current_image = image_list[current_image_index]
        image_rect = current_image.get_rect()
        image_rect.center = (screen_width // 2, screen_height // 2)
        screen.blit(current_image, image_rect)

        # Verificar si el ratón está sobre los botones y mostrar la imagen correspondiente
        if (
            prev_button_x <= pygame.mouse.get_pos()[0] <= prev_button_x + button_width
            and prev_button_y
            <= pygame.mouse.get_pos()[1]
            <= prev_button_y + button_height
        ):
            screen.blit(prev_button_hover_image, (prev_button_x, prev_button_y))
        else:
            screen.blit(prev_button_image, (prev_button_x, prev_button_y))

        if (
            next_button_x <= pygame.mouse.get_pos()[0] <= next_button_x + button_width
            and next_button_y
            <= pygame.mouse.get_pos()[1]
            <= next_button_y + button_height
        ):
            screen.blit(next_button_hover_image, (next_button_x, next_button_y))
        else:
            screen.blit(next_button_image, (next_button_x, next_button_y))

        # Renderizar botón "Centro" en la pantalla
        if (
            center_button_x
            <= pygame.mouse.get_pos()[0]
            <= center_button_x + button_width
            and center_button_y
            <= pygame.mouse.get_pos()[1]
            <= center_button_y + button_height
        ):
            screen.blit(center_button_hover_image, (center_button_x, center_button_y))
        else:
            screen.blit(center_button_image, (center_button_x, center_button_y))

        # Renderizar imagen superior en medio
        screen.blit(top_image, top_image_rect)
        pygame.display.update()
    instrucciones(nombre, genero, piel,idioma,level,puntuacion)
    
def instrucciones(nombre, genero, piel,idioma,level,puntuacion):
    idiomas_manager = Lenguajes()
    idiomas_manager.cambiar_idioma(idioma)
    title_text_info = idiomas_manager.obtener_traduccion("instrucciones")
    title = title_text_info["texto"]
    pygame.display.set_caption(f"{title} - Alimenta Tu Barriga")

    idioma_actual = idiomas_manager.obtener_idioma()
    top_image = pygame.transform.scale(
        pygame.image.load(f"img/textoEnterN_{idioma_actual}.png"), (screen_width - 230, 60)
    )
    top_image_rect = top_image.get_rect()
    if (level==2):
        instrucciones_path = f"img/instrucciones/{idioma_actual}.png"
    else:
        instrucciones_path = f"img/instrucciones/{level}/{genero}_{piel}_{idioma_actual}.png"
    instruccionesHB = pygame.image.load(instrucciones_path).convert()
    instruccionesHB = pygame.transform.scale(instruccionesHB, (600, 750))
    if idioma_actual == "español":
        if level==2:
            top_image_rect.center = (screen_width // 2, 11)
        top_image_rect.center = (screen_width // 2, 38)
    else:
        top_image_rect.center = (screen_width // 2, 45)
    tiempo_fin = pygame.time.get_ticks() + 10000
    success = True
    while pygame.time.get_ticks() < tiempo_fin and success:
        screen.blit(instruccionesHB, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    success = False
        screen.blit(top_image, top_image_rect)
        pygame.display.update()
    level1(nombre, genero, piel, level, puntuacion, idioma)
    
def level1(nombre_personaje, genero, piel, level_number, puntajeAnt, idioma):
    idiomas_manager = Lenguajes()
    idiomas_manager.cambiar_idioma(idioma)
    from level1HB2 import level1HB
    title_text_info = idiomas_manager.obtener_traduccion("nivel")
    title = title_text_info["texto"]
    pygame.display.set_caption(f"{title} {level_number} - Alimenta Tu Barriga")
    level = level1HB()
    level.Run(
        genero, "delgado", piel, nombre_personaje, level_number, puntajeAnt, idioma
    )

def pociones(event,idioma):
    idiomas_manager = Lenguajes()
    idiomas_manager.cambiar_idioma(idioma)
    # img/instrucciones/español.png
    instruccionesHB = pygame.image.load(f"img/instrucciones/{idioma}.png").convert()
    instruccionesHB = pygame.transform.scale(instruccionesHB, (600, 750))
    screen.blit(instruccionesHB,[0,0])
    if hasattr(event, 'type'):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if btnReturn.is_hover(mouse_x, mouse_y):
                return "game"
    btnReturn.draw(screen)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if btnReturn.is_hover(mouse_x, mouse_y):
        btnReturn.change_image(btnReturn.hover_image)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        btnReturn.change_image(btnReturn.normal_image)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    return btnReturn
pygame.display.update()