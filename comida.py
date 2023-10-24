import random,pygame
width, height = 600, 750
class create_food_or_junk():
    def __init__(self, puntaje_saludable, puntaje_chatarra, ancho_comida, largo_comida):
        self.puntaje_saludable = puntaje_saludable
        self.puntaje_chatarra = puntaje_chatarra
        self.ancho_comida = ancho_comida
        self.largo_comida = largo_comida
        
    def draw(self):
        # Lista de tipos de alimentos y comida chatarra
        food_types = ["img\comida\saludable\CEREZAS ORG.png", "img\comida\saludable\lechuga org.png", "img\comida\saludable\MANZANA ORG.png"
                    ,"img\comida\saludable\PIÑA ORG.png"]
        junk_types = ["img\comida\chatarra\COLA ORG.png", "img\comida\chatarra\HAMBUERGUESA2.png","img\comida\chatarra\PAPAS ORG.png",
                    "img\comida\chatarra\PASTEL2.png","img\comida\chatarra\PIZZA2.png","img\comida\chatarra\POLLA ORG.png"]
        # Elegir aleatoriamente entre alimentos y comida chatarra
        is_food = random.choice([True, False])

        # Elegir aleatoriamente el tipo de comida
        if is_food:
            food_type = random.choice(food_types)
            puntaje=self.puntaje_saludable
        else:
            food_type = random.choice(junk_types)
            puntaje=self.puntaje_chatarra
        # Definir la posición inicial en x y en la parte superior de la pantalla
        x = random.randint(0, width - 50)  # Ajusta el rango de x según tus necesidades
        y = 300  # comenzar abajo de la casa

        # Cargar la imagen de la comida
        food_image = pygame.image.load(food_type)

        # Escalar la imagen (ajusta el tamaño según tus necesidades)
        food_image = pygame.transform.scale(food_image, (self.ancho_comida, self.largo_comida))

        return {"image": food_image, "x": x, "y": y, "is_food": is_food, "puntaje":puntaje}