import pygame,random, math,sys
import comidaModel
from HealthBar import HealthBar
from funciones import hay_colision,mostrar_puntaje,draw_game_over_screen
pygame.init() 
width, height = 600, 750
screen = pygame.display.set_mode((width, height))
pygame.mixer.init() 
pygame.mixer.music.load('./Audio/ringtones-super-mario-bros.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
puntaje = 20
texto_x = 10
texto_y = 20
done=False
foods_and_junk = []
game_state="game"
pygame.display.set_caption("Nivel 1")

# Personajes
player1 = pygame.image.load("./img/amigos/friend1.png").convert_alpha()
player1 = pygame.transform.scale(player1, (100, 100))
player1_x = 80
player1_y = 195
player1_speed = 2

player2 = pygame.image.load("./img/amigos/friend2.png").convert_alpha()
player2 = pygame.transform.scale(player2, (100, 100))
player2_x = 510
player2_y = 195
player2_speed = 2


# Nos permite controlar los frame
clock = pygame.time.Clock()

#Subiendo el personaje, "alpha" es para poner la transparencia de la imagen
player = pygame.image.load("./img/hombre/delgado/enfrente.png").convert_alpha()
player = pygame.transform.scale(player, (100, 100))
# Ingresamos fondo
backgroundDay = pygame.image.load("./img/dia.png").convert()

# Coordenadas del mono
coord_x = 215
coord_y = 650
# Velocidad
x_speed = 0
y_speed = 0

sentido=1
health_bar = HealthBar(10, 10, 300, 10, 100)
while not done:
	for event in pygame.event.get():
		# print(event)
		if event.type == pygame.QUIT:
			# sys.exit()
			done=True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_speed = -4
			if event.key == pygame.K_RIGHT:
				x_speed = 4
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				x_speed = 0
				pass
			if event.key == pygame.K_RIGHT:
				x_speed = 0
				pass
	if game_state == "game over":
		draw_game_over_screen()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_r]:
			game_state = "start_menu"
		if keys[pygame.K_q]:
			pygame.quit()
			quit()		
	else:
		if player1_x>510 or player1_x<70:
			sentido=sentido*-1
		player1_x += player1_speed*sentido
		player2_x -= player2_speed*sentido
		coord_x += x_speed
		coord_y += y_speed
		
		# Se usa el método "blit" para imprimir la imagen
		screen.blit(backgroundDay,[0,0])
		if coord_x<0:
			coord_x=0
		if coord_x>500:
			coord_x=500
		screen.blit(player, (coord_x, coord_y))

		# Dibujar los personajes
		screen.blit(player1, (player1_x, player1_y))
		screen.blit(player2, (player2_x, player2_y))
		if random.random() < 0.02:
			comida_model=comidaModel.create_food_or_junk(5,-10,80,80)
			foods_and_junk.append(comida_model.draw())

		# Actualizar la posición de los alimentos y comida chatarra y eliminar los que han salido de la pantalla
		for item in foods_and_junk:
			item["y"] +=1  # Velocidad de descenso hacia abajo
			if item["y"] > height:   
				foods_and_junk.remove(item)
		# Dibujar la pantalla
		for item in foods_and_junk:
			screen.blit(item["image"], (item["x"], item["y"]))
	
		for item in foods_and_junk:
			if hay_colision(item["x"],item["y"],coord_x,coord_y):
				sonido_colision = pygame.mixer.Sound('./Audio/Comer.mp3')
				sonido_colision.play()
				foods_and_junk.remove(item)
				puntaje += item["puntaje"]
		if puntaje>100:
			puntaje=100
		if puntaje<=0:
			game_state="game over"
		mostrar_puntaje(texto_x, texto_y,puntaje)
	
		health_bar.hp=puntaje
		health_bar.draw(screen)
	
		#  Actualizamos pantalla
		pygame.display.flip()
		clock.tick(60)
		
		# Controlar la velocidad de actualización
		pygame.time.delay(20)
	
    
pygame.quit()
sys.exit()