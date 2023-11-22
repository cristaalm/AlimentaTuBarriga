import pygame

class Button():
    def __init__(self, x, y, normal_image, hover_image, scale):
        self.normal_image = pygame.transform.scale(normal_image, (int(normal_image.get_width() * scale), int(normal_image.get_height() * scale)))
        self.hover_image = pygame.transform.scale(hover_image, (int(hover_image.get_width() * scale), int(hover_image.get_height() * scale)))
        self.image = self.normal_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def is_hover(self, mouse_x, mouse_y):
        return self.rect.collidepoint(mouse_x, mouse_y)

    def change_image(self, new_image):
        self.image = new_image

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))