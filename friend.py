import pygame
width, height = 600, 750
screen = pygame.display.set_mode((width, height))
class Friend(pygame.sprite.Sprite):
    def __init__(self, position,amigo,speed,direction,esArdilla=False):
        self.esArdilla=esArdilla
        if self.esArdilla:
            self.left_states = { 0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76) }
            self.right_states = { 0: (0, 0, 52, 76), 1: (52, 0, 52, 76), 2: (156, 0, 52, 76) }
            self.up_states = { 0: (0, 0, 52, 76), 1: (52, 0, 52, 76), 2: (156, 0, 52, 76) }
            self.sheet = pygame.image.load(f"img/amigos/spriteArdilla.png").convert_alpha()
        else:
            self.left_states = { 0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76) }
            self.right_states = { 0: (0, 152, 52, 76), 1: (52, 152, 52, 76), 2: (156, 152, 52, 76) }
            self.up_states = { 0: (0, 0, 52, 76), 1: (0, 0, 52, 76), 2:(0, 0, 52, 76) }
            self.sheet = pygame.image.load(f"img/amigos/sprite{amigo}.png").convert_alpha()
        self.sheet.set_clip(pygame.Rect(0, 0, 52, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.inicial=self.rect.x
        self.posicionInicial=False
        self.frame = 0
        self.speed = speed
        self.direction=direction
        self.endgame=False
    def reiniciar(self,position,amigo,speed,direction):
        self.sheet = pygame.image.load(f"img/amigos/{amigo}.png").convert_alpha()
        self.sheet.set_clip(pygame.Rect(0, 0, 52, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.speed = speed
        self.direction=direction
        if self.esArdilla:
            self.left_states = { 0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76) }
            self.right_states = { 0: (0, 0, 52, 76), 1: (52, 0, 52, 76), 2: (156, 0, 52, 76) }
            self.up_states = { 0: (0, 0, 52, 76), 1: (52, 0, 52, 76), 2: (156, 0, 52, 76) }
        else:
            self.left_states = { 0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76) }
            self.right_states = { 0: (0, 152, 52, 76), 1: (52, 152, 52, 76), 2: (156, 152, 52, 76) }
            self.up_states = { 0: (0, 0, 52, 76), 1: (0, 0, 52, 76), 2:(0, 0, 52, 76) }
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
    
    def update(self):
        if self.direction == True:
            
            if not self.posicionInicial:
                self.clip(self.left_states)
                self.rect.x -= self.speed
            else:
                self.clip(self.up_states)
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self.image = pygame.transform.scale(self.image, (100, 100))
                screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.direction == False:
            if not self.posicionInicial:
                self.clip(self.right_states)
                self.rect.x += self.speed
            else:
                self.clip(self.up_states)
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self.image = pygame.transform.scale(self.image, (100, 100))
                screen.blit(self.image, (self.rect.x, self.rect.y))
        
        if self.esArdilla:
             if self.rect.x>1200 or self.rect.x<-1000:
                self.direction=not self.direction
        else:
            if self.endgame:
                if self.inicial<300:
                    if self.rect.x>=200 and self.rect.x<=210:
                        self.posicionInicial=True
                if self.inicial>300:
                    if self.rect.x>=300 and self.rect.x<=310:
                        self.posicionInicial=True
                if self.rect.x>510 or self.rect.x<70:
                    self.direction=not self.direction 
            else:
                if self.rect.x>510 or self.rect.x<70:
                    self.direction=not self.direction 
        
        if self.posicionInicial==False:
            self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image = pygame.transform.scale(self.image, (100, 100))
        screen.blit(self.image, (self.rect.x, self.rect.y))