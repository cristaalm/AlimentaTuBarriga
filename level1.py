# Importar librerías
import pygame
import random
# Incializando pygame
pygame.init() 

# Declaramos ventana con dimensiones específicas (screen)
width, height = 600, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Nivel 1")

# Colores de personajes secundarios de arriba 
white = (255,255,255)
pink = (255,192,203)

# Personajes secundarios de prueba
#Rosa
player1_width = 50
player1_height = 50
player1_x = 20
player1_y = 200
player1_speed = 4
#Blanco
player2_width = 50
player2_height = 50
player2_x = 530
player2_y = 200
player2_speed = 4

#Circulos aleatorios
# Definición de la función para crear alimentos y comida chatarra aleatoriamente
def create_food_or_junk():
    # Lista de tipos de alimentos y comida chatarra
    food_types = ["img\comida\saludable\CEREZAS ORG.png", "img\comida\saludable\lechuga.png", "img\comida\saludable\MANZANA ORG.png"
				  ,"img\comida\saludable\PIÑA ORG.png"]
    junk_types = ["img\comida\chatarra\COLA ORG.png", "img\comida\chatarra\HAMBUERGUESA2.png","img\comida\chatarra\PAPAS ORG.png",
				  "img\comida\chatarra\PASTEL2.png","img\comida\chatarra\PIZZA2.png","img\comida\chatarra\POLLA ORG.png"]
    # Elegir aleatoriamente entre alimentos y comida chatarra
    is_food = random.choice([True, False])

    # Elegir aleatoriamente el tipo de comida
    if is_food:
        food_type = random.choice(food_types)
    else:
        food_type = random.choice(junk_types)
    # Definir la posición inicial en x y en la parte superior de la pantalla
    x = random.randint(0, width - 50)  # Ajusta el rango de x según tus necesidades
    y = 300  # comenzar abajo de la casa

    # Cargar la imagen de la comida
    food_image = pygame.image.load(food_type)

    # Escalar la imagen (ajusta el tamaño según tus necesidades)
    food_image = pygame.transform.scale(food_image, (75, 75))

    return {"image": food_image, "x": x, "y": y, "is_food": is_food}
# Nos permite controlar los frame
clock = pygame.time.Clock()
done=False

#Subiendo el personaje, "alpha" es para poner la transparencia de la imagen
player = pygame.image.load("./img/hombre/delgado/enfrente.png").convert_alpha() 
player = pygame.transform.scale(player, (100, 100))
#amigos
amigo1 = pygame.image.load("img/amigos/pixil-frame-0 (1).png").convert_alpha() 
amigo1 = pygame.transform.scale(amigo1, (100, 100))
amigo2 = pygame.image.load("img/amigos/pixil-frame-0.png").convert_alpha() 
amigo2 = pygame.transform.scale(amigo2, (100, 100))
# Ingresamos fondo
backgroundDay = pygame.image.load("./img/dia.png").convert()

# Coordenadas del personaje
coord_x = 215
coord_y = 650
# Velocidad inicial
x_speed = 0
y_speed = 0

# Lista para almacenar alimentos y comida chatarra
foods_and_junk = []

while not done:
	for event in pygame.event.get():
		# print(event)
		if event.type == pygame.QUIT:
			# sys.exit()
			done=True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_speed = -5
			if event.key == pygame.K_RIGHT:
				x_speed = 5


		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				x_speed = 0
				pass
			if event.key == pygame.K_RIGHT:
				x_speed = 0
				pass
#limite de la pantalla de movimiento del personaje principal
	if (coord_x > 500 or coord_x < 0):
		x_speed *= -1
	if (coord_y > 0 or coord_y < 0):
		y_speed *= 1

	# Mover los personajes de izquierda a derecha
	player1_x += player1_speed
	player2_x -= player2_speed

	coord_x += x_speed
	coord_y += y_speed
	
	# Se usa el método "blit" para imprimir la imagen
	screen.blit(backgroundDay,[0,0])
	screen.blit(player, (coord_x, coord_y))

    # Dibujar los personajes "amigos"
	screen.blit(amigo1, (player1_x,player1_y))
	screen.blit(amigo2, (player2_x,player2_y))


	#dibujar circulos
	# Crear un nuevo alimento o comida chatarra con cierta probabilidad
	if random.random() < 0.02:
		foods_and_junk.append(create_food_or_junk())

    # Actualizar la posición de los alimentos y comida chatarra y eliminar los que han salido de la pantalla
	for item in foods_and_junk:
		item["y"] += 5  # Velocidad de descenso hacia abajo
		if item["y"] > height:   
			foods_and_junk.remove(item)
    # Dibujar la pantalla
	for item in foods_and_junk:
		screen.blit(item["image"], (item["x"], item["y"]))

	  #limite de la pantalla de movimiento del personajes secundarios 	
	if (player1_x > 500 or player1_x < 0):
		player1_speed *= -1

	if (player2_x > 549 or player2_x < 0):
		player2_speed *= -1
	#  Actualizamos pantalla
	pygame.display.flip()
	clock.tick(60)
 
     # Controlar la velocidad de actualización
	pygame.time.delay(20)
    
pygame.quit()