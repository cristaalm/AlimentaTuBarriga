import random,pygame
width, height = 600, 750
class create_food_or_junk():
    def __init__(self, puntaje_saludable, puntaje_chatarra, ancho_comida, largo_comida):
        self.puntaje_saludable = puntaje_saludable
        self.puntaje_chatarra = puntaje_chatarra
        self.ancho_comida = ancho_comida
        self.largo_comida = largo_comida
        
    def draw(self,level_number):
        # Lista de tipos de alimentos y comida chatarra
        is_yunque=False
        food_types = ["img/comida/saludable/cerezas.png", "img/comida/saludable/lechuga.png", "img/comida/saludable/manzana.png","img/comida/saludable/piña.png","img/comida/saludable/plátano.png","img/comida/saludable/sandía.png","img/comida/saludable/tomate.png","img/comida/saludable/uva.png","img/comida/saludable/zanahoria.png"]
        if level_number>1:
            junk_types = ["img/comida/chatarra/PESA.png","img/comida/chatarra/coca.png", "img/comida/chatarra/papas.png","img/comida/chatarra/hamburguesita.png",
                    "img/comida/chatarra/pastelito.png","img/comida/chatarra/PESA.png","img/comida/chatarra/pizza.png","img/comida/chatarra/pollo.png","img/comida/chatarra/PESA.png"]
        else:
            junk_types = ["img/comida/chatarra/coca.png", "img/comida/chatarra/papas.png","img/comida/chatarra/hamburguesita.png",
                    "img/comida/chatarra/pastelito.png","img/comida/chatarra/pizza.png","img/comida/chatarra/pollo.png"]
        is_food = random.choice([True, False])
        
        # Elegir aleatoriamente el tipo de comida
        if is_food:
            food_type = random.choice(food_types)
            puntaje=self.puntaje_saludable
            tipo = 1
        else:
            food_type = random.choice(junk_types)
            puntaje=self.puntaje_chatarra
            tipo = 2
            if "PESA" in food_type:
                is_yunque=True
                puntaje=0
        # Definir la posición inicial en x y en la parte superior de la pantalla
        x = random.randint(0, width - 50)  # Ajusta el rango de x según tus necesidades
        y = 300  # comenzar abajo de la casa

        # Cargar la imagen de la comida
        food_image = pygame.image.load(food_type)

        # Escalar la imagen (ajusta el tamaño según tus necesidades)
        food_image = pygame.transform.scale(food_image, (self.ancho_comida, self.largo_comida))

        return {"image": food_image, "x": x, "y": y, "is_food": is_food, "puntaje":puntaje,"tipo":tipo,"is_yunque":is_yunque}