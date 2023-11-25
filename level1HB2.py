import sys
import pygame, random, os, time
import button
import comidaModel
from pruebaBTN import Button
from player2 import Player
import friend
from btnPoderes import Poderes
from HealthBar import HealthBar
from lenguajes import Lenguajes
from funciones import (
    hay_colision,
    draw_game_over_screen,
    draw_pause_screen,
    mostrar_puntaje,
    puntajeComida,
    draw_winner_screen,
    info,
    draw_winner80_screen,
    draw_winner70_screen,
    pociones,
    endgame,
    endgame2,
    historia
)

class level1HB:
    def __init__(self):
        self.width, self.height = 600, 750

        # Coordenadas del mono
        self.coord_x = 215
        self.coord_y = 650
        # Velocidad
        self.x_speed = 0
        self.y_speed = 0
        self.sentido = 1
        self.audio_winner=False
        self.health_bar = HealthBar(65, 40, 350, 30, 100, 1)
        # barra= pygame.draw.rect(screen,'white',)
        self.tipo_comida = 0
        self.is_slow = False
        self.is_fast = False
        self.is_inmune = False
        self.texto_puntaje = []
        self.puntaje = 50
        self.texto_x = 65
        self.texto_y = 65
        self.done = False
        self.foods_and_junk = []
        self.game_state = "startgame"
        # Personajes
        self.nombre = ""
        self.level_number = 1
        self.idioma = ""
        self.idiomas_manager = Lenguajes()  # Nos permite controlar los frame
        self.clock = pygame.time.Clock()
        # Ingresamos fondo
        self.backgroundDay = pygame.image.load("./img/dia.png").convert()

    def cargar_musica(self, level_number):
        pygame.mixer.init()
        if level_number == 1:
            pygame.mixer.music.load("Audio/ES_Fair N Square - William Benckert.mp3")
        elif level_number == 2:
            pygame.mixer.music.load("Audio/musicalvl2.mp3")
        elif level_number == 3:
            pygame.mixer.music.load("Audio/musicalvl3.mp3")
        # Añade más casos según sea necesario para otros niveles

        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        self.is_mute = False

    def mute(self):
        pygame.mixer.music.pause()
        self.is_mute = True

    def unmute(self):
        pygame.mixer.music.unpause()
        self.is_mute = False

    pygame.time.set_timer(pygame.USEREVENT, 5000)

    def Run(
        self, genero, complexion, color, nombre, level_number, puntajeAnt, idioma_actual
    ):
        self.idioma = idioma_actual

        self.idiomas_manager.cambiar_idioma(self.idioma)
        pygame.init()
        self.level_number = level_number
        self.nombre = nombre
        event = None
        slowt = 0
        inmuneT = 0
        waiting_time=0
        waiting=False
        fastT = 0
        self.font = pygame.font.SysFont(None, 50)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.health_bar = HealthBar(65, 36.6, 350, 30, 100, self.level_number)

        # Cargar la música según el nivel
        self.cargar_musica(self.level_number)

        if self.level_number == 1:
            self.backgroundDay = pygame.image.load("./img/dia.png").convert()
        elif self.level_number == 2:
            print(f"puntaje pasado: {puntajeAnt}")
            self.backgroundDay = pygame.image.load("./img/tarde.png").convert()
            # Acá pongan todo lo restante del nivel 2
            self.poderes = Poderes(puntajeAnt)
        else:
            self.backgroundDay = pygame.image.load("./img/noche.png").convert()
            self.poderes = Poderes(puntajeAnt)
            # Acá pongan todo lo restante del nivel 3
            # Puedes crear una clase específica para manejar el nivel 3 si es necesario
            # self.nivel_tres = NivelTres()
        if self.level_number==2 or self.level_number==3:
            btn1 = pygame.image.load("img/btn/1.png").convert_alpha()
            btn1 = pygame.transform.scale(btn1, (60, 60))
            btn1 = button.Button(10, 268, btn1, 0.7)
            btn2 = pygame.image.load("img/btn/2.png").convert_alpha()
            btn2 = pygame.transform.scale(btn2, (60, 60))
            btn2 = button.Button(10, 364, btn2, 0.7)
            btn3 = pygame.image.load("img/btn/3.png").convert_alpha()
            btn3 = pygame.transform.scale(btn3, (60, 60))
            btn3 = button.Button(10, 470, btn3, 0.7)

        player1 = friend.Friend((80, 195), "amigo1", 4, True)
        player2 = friend.Friend((510, 195), "amigo2", 4, False)
        if self.level_number == 3:
            ardilla = friend.Friend((-500, 650), "amigo1", 8, False, True)
        btnPociones = Button(
        425,
        20,
        pygame.image.load("./img/btn/btnPotion.png").convert_alpha(),
        pygame.image.load("./img/btn/btnPotionHover.png").convert_alpha(),
        0.14,
        )

        btnInfo = Button(
            500,
            20,
            pygame.image.load("./img/btn/btnQuestion.png").convert_alpha(),
            pygame.image.load("./img/btn/btnQuestionHover.png").convert_alpha(),
            0.14,
        )
        btnMute = Button(
            5,
            695,
            pygame.image.load("./img/btn/btnMute.png").convert_alpha(),
            pygame.image.load("./img/btn/btnUnmute.png").convert_alpha(),
            0.09,
        )
        btnFlechas = pygame.image.load("img/btn/keyDown.png").convert_alpha()
        btnFlechas = pygame.transform.scale(btnFlechas, (40, 40))
        btnFlechas = button.Button(43, 712, btnFlechas, 0.8)
        
        player = Player(
            (self.coord_x, self.coord_y), genero, complexion, color, self.level_number
        )
        while not self.done:
            current_time = pygame.time.get_ticks()
            # Se usa el método "blit" para imprimir la imagen
            self.screen.blit(self.backgroundDay, [0, 0])

            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    # sys.exit()
                    self.done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if btnInfo.is_hover(mouse_x, mouse_y):
                        self.game_state = "info"
                        self.health_bar.pause()
                    if level_number==2 or level_number==3:
                        if btnPociones.is_hover(mouse_x, mouse_y):
                            self.game_state="pociones"
                    if btnMute.is_hover(mouse_x, mouse_y):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        if self.is_mute:
                            self.unmute()
                        else:
                            self.mute()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.game_state != "game over":
                            self.game_state = "pause"
                            self.health_bar.pause()
                    if event.key == pygame.K_DOWN:
                        if self.is_mute:
                            self.unmute()
                        else:
                            self.mute()
            if self.game_state == "endgame":
                player1.update()
                player2.update()
                middle=self.width/2
                player_position=player.rect.x
                direction=1
                
                if (middle-player_position>0):
                    direction=1
                else:
                    direction=-1
                diferencia=abs(middle-player_position)
                run_direction=""
                if (direction==1):
                    diferencia -=50
                    run_direction="right"
                else:
                    diferencia +=50
                    run_direction="left"
                while diferencia>0:
                    player.rect.x += 2*direction
                    player.updateEndgame(run_direction)
                    diferencia -=2
                    self.screen.blit(self.backgroundDay, [0, 0])
                    self.screen.blit(player.image, player.rect)
                    player1.update()
                    player2.update()
                    pygame.display.flip()
                    self.clock.tick(30)
                    pygame.display.update()
                if waiting==False:
                    waiting=True
                    waiting_time= current_time+1000
                
                player.updateEndgame("stand_none")
                self.screen.blit(player.image, player.rect)
                pygame.display.update()
                if current_time>waiting_time and player1.posicionInicial and player2.posicionInicial:
                    self.mute()
                    endgame2(genero,color,self.idioma)
            if self.game_state == "info":
                respuesta = info(event, genero, color,self.idioma,level_number)
                if respuesta == "game":
                    self.game_state = respuesta
                    self.health_bar.restore()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    self.game_state = "game"
            if self.game_state == "pociones":
                respuesta = pociones(event, self.idioma)
                if respuesta == "game":
                    self.game_state = respuesta
                    self.health_bar.restore()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    self.game_state = "game"
            if self.game_state == "game over":
                respuesta = draw_game_over_screen(event,self.idioma,self.nombre)
                if respuesta == "SALIR":
                    pygame.quit()
                    sys.exit()
                    
                if respuesta == "REINICIAR":
                    self.game_state = "startgame"
                if respuesta == "PRINCIPAL":
                    from menuPrincipal import main_menu
                    main_menu()
                    # pygame.quit()
                    # os.system("python menuPrincipal.py")
                    # quit()    
                keys = pygame.key.get_pressed()
                if keys[pygame.K_s]:
                    self.game_state = "startgame"
                if keys[pygame.K_q]:
                    pygame.quit()
                    sys.exit()
                    quit()
            if self.game_state == "winner":
               
                respuesta = draw_winner_screen( 
                    self.puntaje, genero, color, event, self.idioma, level_number,self.audio_winner,self.nombre 
                )
                self.audio_winner=False
                if respuesta == "LEVEL2":
                    historia(nombre,genero,color,self.idioma,2,self.puntaje)
                    # level = level1HB()
                    # level.Run(
                    #     genero, complexion, color, nombre, 2, self.puntaje, self.idioma
                    # )
                if respuesta == "LEVEL3":
                    historia(nombre,genero,color,self.idioma,3,self.puntaje)
                    # level = level1HB()
                    # level.Run(
                    #     genero, complexion, color, nombre, 3, self.puntaje, self.idioma
                    # )
                if respuesta == "ENDGAME":
                    endgame(genero,color)
                if respuesta == "SALIR":
                    pygame.quit()
                    sys.exit()
                    quit()
                if respuesta == "REINICIAR":
                    self.game_state = "startgame"
                if respuesta == "PRINCIPAL":
                    from menuPrincipal import main_menu
                    main_menu()
                    # pygame.quit()
                    # os.system("python menuPrincipal.py")
                    # quit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_s]:
                    self.game_state = "startgame"
                if keys[pygame.K_q]:
                    pygame.quit()
                    sys.exit()
                    quit()
            if self.game_state == "pause":
                respuesta = draw_pause_screen(event)
                if respuesta == "SALIR":
                    pygame.quit()
                    sys.exit()
                    quit()
                if respuesta == "CONTINUAR":
                    self.game_state = "game"
                    self.health_bar.restore()
                if respuesta == "REINICIAR":
                    self.game_state = "startgame"
                if respuesta == "PRINCIPAL":
                    from menuPrincipal import main_menu
                    main_menu()
                    # pygame.quit()
                    # os.system("python menuPrincipal.py")
                    # quit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_s]:
                    self.game_state = "startgame"
                if keys[pygame.K_q]:
                    pygame.quit()
                    sys.exit()
                    quit()
            if self.game_state == "startgame":
                player1.rect.x = 80
                player2.rect.x = 510
                self.coord_x = 215
                self.coord_y = 650
                self.sentido = 1
                self.tipo_comida = 0
                # Este es el bueno a modificar, pruebas
                self.puntaje = 50
                self.is_slow = False
                self.is_fast = False
                self.is_inmune = False
                self.health_bar.reset()
                self.texto_puntaje.clear()
                self.foods_and_junk.clear()
                self.unmute()
                player.reiniciar(
                    (self.coord_x, self.coord_y), genero, complexion, color
                )
                self.game_state = "game"
                if self.level_number == 3: 
                    ardilla = friend.Friend((-500, 650), "amigo1", 8, False, True)
                self.poderes = Poderes(puntajeAnt)
            if self.game_state == "game":
                player1.update()
                player2.update()
                if self.level_number == 2:
                    self.poderes.run(self.screen, self.puntaje)
                    # PODERES
                    if self.poderes.es_inmune:
                        self.is_inmune = True
                        inmuneT = current_time + 5000
                        self.poderes.es_inmune = False
                    if self.poderes.tiene_alcanzame:
                        self.is_fast = True
                        fastT = current_time + 5000
                        self.poderes.tiene_alcanzame = False
                    if self.poderes.tiene_volveralavida:
                        self.puntaje = 50
                        self.poderes.tiene_volveralavida = False
                if self.level_number == 3:
                    self.poderes.run(self.screen, self.puntaje)
                    # PODERES
                    if self.poderes.es_inmune:
                        self.is_inmune = True
                        inmuneT = current_time + 5000
                        self.poderes.es_inmune = False
                    if self.poderes.tiene_alcanzame:
                        self.is_fast = True
                        fastT = current_time + 5000
                        self.poderes.tiene_alcanzame = False
                    if self.poderes.tiene_volveralavida:
                        self.puntaje = 50
                        self.poderes.tiene_volveralavida = False
                    ardilla.update()
                self.coord_x = player.rect.x
                self.coord_y = player.rect.y
                if player.rect.x < 0:
                    player.rect.x = 0
                if player.rect.x > 500:
                    player.rect.x = 500
                if random.random() < 0.03:
                    self.comida_model = comidaModel.create_food_or_junk(5, -10, 80, 80)
                    if self.level_number == 2:
                        self.comida_model = comidaModel.create_food_or_junk(
                            5, -15, 80, 80
                        )
                    if self.level_number == 3:
                        self.comida_model = comidaModel.create_food_or_junk(
                            10, -20, 80, 80
                        )

                    # yunque
                    self.foods_and_junk.append(self.comida_model.draw(level_number))

                    # Actualizar la posición de los alimentos y comida chatarra y eliminar los que han salido de la pantalla
                for item in self.foods_and_junk:
                    if self.level_number == 1 or self.level_number == 2:
                        item["y"] += 1.6  # Velocidad de descenso hacia abajo
                    # if self.level_number == 2:
                    # item["y"] += 3.2  # Velocidad de descenso hacia abajo
                    if self.level_number == 3:
                        item["y"] += 2.2  # Velocidad de descenso hacia abajo
                    if item["y"] > self.height:
                        self.foods_and_junk.remove(item)
                # Dibujar la pantalla
                for item in self.foods_and_junk:
                    self.screen.blit(item["image"], (item["x"], item["y"]))
                for item in self.foods_and_junk:
                    if hay_colision(item["x"], item["y"], self.coord_x, self.coord_y):
                        sonido_colision = pygame.mixer.Sound(
                            "Audio/ES_Human Bite Food 20 - SFX Producer.mp3"
                        )
                        sonido_colision.play()
                        self.foods_and_junk.remove(item)
                        if item["puntaje"] < 0:
                            # verifica si el objeto (presumiblemente una instancia de una clase) tiene un atributo llamado "poderes"
                            if hasattr(self, "poderes"):
                                if self.is_inmune:
                                    item["puntaje"] = 0
                                    # Disable the immunity after 5 seconds
                        self.puntaje += item["puntaje"]
                        self.tipo_comida = item["tipo"]
                        if item["is_yunque"]:
                            sonido_colision = pygame.mixer.Sound("Audio/sonidoYunque.mp3")
                            sonido_colision.play()
                            slowt = current_time + 5000
                            self.is_slow = True
                        if item["is_yunque"] == False:
                            self.texto_puntaje.append(
                                (
                                    self.coord_x,
                                    self.coord_y,
                                    item["puntaje"],
                                    current_time + 1500,
                                )
                            )
                for text in self.texto_puntaje[:]:
                    if text[3] > current_time:
                        puntajeComida(text[0], text[1], text[2], text[3])
                    else:
                        self.texto_puntaje.remove(text)
                if self.puntaje >= 100:
                    if self.level_number==3 and not player.isJumping:
                        self.game_state="endgame"
                        player1.endgame=True
                        player2.endgame=True
                    else:
                        if self.level_number!=3:
                            self.game_state = "winner"
                            self.audio_winner=True
                            self.mute()
                # Si el puntaje es menor de 0, marca fin del juego
                if self.health_bar.remaining_time == 0:
                    if self.level_number==3 and not player.isJumping:
                        self.game_state="endgame"
                        player1.endgame=True
                        player2.endgame=True
                    else:
                        if self.level_number!=3:
                            self.game_state = "winner"
                            self.audio_winner=True
                            self.mute()
                            continue

                if self.puntaje <= 0:
                    self.game_state = "game over"
                    continue

                if self.level_number == 3 and hay_colision(
                    ardilla.rect.x, ardilla.rect.y, self.coord_x, self.coord_y
                ):
                    self.game_state = "game over"
                    continue
                # self.madera = pygame.image.load("img/wood.png").convert_alpha()
                # self.madera = pygame.transform.scale(self.madera, (450, 100))
                # self.screen.blit(self.madera, [15, 5])

                self.wood = pygame.image.load("img/btn/btnBig.png").convert_alpha()
                self.wood = pygame.transform.scale(self.wood, (400, 130))
                self.screen.blit(self.wood, [40.5, -11])
                
                self.health_bar.hp = self.puntaje
                self.health_bar.draw(self.screen,self.idioma)
                self.corazon = pygame.image.load(
                    "img/btn/btnCorazon.png"
                ).convert_alpha()
                self.corazon = pygame.transform.scale(self.corazon, (80, 70))
                self.screen.blit(self.corazon, [30, 15])
                # Mandamos a llamar a nuestra función de "mostrar_puntaje"
                mostrar_puntaje(self.texto_x+1.5, self.texto_y-20, self.puntaje)
                # Cambiar gordura del personaje de acuerdo a cada puntaje
                if self.puntaje < 50:
                    if hasattr(self, "poderes"):
                        player.changeSprite(
                            genero, "gordo", color, self.is_slow, self.is_fast
                        )
                    else:
                        player.changeSprite(genero, "gordo", color, self.is_slow)
                else:
                    if hasattr(self, "poderes"):
                        player.changeSprite(
                            genero, complexion, color, self.is_slow, self.is_fast
                        )
                    else:
                        player.changeSprite(genero, complexion, color, self.is_slow)

                player.handle_event(event)
                if current_time > slowt:
                    self.is_slow = False
                if current_time > inmuneT:
                    if hasattr(self, "poderes"):
                        self.is_inmune = False
                if current_time > fastT:
                    if hasattr(self, "poderes"):
                        self.is_fast = False
                self.screen.blit(player.image, player.rect)

                btnInfo.draw(self.screen)
                btnMute.draw(self.screen)
                btnFlechas.draw(self.screen)
                if level_number==2 or level_number==3:
                    btnPociones.draw(self.screen)
                    btn1.draw(self.screen)
                    btn2.draw(self.screen)
                    btn3.draw(self.screen)

                mouse_x, mouse_y = pygame.mouse.get_pos()
                if btnInfo.is_hover(mouse_x, mouse_y):
                    btnInfo.change_image(btnInfo.hover_image)
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    btnInfo.change_image(btnInfo.normal_image)
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                if self.is_mute:
                    btnMute.change_image(btnMute.hover_image)
                else:
                    btnMute.change_image(btnMute.normal_image)
                # if btnMute.is_hover(mouse_x, mouse_y):
                #     pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                # else:
                #     pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
 


            pygame.display.flip()
            self.clock.tick(40)

        pygame.quit()
        sys.exit()
